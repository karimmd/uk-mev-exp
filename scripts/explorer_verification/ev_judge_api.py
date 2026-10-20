#!/usr/bin/env python3
"""Score each explorer card with one API-served model reader following a protocol file.

Usage: ev_judge_api.py protocol.md cards_dir out_dir --reader {sonnet,opus,deepseek} [--workers N] [--limit N]
The reader gets the protocol and one card as a single user message (no system prompt, no tools) and must
answer with one JSON object; the prompt text is byte-identical to the one ev_judge.py sent through Claude Code.
Resumable: a case whose judgment exists is skipped. Writes judgments/<case>.json and sheet.csv (same layout
as ev_judge.py) plus the model id the endpoint reports, the settings, the usage and the request id per card.
Credentials come from api_info.txt at the project root; nothing from it is written to the outputs.
"""
import argparse, csv, glob, json, os, re, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
READERS = {
    "sonnet":   {"provider": "anthropic", "model": "claude-sonnet-5-5", "effort": "high"},
    "opus5":    {"provider": "anthropic", "model": "claude-opus-5",     "effort": "high"},
    "opus55":   {"provider": "anthropic", "model": "claude-opus-5-5",   "effort": "high"},
    "deepseek": {"provider": "deepseek",  "model": "deepseek-flash",    "effort": "high"},
}
MAX_TOKENS = 16000
RETRIES = 6

class Refusal(Exception):
    """The endpoint's safety classifier declined the card (stop_reason refusal); not retried, recorded as such."""

def creds():
    txt = open(os.path.join(ROOT, "api_info.txt")).read()
    ds, cl = txt.split("# Claude")[0], txt.split("# Claude")[1]
    g = lambda s, k: (re.search(k + r":\s*(\S+)", s) or [None, None])[1]
    return {"deepseek_key": g(ds, "api"), "deepseek_base": g(ds, "base_url"),
            "anthropic_key": g(cl, "api"), "anthropic_workspace": g(cl, "workspace-id")}

C = creds()

def ask_anthropic(model, effort, prompt):
    # Raw HTTP rather than the anthropic SDK: on this desktop the SDK's httpx transport drops the connection
    # within seconds (APITimeoutError) while a plain urllib request to the same endpoint completes.
    body = {"model": model, "max_tokens": MAX_TOKENS, "output_config": {"effort": effort},
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=json.dumps(body).encode(),
                                 headers={"x-api-key": C["anthropic_key"], "anthropic-version": "2023-06-01",
                                          "anthropic-workspace-id": C["anthropic_workspace"], "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as resp:
        r = json.loads(resp.read()); hdr = dict(resp.headers)
    if r.get("stop_reason") == "refusal":
        raise Refusal(json.dumps({"stop_details": r.get("stop_details"), "request_id": hdr.get("request-id") or hdr.get("Request-Id")}))
    if r.get("stop_reason") != "end_turn":
        raise RuntimeError("stop_reason %s" % r.get("stop_reason"))
    text = "".join(b.get("text", "") for b in r["content"] if b.get("type") == "text")
    u = r.get("usage", {})
    meta = {"_model": r.get("model"), "_settings": {"effort": effort, "thinking": "adaptive (default)", "max_tokens": MAX_TOKENS,
                                                    "system_prompt": None, "tools": None, "interface": "Anthropic Messages API"},
            "_usage": {"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                       "thinking_tokens": (u.get("output_tokens_details") or {}).get("thinking_tokens")},
            "_request_id": hdr.get("request-id") or hdr.get("Request-Id"), "_response_id": r.get("id")}
    return text, meta

def ask_deepseek(model, effort, prompt):
    body = {"model": model, "max_tokens": MAX_TOKENS, "reasoning_effort": effort,
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(C["deepseek_base"].rstrip("/") + "/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Authorization": "Bearer " + C["deepseek_key"], "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as resp:
        r = json.loads(resp.read()); hdr = dict(resp.headers)
    ch = r["choices"][0]
    if ch.get("finish_reason") != "stop":
        raise RuntimeError("finish_reason %s" % ch.get("finish_reason"))
    text = ch["message"]["content"]
    u = r.get("usage", {})
    meta = {"_model": r.get("model"), "_settings": {"reasoning_effort": effort, "max_tokens": MAX_TOKENS,
                                                    "system_prompt": None, "tools": None, "interface": "DeepSeek chat completions API"},
            "_usage": {"input_tokens": u.get("prompt_tokens"), "output_tokens": u.get("completion_tokens"),
                       "thinking_tokens": (u.get("completion_tokens_details") or {}).get("reasoning_tokens")},
            "_request_id": hdr.get("x-ds-trace-id") or hdr.get("X-Ds-Trace-Id") or hdr.get("x-request-id"),
            "_response_id": r.get("id"), "_system_fingerprint": r.get("system_fingerprint")}
    return text, meta

def ask(reader, proto, card):
    spec = READERS[reader]
    prompt = proto + "\n\n---\n\n# Card\n\n" + card + "\n\nAnswer with the JSON object only."
    fn = ask_anthropic if spec["provider"] == "anthropic" else ask_deepseek
    err = None
    for i in range(RETRIES):
        try:
            text, meta = fn(spec["model"], spec["effort"], prompt)
            m = re.search(r"\{.*\}", text, re.S)
            ans = json.loads(m.group(0))
            ans.update(meta); ans["_reader"] = reader
            return ans, text
        except Refusal as e:
            return None, "REFUSAL " + str(e)
        except Exception as e:
            err = "%s: %s" % (type(e).__name__, str(e)[:300])
            time.sleep(5 + 10 * i)
    return None, err

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("protocol"); ap.add_argument("cards_dir"); ap.add_argument("out_dir")
    ap.add_argument("--reader", required=True, choices=sorted(READERS))
    ap.add_argument("--workers", type=int, default=2); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-tokens", type=int, default=16000, help="output limit per reading (16000 in the v1 run, 32000 under amendment 1)")
    a = ap.parse_args()
    globals()["MAX_TOKENS"] = a.max_tokens
    jd = os.path.join(a.out_dir, "judgments"); os.makedirs(jd, exist_ok=True)
    proto = open(a.protocol).read()
    cards = sorted(glob.glob(os.path.join(a.cards_dir, "*.md")))
    if a.limit: cards = cards[:a.limit]
    todo = [p for p in cards if not os.path.exists(os.path.join(jd, os.path.basename(p)[:-3] + ".json"))]
    print("%s reader=%s model=%s cards=%d todo=%d" % (time.strftime("%H:%M:%S"), a.reader, READERS[a.reader]["model"], len(cards), len(todo)), flush=True)

    def one(path):
        cid = os.path.basename(path)[:-3]
        ans, text = ask(a.reader, proto, open(path).read())
        if ans is None:
            if text.startswith("REFUSAL "):
                rd = os.path.join(a.out_dir, "refusals"); os.makedirs(rd, exist_ok=True)
                json.dump({"case_id": cid, "_reader": a.reader, "_model": READERS[a.reader]["model"], "_time": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                           **json.loads(text[8:])}, open(os.path.join(rd, cid + ".json"), "w"), indent=1)
            print("%s %s FAILED %s" % (time.strftime("%H:%M:%S"), cid, text), flush=True); return
        ans["_raw"] = text; ans["case_id"] = cid; ans["_time"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        tmp = os.path.join(jd, cid + ".json.tmp")
        json.dump(ans, open(tmp, "w"), indent=1); os.replace(tmp, os.path.join(jd, cid + ".json"))
        print("%s %s Q1=%s Q2=%s conf=%s out_tok=%s" % (time.strftime("%H:%M:%S"), cid, ans.get("Q1"), ans.get("Q2"), ans.get("confidence"), ans["_usage"].get("output_tokens")), flush=True)

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        list(ex.map(one, todo))

    with open(os.path.join(a.out_dir, "sheet.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["case_id", "scorer", "Q1_sandwich", "Q2_positive_after_cost", "confidence_1to5", "actor", "note"])
        for jp in sorted(glob.glob(os.path.join(jd, "*.json"))):
            j = json.load(open(jp))
            w.writerow([j["case_id"], j.get("_model"), j.get("Q1"), j.get("Q2"), j.get("confidence"), j.get("actor"), (j.get("note") or "").replace("\n", " ")])
    done = len(glob.glob(os.path.join(jd, "*.json")))
    print("judge complete %d of %d" % (done, len(cards)), flush=True)
    sys.exit(0 if done == len(cards) else 1)

if __name__ == "__main__":
    main()

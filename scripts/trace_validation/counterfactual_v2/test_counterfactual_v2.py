import ast, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import state2 as S

OK, FAIL = [], []
def check(name, cond, extra=""):
    (OK if cond else FAIL).append(name)
    print(("  ok   " if cond else "  FAIL ") + name + (("  " + str(extra)) if extra and not cond else ""))

Z = S.ZERO32
A, B, C = "0x" + "a" * 40, "0x" + "b" * 40, "0x" + "c" * 40
SLOT0, SLOT1 = "0x" + "00" * 31 + "00", "0x" + "00" * 31 + "01"

def d(pre=None, post=None):
    return {"pre": pre or {}, "post": post or {}}

print("\n[1] tier-1 envelope normalization")
raw = [{"txHash": "0x1", "result": d({A: {"balance": "0x1"}}, {A: {"balance": "0x2"}})}]
n = S.normalize_tier1(raw, 1)
check("unwraps the {txHash,result} envelope exactly once", n[0]["post"][A]["balance"] == "0x2")
check("idempotent on already-unwrapped tier-2 shape",
      S.normalize_tier1([d({A: {}}, {A: {}})], 1)[0]["post"] == {A: {}})
try:
    S.normalize_tier1([{"txHash": "0x1", "result": {"pre": {}}}], 1); bad = False
except S.RpcError: bad = True
check("rejects a malformed inner result", bad)
try:
    S.normalize_tier1(raw, 2); card = False
except S.RpcError: card = True
check("T5 cardinality shortfall raises", card)

print("\n[2] zeroed storage slots")
zd = d({A: {"storage": {SLOT0: "0x5", SLOT1: "0x7"}}}, {A: {"storage": {SLOT0: "0x9"}}})
check("slot in pre and absent from post is detected", S.zeroed_slots(zd) == {A: {SLOT1}})
ov = S.accumulate([zd])
check("zeroed slot accumulates as 32-byte zero", ov[A]["stateDiff"][SLOT1] == Z)
check("ordinary write still accumulates", ov[A]["stateDiff"][SLOT0] == "0x9")
check("a v1-style post-only accumulator would have missed it",
      SLOT1 not in {k: v for k, v in (d({}, {A: {"storage": {SLOT0: "0x9"}}})
                                      .get("post")[A]["storage"]).items()})

print("\n[3] accumulation order and completeness")
o = S.accumulate([d({}, {A: {"storage": {SLOT0: "0x1"}}}), d({}, {A: {"storage": {SLOT0: "0x2"}}})])
check("later write wins", o[A]["stateDiff"][SLOT0] == "0x2")
o2 = S.accumulate([d({}, {A: {"balance": "0x1", "nonce": 3, "code": "0xfe",
                             "storage": {SLOT0: "0x1"}}})])
check("balance, nonce, code and storage all carried",
      o2[A]["balance"] == "0x1" and o2[A]["nonce"] == 3 and o2[A]["code"] == "0xfe"
      and o2[A]["stateDiff"][SLOT0] == "0x1")

print("\n[4] empty-override precondition")
try:
    S.assert_overrides_sound([d({}, {A: {"balance": "0x2"}})], {}); raised = False
except S.ReconstructionError: raised = True
check("state-changing prefix with empty overrides RAISES", raised)
check("empty prefix with empty overrides is fine", S.assert_overrides_sound([], {}))
check("prefix_changes_state false on no-op diffs", not S.prefix_changes_state([d({}, {})]))

print("\n[5] block context")
try:
    S.block_context({"number": "0x1"}); raised = False
except S.ReconstructionError: raised = True
check("missing timestamp RAISES (the v1 defect)", raised)
bc = S.block_context({"number": "0x1", "timestamp": "0x64", "baseFeePerGas": "0x7",
                      "gasLimit": "0x9", "miner": C})
check("time is carried", bc["time"] == "0x64")
check("baseFee/gasLimit/feeRecipient carried", bc["baseFee"] == "0x7" and bc["gasLimit"] == "0x9"
      and bc["feeRecipient"] == C)

print("\n[6] call construction")
c = S.call_from_tx({"from": A, "gas": "0x1", "to": B, "input": "0xab", "gasPrice": "0x5",
                    "nonce": "0x2", "accessList": [{"address": C, "storageKeys": []}]})
check("fee fields carried", c["gasPrice"] == "0x5")
check("access list carried", c["accessList"][0]["address"] == C)
check("nonce carried", c["nonce"] == "0x2")
t2 = S.call_from_tx({"from": A, "gas": "0x1", "to": B, "gasPrice": "0x5",
                     "maxFeePerGas": "0x9", "maxPriorityFeePerGas": "0x1"})
check("type-2 tx sends 1559 fields and NOT gasPrice (they are mutually exclusive)",
      "gasPrice" not in t2 and t2["maxFeePerGas"] == "0x9", t2)
t0 = S.call_from_tx({"from": A, "gas": "0x1", "to": B, "gasPrice": "0x5"})
check("legacy tx still sends gasPrice", t0["gasPrice"] == "0x5" and "maxFeePerGas" not in t0)

print("\n[7] decoded token output")
def xfer(tok, frm, to, amt):
    return (tok, (S.XFER, "0x" + "00" * 12 + frm[2:], "0x" + "00" * 12 + to[2:]),
            "0x" + hex(amt)[2:].rjust(64, "0"))
logs = [xfer(C, B, A, 500), xfer(C, A, B, 200)]
check("net position is signed and netted", S.token_deltas(logs, A) == {C: 300})
check("unrelated actor sees nothing", S.token_deltas(logs, "0x" + "d" * 40) == {})
check("zero net position is dropped", S.token_deltas([xfer(C, A, B, 5), xfer(C, B, A, 5)], A) == {})

print("\n[7b] transfer multiset is the positive criterion")
tm = S.transfer_multiset(logs)
check("captures every Transfer with exact value", len(tm) == 2 and tm[0][3] in (200, 500))
check("a changed amount changes the multiset",
      S.transfer_multiset([xfer(C, B, A, 499)]) != S.transfer_multiset([xfer(C, B, A, 500)]))
check("non-Transfer logs are excluded",
      S.transfer_multiset([(C, ("0xdead",), "0x")]) == [])
eoa_logs = [xfer(C, B, "0x" + "e" * 40, 700)]
check("SENDER-NET criterion would be vacuous here (the v1-of-05 defect)",
      S.token_deltas(eoa_logs, A) == {})
check("transfer multiset is NOT vacuous here", len(S.transfer_multiset(eoa_logs)) == 1)

print("\n[7c] R2-05B exact shared-pool Swap-amount criterion")
P1, P2, P3 = "0x" + "9" * 40, "0x" + "8" * 40, "0x" + "7" * 40
def w(*vals):
    out = "0x"
    for v in vals:
        out += format(v & ((1 << 256) - 1), "064x")
    return out
def v2swap(pool, a0i, a1i, a0o, a1o):
    return (pool, (S.V2_SWAP_TOPIC, "0x0", "0x0"), w(a0i, a1i, a0o, a1o))
def v3swap(pool, a0, a1):
    return (pool, (S.V3_SWAP_TOPIC, "0x0", "0x0"), w(a0, a1, 0, 0, 0))

vec, err = S.decode_swap_vector([v2swap(P1, 11, 22, 33, 44)], {P1})
check("F1 V2 decodes all four amount fields",
      err is None and vec[0]["amounts"] == [11, 22, 33, 44], (vec, err))
vec, err = S.decode_swap_vector([v3swap(P1, -1000, 2500)], {P1})
check("F2 V3 decodes signed two's-complement both ways",
      err is None and vec[0]["amounts"] == [-1000, 2500], (vec, err))
a, _ = S.decode_swap_vector([v2swap(P1, 100, 0, 0, 900)], {P1})
b, _ = S.decode_swap_vector([v2swap(P1, 100, 0, 0, 880)], {P1})
check("F3 exact-INPUT: changed output detected", bool(S.vector_changes(a, b)))
a, _ = S.decode_swap_vector([v2swap(P1, 100, 0, 0, 900)], {P1})
b, _ = S.decode_swap_vector([v2swap(P1, 130, 0, 0, 900)], {P1})
ch = S.vector_changes(a, b)
check("F4 exact-OUTPUT: changed input detected", bool(ch))
check("F4 direction recorded per field (not collapsed to a Boolean)",
      ch and ch[0]["delta"][0] == "30" and ch[0]["delta"][3] == "0", ch)
a, _ = S.decode_swap_vector([v3swap(P1, -83010000000, 21999227284318703755)], {P1})
b, _ = S.decode_swap_vector([v3swap(P1, -83010000000, 22500000000000000000)], {P1})
check("F5 routed V3 exact-output false negative is now DETECTED", bool(S.vector_changes(a, b)))
logs_mp = [v2swap(P2, 1, 0, 0, 2), v3swap(P1, -5, 7)]
vec, err = S.decode_swap_vector(logs_mp, {P1, P2})
check("F6 every shared pool included, sorted deterministically",
      err is None and [e["pool"] for e in vec] == sorted([P1, P2]), vec)
check("F6 dropping a pool changes the vector (no cherry-picking)",
      S.decode_swap_vector(logs_mp, {P1})[0] != vec)
base = [v2swap(P1, 100, 0, 0, 900)]
check("F7 unrelated ERC-20 transfer does not affect the vector",
      S.decode_swap_vector(base + [xfer(C, A, B, 5)], {P1})[0] == S.decode_swap_vector(base, {P1})[0])
check("F7 Swap on a NON-shared pool does not affect the vector",
      S.decode_swap_vector(base + [v2swap(P3, 7, 7, 7, 7)], {P1})[0]
      == S.decode_swap_vector(base, {P1})[0])
check("F7 a Deposit/raw log does not affect the vector",
      S.decode_swap_vector(base + [(C, ("0xe1fffcc4",), "0x")], {P1})[0]
      == S.decode_swap_vector(base, {P1})[0])
check("F8 no shared pool -> error", S.decode_swap_vector(base, set())[1] == "no_shared_pool")
check("F8 shared pool with no Swap -> error",
      S.decode_swap_vector([xfer(C, A, B, 1)], {P1})[1] == "no_swap_event_on_shared_pool")
check("F8 malformed V2 data -> error",
      S.decode_swap_vector([(P1, (S.V2_SWAP_TOPIC, "0x0", "0x0"), "0x1234")], {P1})[1]
      == "malformed_v2_swap_data")
check("F8 malformed V3 data -> error",
      S.decode_swap_vector([(P1, (S.V3_SWAP_TOPIC, "0x0", "0x0"), "0x")], {P1})[1]
      == "malformed_v3_swap_data")
a, _ = S.decode_swap_vector([v2swap(P1, 1, 2, 3, 4)], {P1})
b, _ = S.decode_swap_vector([v3swap(P1, 1, 2)], {P1})
check("F8 venue/arity mismatch is NOT comparable", not S.vectors_comparable(a, b))
check("F8 differing event counts are NOT comparable",
      not S.vectors_comparable(a, S.decode_swap_vector([v2swap(P1,1,2,3,4), v2swap(P1,5,6,7,8)], {P1})[0]))
check("F8 identical vectors compare equal and yield no change", not S.vector_changes(a, a))

print("\n[8] taint: transitive A -> B")
opening = d({}, {A: {"storage": {SLOT0: "0x1"}}})
slots, accts = S.merge_post(set(), set(), opening)
txB = {A: {"storage": {SLOT0: "0x0"}}}
check("B intersects the opening's tainted slot", S.intersects(txB, slots, accts))
rexB = d({}, {B: {"storage": {SLOT1: "0x9"}}})
slots, accts = S.merge_post(slots, accts, rexB)
txC = {B: {"storage": {SLOT1: "0x9"}}}
check("C is tainted transitively through B", S.intersects(txC, slots, accts))
check("a direct-overlap-only gate would have MISSED C",
      not S.intersects(txC, *S.merge_post(set(), set(), opening)))
check("a genuinely disjoint tx is not tainted",
      not S.intersects({C: {"storage": {SLOT0: "0x1"}}}, *S.merge_post(set(), set(), opening)))
check("zeroed slot also propagates taint",
      ("0x" + "a" * 40, SLOT1) in S.merge_post(set(), set(),
          d({A: {"storage": {SLOT1: "0x3"}}}, {A: {"storage": {}}}))[0])

print("\n[9] balance rule is conservative")
op = d({A: {"balance": "0x1"}}, {A: {"balance": "0x2", "code": "0xfe"}})
cb = S.contaminated_contract_balances(op, fee_recipient=C)
check("contaminated CONTRACT balance is flagged", cb == {A})
eoa = d({A: {"balance": "0x1"}}, {A: {"balance": "0x2"}})
check("EOA gas bookkeeping is NOT flagged", S.contaminated_contract_balances(eoa, C) == set())
fr = d({C: {"balance": "0x1"}}, {C: {"balance": "0x2", "code": "0xfe"}})
check("fee recipient is excluded", S.contaminated_contract_balances(fr, C) == set())
check("unchanged balance is not flagged",
      S.contaminated_contract_balances(d({A: {"balance": "0x2"}},
                                         {A: {"balance": "0x2", "code": "0xfe"}}, ), C) == set())
check("a contaminated balance in the read set is UNCERTAIN", S.balance_uncertain({A: {}}, cb))
check("an unrelated read set is not uncertain", S.balance_uncertain({B: {}}, cb) is False)

print("\n[10] self-destruct / account replacement")
sd = d({A: {"balance": "0x5", "code": "0xfe", "storage": {SLOT0: "0x1"}}}, {})
check("account present in pre and absent from post zeroes its slots",
      S.zeroed_slots(sd) == {A: {SLOT0}})
check("its slots enter the taint set", ("0x" + "a" * 40, SLOT0) in S.merge_post(set(), set(), sd)[0])

print("\n[11] incremental accumulation == batch accumulation")
seq = [d({}, {A: {"storage": {SLOT0: "0x1"}, "balance": "0x1"}}),
       d({A: {"storage": {SLOT1: "0x3"}}}, {A: {"storage": {SLOT0: "0x2"}}}),
       d({}, {B: {"nonce": 2, "code": "0xab"}})]
inc = {}
for x in seq:
    S.apply_diff(inc, x)
check("apply_diff folded in order equals accumulate over the sequence", inc == S.accumulate(seq),
      (inc, S.accumulate(seq)))
check("later write still wins under incremental folding", inc[A]["stateDiff"][SLOT0] == "0x2")
check("zeroed slot survives incremental folding", inc[A]["stateDiff"][SLOT1] == Z)

print("\n[11b] frozen subset rule and provider disagreement")
import witness2 as W2
check("scope is ADJACENT_ONLY", W2.TOLERANCE["scope"] == "ADJACENT_ONLY")
check("subset rule is frozen", W2.SUBSET_RULE == "victim_index == opening_index + 1")
src_w = open(os.path.join(HERE, "witness2.py")).read()
i_sub = src_w.index("subset_ineligible"); i_cf = src_w.index("-- counterfactual arm")
check("subset gate precedes the counterfactual path (never executed for non-adjacent)",
      i_sub < i_cf)
i_t4 = src_w.index("provider_disagreement")
check("F9 provider disagreement returns undecidable, never positive/negative",
      '_fail("undecidable", "provider_disagreement"' in src_w)
check("F9 T4 compares the decoded shared-pool vector, not only gas and logs",
      "v2vec == got_tok" in src_w)
check("counterfactual REVERT returns undecidable, never positive",
      '_fail("undecidable", "counterfactual_reverts_amounts_incomparable"' in src_w
      and '"positive", "counterfactual_victim_reverts"' not in src_w)
check("relevant pools are fixed before the counterfactual arm",
      src_w.index("shared_pools") < src_w.index("-- counterfactual arm"))
check("T4 disagreement is checked before the counterfactual arm", i_t4 < i_cf)

print("\n[12] independence (AST)")
src = open(os.path.join(HERE, "witness2.py")).read()
tree = ast.parse(src)
imports = set()
for n in ast.walk(tree):
    if isinstance(n, ast.Import):
        imports |= {a.name for a in n.names}
    elif isinstance(n, ast.ImportFrom):
        imports.add(n.module or "")
strings = {n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)}
check("does not import the v1 package", not any("counterfactual." in i or i == "witness" or i == "state"
                                                for i in imports), imports)
check("no group/outcome column name appears",
      not ({"group", "is_sandwich", "label", "treatment", "outcome", "arm"} & strings))
check("no canonical matching import", not any("match" in i for i in imports))

print("\n%d passed, %d failed" % (len(OK), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL); sys.exit(1)

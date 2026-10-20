#!/usr/bin/env bash
# Multi-reader explorer validation: one reader over the four card samples, through its vendor's API.
# Usage: [VERSION=v1|v2] [WORKERS=n] run_multi_reader.sh <reader>   (sonnet | opus55 | deepseek); launched detached per reader.
# v1: PROTOCOL.md / PROTOCOL_ARBITRAGE.md, 16000 output tokens, out/explorer_verification_api/.
# v2 (amendment 1): PROTOCOL_v2.md / PROTOCOL_ARBITRAGE_v2.md, 32000 output tokens, out/explorer_verification_api_v2/.
set -u
reader="$1"
VERSION="${VERSION:-v1}"
R=/home/user/Google-Drive/G-Projects/research/uk-mev/server/revision
EV=$R/out/explorer_verification
if [ "$VERSION" = v2 ]; then OUT=$R/out/explorer_verification_api_v2/$reader; SFX=_v2; MT=32000; else OUT=$R/out/explorer_verification_api/$reader; SFX=; MT=16000; fi
mkdir -p "$OUT"
echo "start $(date -Is) host $(hostname) reader $reader version $VERSION" | tee -a "$OUT/run.log"
rc=0
for s in f1b sym100 rej53 arb106; do
  proto=PROTOCOL$SFX.md; [ "$s" = arb106 ] && proto=PROTOCOL_ARBITRAGE$SFX.md
  python3 "$R/scripts/explorer_verification/ev_judge_api.py" "$R/notes/explorer_verification/$proto" "$EV/$s/cards" "$OUT/$s" --reader "$reader" --workers "${WORKERS:-2}" --max-tokens $MT >> "$OUT/run.log" 2>&1 || rc=1
done
if [ $rc -eq 0 ]; then echo "DONE $(date -Is)" | tee -a "$OUT/run.log" "$OUT/DONE"; else echo "INCOMPLETE $(date -Is)" | tee -a "$OUT/run.log"; fi

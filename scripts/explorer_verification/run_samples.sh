#!/usr/bin/env bash
set -u
export PATH="$HOME/.local/bin:$PATH"
R=$MEV_ROOT/revision
EV=$R/out/explorer_verification
export ETHERSCAN_API_KEY="$(grep -oE 'ETHERSCAN_API_KEY = "[A-Za-z0-9]+"' "$R/../previous/Part-3_Baseline_Comparison/GNN_GAT_Analysis/validate_unknown_transactions.py" | cut -d'"' -f2)"
echo "start $(date -Is) host $(hostname)"
run_one () {
  local name=$1 proto=$2
  local OUT=$EV/$name
  if [ -f "$OUT/DONE" ]; then echo "$name already DONE"; return 0; fi
  echo "== $name start $(date -Is)"
  python3 "$R/scripts/explorer_verification/ev_fetch.py" "$OUT/cases.csv" "$OUT" || { echo "$name fetch FAILED $(date -Is)"; return 1; }
  python3 "$R/scripts/explorer_verification/ev_judge.py" "$proto" "$OUT/cards" "$OUT" --model claude-sonnet-5-5 || { echo "$name judge FAILED $(date -Is)"; return 1; }
  echo "DONE $(date -Is)" | tee "$OUT/DONE"
}
run_one sym100 "$R/notes/explorer_verification/PROTOCOL.md"
run_one rej53  "$R/notes/explorer_verification/PROTOCOL.md"
run_one arb106 "$R/notes/explorer_verification/PROTOCOL_ARBITRAGE.md"
echo "ALL DONE $(date -Is)" | tee "$EV/SAMPLES_DONE"

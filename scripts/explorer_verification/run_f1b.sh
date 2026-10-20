#!/usr/bin/env bash
set -u
export PATH="$HOME/.local/bin:$PATH"
R=$MEV_ROOT/revision
OUT=$R/out/explorer_verification/f1b
export ETHERSCAN_API_KEY="$(grep -oE 'ETHERSCAN_API_KEY = "[A-Za-z0-9]+"' "$R/../previous/Part-3_Baseline_Comparison/GNN_GAT_Analysis/validate_unknown_transactions.py" | cut -d'"' -f2)"
mkdir -p "$OUT"
echo "start $(date -Is) host $(hostname)"
python3 "$R/scripts/explorer_verification/ev_fetch.py" "$OUT/cases.csv" "$OUT" || { echo "fetch FAILED $(date -Is)"; exit 1; }
python3 "$R/scripts/explorer_verification/ev_judge.py" "$R/notes/explorer_verification/PROTOCOL.md" "$OUT/cards" "$OUT" --model claude-sonnet-5-5 || { echo "judge FAILED $(date -Is)"; exit 1; }
echo "DONE $(date -Is)" | tee "$OUT/DONE"

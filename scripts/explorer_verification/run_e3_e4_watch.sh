#!/usr/bin/env bash
set -u
R=$MEV_ROOT/revision
cd $R && source scripts/env.sh
EV=$R/out/explorer_verification
echo "watch start $(date -Is) host $(hostname)"
for i in $(seq 1 576); do
  if [ -f $EV/SAMPLES_DONE ] && [ ! -f $EV/E3_DONE ]; then
    $MEV_PY scripts/explorer_verification/samples_unseal_score.py > $EV/samples_unseal.log 2>&1 && echo "E3 DONE $(date -Is)" | tee $EV/E3_DONE || echo "E3 FAILED $(date -Is)"
  fi
  if [ ! -f $EV/E4_DONE ]; then
    n=$(wc -l < out/mev_inspect/sweep50.jsonl)
    if ! pgrep -f "run_mev_inspect.py out/mev_inspect/blocks_sweep50" > /dev/null && [ "$n" -ge 49900 ]; then
      $MEV_PY scripts/diag_20261005/arbitrage_cross_check.py > out/diag_20261005/arbitrage_cross_check.log 2>&1 && echo "E4 DONE $(date -Is) lines $n" | tee $EV/E4_DONE || echo "E4 FAILED $(date -Is)"
    elif ! pgrep -f "run_mev_inspect.py out/mev_inspect/blocks_sweep50" > /dev/null; then
      echo "$(date -Is) sweep driver not running and file has $n lines (< 49900): waiting for a manual restart"
    fi
  fi
  if [ -f $EV/E3_DONE ] && [ -f $EV/E4_DONE ]; then echo "watch complete $(date -Is)"; exit 0; fi
  sleep 300
done
echo "watch timed out $(date -Is)"

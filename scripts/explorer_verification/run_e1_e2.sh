#!/usr/bin/env bash
set -u
R=$MEV_ROOT/revision
cd $R && source scripts/env.sh
echo "start $(date -Is) host $(hostname) python $MEV_PY"
test -f out/explorer_verification/f1b/DONE || { echo "F1b not DONE"; exit 1; }
$MEV_PY scripts/explorer_verification/f1b_unseal_score.py > out/explorer_verification/f1b/unseal.log 2>&1 && echo "E1 done $(date -Is)" || echo "E1 FAILED $(date -Is)"
$MEV_PY scripts/diag_20261005/symmetric_arm_contrast.py > out/diag_20261005/symmetric_arm_contrast.log 2>&1 && echo "E2a done $(date -Is)" || echo "E2a FAILED $(date -Is)"
$MEV_PY scripts/diag_20261005/symmetric_arm_magnitudes.py > out/diag_20261005/symmetric_arm_magnitudes.log 2>&1 && echo "E2b done $(date -Is)" || echo "E2b FAILED $(date -Is)"
echo "E1_E2 DONE $(date -Is)" | tee out/explorer_verification/E1_E2_DONE

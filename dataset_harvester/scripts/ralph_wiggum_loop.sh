#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

mkdir -p logs output

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt

PROMPT='이 저장소를 점검해서 데이터셋 추출 성공률을 높여줘. 실패한 extractor를 수정하고, 필요하면 Playwright fallback을 추가하고, harvest.py 실행 후 output/datasets.csv를 갱신해.'

while true; do
  echo "[loop] $(date -Iseconds) running harvest" | tee -a logs/loop.log
  python scripts/harvest.py --targets config/targets.yaml --out output/datasets.csv | tee -a logs/loop.log || true

  if command -v codex >/dev/null 2>&1; then
    echo "[loop] invoking codex" | tee -a logs/loop.log
    codex "$PROMPT" || true
  fi

  if command -v opencode >/dev/null 2>&1; then
    echo "[loop] opencode detected (token auto-compact optional)" | tee -a logs/loop.log
  fi

  sleep 300
done

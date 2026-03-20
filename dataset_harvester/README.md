# Dataset Harvester

URL 리스트에서 데이터셋 목록을 자동 수집해서 `domain,dataset_name,link,source` 형식으로 저장하는 자동화 스캐폴드입니다.

## 목표
- 입력 URL 목록 순회
- 사이트별 수집기 실행
- 결과를 CSV/MD/TXT로 저장
- 실패/재시도/로그 기록
- Codex CLI 루프와 결합 가능
- EzyCopy를 옵션으로 사용해 웹 본문을 markdown으로 정리 가능
- OpenCode는 옵션으로 연동 가능

## 현재 포함된 수집기
- Our World in Data explorers
- Our World in Data all-topics
- FiveThirtyEight index.csv
- Kaggle datasets (페이지 순회 구조 포함)
- Kaggle competitions
- UCI datasets
- OpenML datasets
- AWS Open Data Registry
- World Bank Data360
- WSDM 2026 (dataset/resource link 후보 추출)
- DrivenData completed competitions
- Zindi competitions

## 빠른 실행
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/harvest.py --targets config/targets.yaml --out output/datasets.csv
```

## 완전자동 루프 예시
```bash
bash scripts/ralph_wiggum_loop.sh
```

## Codex CLI 예시
```bash
codex "프로젝트를 스캔하고 실패한 extractor를 자동 수정한 뒤 테스트를 다시 실행해줘"
```

## 출력
- `output/datasets.csv`
- `output/datasets.md`
- `output/datasets.txt`
- `logs/harvest.jsonl`

## 주의
- Kaggle 일부 페이지는 로그인/동적 렌더링이 필요할 수 있어 Playwright fallback 사용을 권장합니다.
- robots.txt, 이용약관, rate limit을 준수하세요.

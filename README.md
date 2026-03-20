# Dataset Harvester

Phase 1 collects dataset list pages into `domain,dataset_name,link,source` CSV outputs.

The project now uses source-specific adapters instead of generic link scraping:

- Our World in Data explorers and topic lists
- FiveThirtyEight `index.csv`
- Kaggle datasets via the authenticated Kaggle API/CLI path by default
- UCI dataset cards
- OpenML dataset API
- AWS Open Data Registry metadata from the registry source repo
- World Bank Data360 search API

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/harvest.py --targets config/targets.yaml --out output/datasets_by_source.csv
```

On Windows Git Bash, the same commands work after activating `.venv/Scripts/activate`.

## Kaggle authentication

The default Kaggle path is authenticated. Set either:

```bash
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_key
```

or create `~/.kaggle/kaggle.json`.

If Kaggle credentials are missing, the harvester logs a target error and exits non-zero unless you pass `--allow-partial`.

## Outputs

- `output/datasets_by_source.csv`
- `output/datasets_by_domain.csv`
- `logs/harvest.jsonl`

`domain` is now a fixed label from:

- `public`
- `ml`
- `finance`
- `health`
- `environment`
- `text`
- `vision`
- `timeseries`
- `social`
- `competition`
- `others`

## Notes

- Kaggle is intentionally not scraped from raw HTML.
- Dataset names are normalized to ASCII-safe text so odd symbols and broken emoji-style characters do not leak into the CSV.
- Respect each source's terms, robots guidance, and rate limits.

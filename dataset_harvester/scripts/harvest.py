from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

import httpx
import pandas as pd
import trafilatura
import yaml
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; DatasetHarvester/0.1; +https://example.local)"
}


@dataclass
class Row:
    domain: str
    dataset_name: str
    link: str
    source: str


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
def fetch(url: str) -> str:
    with httpx.Client(headers=HEADERS, timeout=30.0, follow_redirects=True) as client:
        r = client.get(url)
        r.raise_for_status()
        return r.text


def domain_of(url: str) -> str:
    return urlparse(url).netloc.replace("www.", "")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def dedupe(rows: Iterable[Row]) -> list[Row]:
    seen = set()
    out: list[Row] = []
    for r in rows:
        key = (r.domain, r.dataset_name.lower(), r.link, r.source.lower())
        if key not in seen and r.dataset_name and r.link:
            seen.add(key)
            out.append(r)
    return out


def extract_links_generic(url: str, source: str) -> list[Row]:
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select("a[href]"):
        href = urljoin(url, a.get("href", ""))
        text = clean(a.get_text(" "))
        if len(text) >= 3 and href.startswith("http"):
            rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_owid_explorers(url: str, source: str) -> list[Row]:
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select('a[href*="/explorers/"]'):
        href = urljoin(url, a.get("href", ""))
        text = clean(a.get_text(" "))
        if text:
            rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_fivethirtyeight_csv(url: str, source: str) -> list[Row]:
    with httpx.Client(headers=HEADERS, timeout=30.0, follow_redirects=True) as client:
        r = client.get(url)
        r.raise_for_status()
        lines = r.text.splitlines()
    reader = csv.DictReader(lines)
    rows: list[Row] = []
    for item in reader:
        name = clean(item.get("dataset") or item.get("title") or item.get("file") or "")
        link = item.get("url") or item.get("source") or item.get("repo") or "https://github.com/fivethirtyeight/data"
        rows.append(Row(domain_of(link), name, link, source))
    return dedupe(rows)


def extract_kaggle_datasets(base_url: str, source: str, pages: int = 1) -> list[Row]:
    rows: list[Row] = []
    for page in range(1, pages + 1):
        url = f"{base_url}&page={page}" if "?" in base_url else f"{base_url}?page={page}"
        try:
            html = fetch(url)
        except Exception:
            continue
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.select('a[href^="/datasets/"]'):
            href = urljoin("https://www.kaggle.com", a.get("href", ""))
            text = clean(a.get_text(" "))
            if text:
                rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_kaggle_competitions(base_url: str, source: str, pages: int = 1) -> list[Row]:
    rows: list[Row] = []
    for page in range(1, pages + 1):
        url = re.sub(r"page=\d+", f"page={page}", base_url)
        html = fetch(url)
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.select('a[href^="/competitions/"]'):
            href = urljoin("https://www.kaggle.com", a.get("href", ""))
            text = clean(a.get_text(" "))
            if text and text.lower() not in {"competitions", "overview"}:
                rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_uci(url: str, source: str) -> list[Row]:
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select('a[href*="/dataset/"]'):
        href = urljoin(url, a.get("href", ""))
        text = clean(a.get_text(" "))
        if text:
            rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_openml(url: str, source: str) -> list[Row]:
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select('a[href*="/search?"] , a[href*="/d/"]'):
        href = urljoin(url, a.get("href", ""))
        text = clean(a.get_text(" "))
        if text and ("dataset" in href or "/d/" in href):
            rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_aws_registry(url: str, source: str) -> list[Row]:
    html = fetch(url)
    text = trafilatura.extract(html) or html
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select('a[href]'):
        href = urljoin(url, a.get("href", ""))
        label = clean(a.get_text(" "))
        if href.startswith("http") and label and label.lower() not in {"learn more", "home"}:
            rows.append(Row(domain_of(href), label, href, source))
    if not rows:
        for line in text.splitlines():
            line = clean(line)
            if 5 <= len(line) <= 120:
                rows.append(Row(domain_of(url), line, url, source))
    return dedupe(rows)


def extract_worldbank(url: str, source: str) -> list[Row]:
    return extract_links_generic(url, source)


def extract_drivendata(url: str, source: str) -> list[Row]:
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select('a[href*="/competitions/"]'):
        href = urljoin(url, a.get("href", ""))
        text = clean(a.get_text(" "))
        if text:
            rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


def extract_zindi(url: str, source: str) -> list[Row]:
    return extract_links_generic(url, source)


def extract_wsdm(url: str, source: str) -> list[Row]:
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for a in soup.select('a[href]'):
        href = urljoin(url, a.get("href", ""))
        text = clean(a.get_text(" "))
        if not text:
            continue
        if any(k in text.lower() for k in ["dataset", "data", "challenge", "track", "benchmark"]):
            rows.append(Row(domain_of(href), text, href, source))
    return dedupe(rows)


EXTRACTORS = {
    "owid_explorers": extract_owid_explorers,
    "owid_topics": extract_links_generic,
    "csv_index": extract_fivethirtyeight_csv,
    "kaggle_datasets": extract_kaggle_datasets,
    "kaggle_competitions": extract_kaggle_competitions,
    "uci_datasets": extract_uci,
    "openml_datasets": extract_openml,
    "aws_registry": extract_aws_registry,
    "worldbank_data360": extract_worldbank,
    "conference_links": extract_wsdm,
    "drivendata_competitions": extract_drivendata,
    "zindi_competitions": extract_zindi,
}


def save_all(rows: list[Row], out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([asdict(r) for r in rows])
    df = df.drop_duplicates().sort_values(["source", "dataset_name", "link"])
    df.to_csv(out_csv, index=False)

    md_path = out_csv.with_suffix(".md")
    with md_path.open("w", encoding="utf-8") as f:
        f.write("| domain | dataset_name | link | source |\n")
        f.write("|---|---|---|---|\n")
        for r in df.to_dict(orient="records"):
            f.write(f"| {r['domain']} | {r['dataset_name'].replace('|','/')} | {r['link']} | {r['source']} |\n")

    txt_path = out_csv.with_suffix(".txt")
    with txt_path.open("w", encoding="utf-8") as f:
        for r in df.to_dict(orient="records"):
            f.write(f"{r['domain']}\t{r['dataset_name']}\t{r['link']}\t{r['source']}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--targets", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    config = yaml.safe_load(Path(args.targets).read_text(encoding="utf-8"))
    rows: list[Row] = []
    log_path = Path("logs/harvest.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    for target in config["targets"]:
        kind = target["kind"]
        extractor = EXTRACTORS[kind]
        try:
            if "pages" in target:
                found = extractor(target["url"], target["source"], target["pages"])
            else:
                found = extractor(target["url"], target["source"])
            rows.extend(found)
            event = {"status": "ok", "target": target, "count": len(found)}
        except Exception as e:
            event = {"status": "error", "target": target, "error": str(e)}
        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

    rows = dedupe(rows)
    save_all(rows, Path(args.out))
    print(f"saved {len(rows)} rows -> {args.out}")


if __name__ == "__main__":
    main()

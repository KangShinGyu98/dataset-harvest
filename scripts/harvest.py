from __future__ import annotations

import argparse
import csv
import html
import io
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlencode, urljoin, urlparse, urlunparse

import httpx
import yaml
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; DatasetHarvester/1.0; +https://example.local)",
    "Accept": "text/html,application/json,text/plain;q=0.9,*/*;q=0.8",
}

WORLD_BANK_HEADERS = {
    "Content-Type": "application/json",
    "Origin": "https://data360.worldbank.org",
    "Referer": "https://data360.worldbank.org/en/search",
    "User-Agent": HEADERS["User-Agent"],
}

ROOT = Path(__file__).resolve().parents[1]
DOMAIN_OVERRIDES_PATH = ROOT / "config" / "domain_overrides.csv"
ALLOWED_DOMAINS = {
    "public",
    "ml",
    "finance",
    "health",
    "environment",
    "text",
    "vision",
    "timeseries",
    "social",
    "competition",
    "others",
}
SOURCE_DEFAULT_DOMAINS = {
    "aws_open_data": "public",
    "fivethirtyeight": "social",
    "openml": "ml",
    "ourworldindata": "public",
    "uci": "ml",
    "worldbank": "public",
}
CHAR_TRANSLATION = str.maketrans(
    {
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        "―": "-",
        "−": "-",
        "…": "...",
        "•": " ",
        "·": " ",
        "&": " and ",
        "₂": "2",
        "₃": "3",
        "₄": "4",
        "₅": "5",
        "₆": "6",
        "₇": "7",
        "₈": "8",
        "₉": "9",
        "₀": "0",
    }
)
CONTROL_CHAR_RE = re.compile(r"[\x00-\x1f\x7f-\x9f]")
NOISY_NAME_RE = re.compile(r"[^A-Za-z0-9&@#%+/\'\"(),.:;!?\[\]_-]+")
SPACE_RE = re.compile(r"\s+")
PUNCT_SPACING_RE = re.compile(r"\s+([),.:;!?\]])")
OPEN_PUNCT_SPACING_RE = re.compile(r"([(/\[])(\s+)")
EMPTY_PARENS_RE = re.compile(r"\(\s*\)")
CAMEL_CASE_RE = re.compile(r"(?<=[a-z])(?=[A-Z][a-z])")
TOKEN_NORMALIZE_RE = re.compile(r"[^a-z0-9]+")
DOMAIN_KEYWORDS = {
    "competition": (
        "challenge",
        "competition",
        "benchmark",
        "contest",
        "cup",
        "hackathon",
        "leaderboard",
        "prize",
    ),
    "health": (
        "health",
        "medical",
        "medicine",
        "clinical",
        "patient",
        "hospital",
        "disease",
        "cancer",
        "covid",
        "diabetes",
        "heart",
        "alzheimer",
        "parkinson",
        "genome",
        "genomic",
        "protein",
        "dna",
        "rna",
        "brain",
        "icu",
        "sleep",
        "neuro",
        "pathology",
        "biomedical",
        "bioinformatics",
        "microbiome",
        "ehr",
        "ecg",
        "mimic",
        "mortality",
    ),
    "finance": (
        "finance",
        "financial",
        "bank",
        "banking",
        "loan",
        "credit",
        "stock",
        "trading",
        "transaction",
        "fraud",
        "insurance",
        "forex",
        "bitcoin",
        "crypto",
        "payment",
        "invoice",
    ),
    "environment": (
        "climate",
        "weather",
        "temperature",
        "rain",
        "precipitation",
        "flood",
        "drought",
        "pollution",
        "air quality",
        "water",
        "ocean",
        "forest",
        "biodiversity",
        "wildlife",
        "earth",
        "satellite",
        "land use",
        "land cover",
        "crop",
        "soil",
        "agric",
        "energy",
        "solar",
        "wind",
        "co2",
        "emission",
        "ecosystem",
        "geospatial",
        "remote sensing",
        "glacier",
        "storm",
        "hurricane",
        "sea",
        "fish",
        "wildfire",
        "fire",
        "earthquake",
        "disaster",
        "infrared",
        "galaxy",
        "astronomy",
        "astrophysics",
        "telescope",
        "space",
        "planetary",
        "sentinel",
        "landsat",
        "nasa",
        "noaa",
        "meteorolog",
    ),
    "text": (
        "text",
        "corpus",
        "nlp",
        "language",
        "essay",
        "review",
        "tweet",
        "twitter",
        "question answering",
        "qa",
        "dialog",
        "chat",
        "transcript",
        "summarization",
        "sentiment",
        "document",
        "caption",
        "translation",
        "spam",
        "email",
        "news",
        "citation",
        "entity linking",
        "llm",
        "prompt",
        "speech recognition",
    ),
    "vision": (
        "image",
        "video",
        "vision",
        "segmentation",
        "detection",
        "object",
        "face",
        "facial",
        "photo",
        "picture",
        "camera",
        "microscopy",
        "x-ray",
        "xray",
        "mri",
        "ct scan",
        "ultrasound",
        "lidar",
        "radar",
        "imagery",
        "scene",
        "visual",
    ),
    "timeseries": (
        "time series",
        "timeseries",
        "forecast",
        "forecasting",
        "temporal",
        "sequence",
        "sensor",
        "telemetry",
        "hourly",
        "daily",
        "monthly",
        "yearly",
        "signal",
        "load diagrams",
        "stream",
    ),
    "social": (
        "social",
        "survey",
        "population",
        "demograph",
        "election",
        "voter",
        "politic",
        "education",
        "employment",
        "crime",
        "housing",
        "migration",
        "gender",
        "income",
        "happiness",
        "wellbeing",
        "student",
        "customer",
        "consumer",
        "behavior",
        "behaviour",
        "public opinion",
        "census",
        "religion",
        "marriage",
        "poverty",
        "inequality",
        "labor",
    ),
    "ml": (
        "machine learning",
        "classification",
        "regression",
        "clustering",
        "tabular",
        "synthetic",
        "anomaly",
        "recommender",
        "recommendation",
        "predictive maintenance",
        "intrusion detection",
        "openml",
        "uci",
    ),
    "public": (
        "public use",
        "government",
        "registry",
        "official",
        "administrative",
        "open data",
        "open government",
        "indicator",
        "statistics",
        "bureau",
        "ministry",
    ),
}


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


@dataclass(frozen=True)
class Row:
    domain: str
    dataset_name: str
    link: str
    source: str


@dataclass
class TargetEvent:
    source: str
    kind: str
    url: str
    status: str
    count: int = 0
    error: str | None = None


def clean(text: str | None) -> str:
    return SPACE_RE.sub(" ", text or "").strip()


def sanitize_dataset_name(text: str | None) -> str:
    value = html.unescape(text or "")
    value = CAMEL_CASE_RE.sub(" ", value)
    value = value.translate(CHAR_TRANSLATION)
    value = unicodedata.normalize("NFKD", value)
    value = CONTROL_CHAR_RE.sub(" ", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = NOISY_NAME_RE.sub(" ", value)
    value = PUNCT_SPACING_RE.sub(r"\1", value)
    value = OPEN_PUNCT_SPACING_RE.sub(r"\1", value)
    value = EMPTY_PARENS_RE.sub("", value)
    value = SPACE_RE.sub(" ", value).strip(" -_/|,.;:")
    return value


def slug_to_title(value: str) -> str:
    return sanitize_dataset_name(value.replace("-", " ").replace("_", " "))


def update_query(url: str, **updates: Any) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query, keep_blank_values=True)
    for key, value in updates.items():
        query[key] = [str(value)]
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def dedupe(rows: list[Row]) -> list[Row]:
    seen: set[tuple[str, str, str]] = set()
    out: list[Row] = []
    for row in rows:
        if not row.dataset_name or not row.link:
            continue
        key = (row.dataset_name.lower(), row.link, row.source.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def load_domain_overrides(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        overrides: dict[str, str] = {}
        for item in reader:
            link = clean(item.get("link"))
            domain = clean(item.get("domain")).lower()
            if link and domain in ALLOWED_DOMAINS:
                overrides[link.rstrip("/")] = domain
        return overrides


DOMAIN_OVERRIDES = load_domain_overrides(DOMAIN_OVERRIDES_PATH)


def contains_any(text: str, keywords: tuple[str, ...]) -> bool:
    normalized_text = f" {TOKEN_NORMALIZE_RE.sub(' ', text.lower()).strip()} "
    for keyword in keywords:
        normalized_keyword = TOKEN_NORMALIZE_RE.sub(" ", keyword.lower()).strip()
        if normalized_keyword and f" {normalized_keyword} " in normalized_text:
            return True
    return False


def classify_domain(source: str, dataset_name: str, link: str) -> str:
    override = DOMAIN_OVERRIDES.get(link.rstrip("/"))
    if override:
        return override

    source_key = clean(source).lower()
    text = f"{dataset_name.lower()} {link.lower()}"

    if source_key in {"drivendata", "zindi"}:
        return "competition"

    if source_key == "fivethirtyeight" and contains_any(
        text,
        (
            "nba",
            "nfl",
            "nhl",
            "mlb",
            "world cup",
            "march madness",
            "fifa",
            "tennis",
            "baseball",
            "basketball",
            "hockey",
            "football",
            "fight songs",
            "bachelorette",
            "avengers",
            "tarantino",
            "classic rock",
            "bob ross",
            "star wars",
            "love actually",
        ),
    ):
        return "others"

    if contains_any(text, DOMAIN_KEYWORDS["competition"]):
        return "competition"
    if contains_any(text, DOMAIN_KEYWORDS["health"]):
        return "health"
    if contains_any(text, DOMAIN_KEYWORDS["finance"]):
        return "finance"
    if contains_any(text, DOMAIN_KEYWORDS["environment"]):
        return "environment"
    if contains_any(text, DOMAIN_KEYWORDS["text"]):
        return "text"
    if contains_any(text, DOMAIN_KEYWORDS["vision"]):
        return "vision"
    if contains_any(text, DOMAIN_KEYWORDS["timeseries"]):
        return "timeseries"
    if contains_any(text, DOMAIN_KEYWORDS["social"]):
        return "social"
    if contains_any(text, DOMAIN_KEYWORDS["ml"]):
        return "ml"
    if contains_any(text, DOMAIN_KEYWORDS["public"]):
        return "public"

    return SOURCE_DEFAULT_DOMAINS.get(source_key, "others")


class Harvester:
    def __init__(self) -> None:
        self.client = httpx.Client(headers=HEADERS, timeout=60.0, follow_redirects=True)

    def close(self) -> None:
        self.client.close()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
    def fetch_text(self, url: str, headers: dict[str, str] | None = None) -> str:
        response = self.client.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
    def fetch_bytes(self, url: str, headers: dict[str, str] | None = None) -> bytes:
        response = self.client.get(url, headers=headers)
        response.raise_for_status()
        return response.content

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
    def fetch_json(
        self,
        url: str,
        *,
        method: str = "GET",
        payload: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        response = self.client.request(method, url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()


def row(source: str, name: str, link: str) -> Row:
    normalized_source = clean(source)
    normalized_link = clean(link)
    normalized_name = sanitize_dataset_name(name)
    return Row(
        domain=classify_domain(normalized_source, normalized_name, normalized_link),
        dataset_name=normalized_name,
        link=normalized_link,
        source=normalized_source,
    )


def extract_owid_explorers(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    html = harvester.fetch_text(target["url"])
    soup = BeautifulSoup(html, "html.parser")
    rows: list[Row] = []
    for anchor in soup.select('a[href*="/explorers/"]'):
        href = urljoin(target["url"], anchor.get("href", ""))
        text = clean(anchor.get_text(" "))
        if text and "/explorers/" in href:
            rows.append(row(target["source"], text, href))
    return dedupe(rows)


def extract_owid_topics(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    html = harvester.fetch_text(target["url"])
    soup = BeautifulSoup(html, "html.parser")
    start = soup.find(id="all-topics")
    if start is None:
        for heading in soup.find_all(re.compile(r"^h[1-6]$")):
            if clean(heading.get_text(" ")).lower() == "all our topics":
                start = heading
                break

    anchors: list[Any] = []
    if start is not None:
        node = start
        for _ in range(150):
            node = node.find_next()
            if node is None:
                break
            if getattr(node, "name", None) and re.fullmatch(r"h[1-6]", node.name):
                text = clean(node.get_text(" ")).lower()
                if text.startswith("our world in data is free"):
                    break
            if getattr(node, "name", None) == "a":
                anchors.append(node)

    excluded = {
        "about",
        "data",
        "latest",
        "search",
        "donate",
        "subscribe",
        "privacy-policy",
        "licensing",
        "charts",
        "grapher",
    }

    rows: list[Row] = []
    for anchor in anchors:
        href = urljoin(target["url"], anchor.get("href", ""))
        parsed = urlparse(href)
        parts = [part for part in parsed.path.split("/") if part]
        if parsed.netloc != "ourworldindata.org":
            continue
        if len(parts) != 1:
            continue
        if parts[0] in excluded:
            continue
        text = clean(anchor.get_text(" ")) or slug_to_title(parts[0])
        rows.append(row(target["source"], text, href))
    return dedupe(rows)


def extract_fivethirtyeight_csv(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    text = harvester.fetch_text(target["url"])
    reader = csv.DictReader(io.StringIO(text))
    rows: list[Row] = []
    for item in reader:
        link = clean(item.get("dataset_url"))
        name = clean(item.get("subfolder_name"))
        if link and name:
            rows.append(row(target["source"], name, link))
    return dedupe(rows)


def kaggle_credentials_available() -> bool:
    if os.getenv("KAGGLE_USERNAME") and os.getenv("KAGGLE_KEY"):
        return True
    return (Path.home() / ".kaggle" / "kaggle.json").exists()


def parse_csv_output(output: str) -> list[dict[str, str]]:
    lines = [line for line in output.splitlines() if line.strip()]
    start = 0
    for index, line in enumerate(lines):
        if line.startswith("ref,") or line.startswith("title,"):
            start = index
            break
    reader = csv.DictReader(io.StringIO("\n".join(lines[start:])))
    return [dict(item) for item in reader]


def kaggle_cli_command() -> str:
    scripts_dir = Path(sys.executable).resolve().parent
    for candidate in (scripts_dir / "kaggle.exe", scripts_dir / "kaggle"):
        if candidate.exists():
            return str(candidate)
    resolved = shutil.which("kaggle")
    if resolved:
        return resolved
    raise RuntimeError("Kaggle CLI is not available in the current environment.")


def extract_kaggle_datasets(_harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    if not kaggle_credentials_available():
        raise RuntimeError(
            "Kaggle credentials are required for the default authenticated extractor path. "
            "Set KAGGLE_USERNAME and KAGGLE_KEY or add ~/.kaggle/kaggle.json."
        )

    pages = int(os.getenv("HARVEST_KAGGLE_PAGES") or target.get("pages", 1))
    sort_by = clean(target.get("sort_by") or "votes")
    rows: list[Row] = []

    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    try:
        api.authenticate()
    except BaseException:
        api = None

    for page_number in range(1, pages + 1):
        try:
            if api is not None:
                items = api.dataset_list(sort_by=sort_by, page=page_number)
                for item in items:
                    ref = clean(getattr(item, "ref", ""))
                    title = clean(getattr(item, "title", "")) or slug_to_title(ref.split("/")[-1])
                    if ref:
                        rows.append(row(target["source"], title, f"https://www.kaggle.com/datasets/{ref}"))
                continue
        except Exception:
            pass

        kaggle_cli = kaggle_cli_command()
        command = [kaggle_cli, "datasets", "list", "--sort-by", sort_by, "-p", str(page_number), "-v"]
        completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
        if completed.returncode != 0:
            stderr = clean(completed.stderr or completed.stdout)
            raise RuntimeError(f"Kaggle API/CLI failed on page {page_number}: {stderr}")

        for item in parse_csv_output(completed.stdout):
            ref = clean(item.get("ref"))
            title = clean(item.get("title")) or slug_to_title(ref.split("/")[-1])
            if ref:
                rows.append(row(target["source"], title, f"https://www.kaggle.com/datasets/{ref}"))

    return dedupe(rows)


def extract_uci(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    pages = int(target.get("pages", 1))
    base_url = target["url"]
    query = parse_qs(urlparse(base_url).query)
    initial_skip = int(query.get("skip", [0])[0])
    take = int(query.get("take", [25])[0])
    rows: list[Row] = []

    for page_number in range(pages):
        page_url = update_query(base_url, skip=initial_skip + (page_number * take), take=take)
        html = harvester.fetch_text(page_url)
        soup = BeautifulSoup(html, "html.parser")
        for anchor in soup.select('a[href^="/dataset/"]'):
            href = urljoin(base_url, anchor.get("href", ""))
            text = clean(anchor.get_text(" "))
            if text:
                rows.append(row(target["source"], text, href))
    return dedupe(rows)


def extract_openml(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    pages = int(target.get("pages", 1))
    page_size = int(target.get("page_size", 100))
    status = clean(target.get("status") or "active")
    rows: list[Row] = []

    for page_number in range(pages):
        offset = page_number * page_size
        api_url = (
            f"https://www.openml.org/api/v1/json/data/list/status/{status}"
            f"/limit/{page_size}/offset/{offset}"
        )
        data = harvester.fetch_json(api_url)
        datasets = data.get("data", {}).get("dataset", [])
        if isinstance(datasets, dict):
            datasets = [datasets]
        for item in datasets:
            did = clean(str(item.get("did", "")))
            name = clean(item.get("name"))
            if did and name:
                rows.append(row(target["source"], name, f"https://www.openml.org/d/{did}"))
    return dedupe(rows)


def extract_aws_registry(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    include_deprecated = bool(target.get("include_deprecated", False))
    archive = harvester.fetch_bytes("https://codeload.github.com/awslabs/open-data-registry/zip/refs/heads/main")
    rows: list[Row] = []

    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        names = [name for name in bundle.namelist() if "/datasets/" in name and name.endswith(('.yaml', '.yml'))]
        for name in sorted(names):
            payload = yaml.safe_load(bundle.read(name).decode("utf-8")) or {}
            if payload.get("Deprecated") and not include_deprecated:
                continue
            dataset_name = clean(payload.get("Name")) or slug_to_title(Path(name).stem)
            slug = Path(name).stem
            link = urljoin(target["url"], f"{slug}/")
            rows.append(row(target["source"], dataset_name, link))

    return dedupe(rows)


def extract_worldbank(harvester: Harvester, target: dict[str, Any]) -> list[Row]:
    pages = int(target.get("pages", 1))
    page_size = int(target.get("page_size", 100))
    rows: list[Row] = []

    for page_number in range(pages):
        payload = {
            "top": page_size,
            "skip": page_number * page_size,
            "filter": "type eq 'dataset'",
        }
        data = harvester.fetch_json(
            "https://data360api.worldbank.org/data360/searchv2",
            method="POST",
            payload=payload,
            headers=WORLD_BANK_HEADERS,
        )
        for item in data.get("value", []):
            series = item.get("series_description") or {}
            metadata = item.get("metadata_information") or {}
            dataset_id = clean(series.get("database_id") or item.get("id"))
            dataset_name = clean(series.get("name") or metadata.get("title") or dataset_id)
            if not dataset_name:
                continue
            if dataset_id:
                link = f"https://data360.worldbank.org/en/dataset/{dataset_id}"
            else:
                link = clean(series.get("json_link") or series.get("api_link") or target["url"])
            rows.append(row(target["source"], dataset_name, link))
    return dedupe(rows)


EXTRACTORS = {
    "owid_explorers": extract_owid_explorers,
    "owid_topics": extract_owid_topics,
    "csv_index": extract_fivethirtyeight_csv,
    "kaggle_datasets": extract_kaggle_datasets,
    "uci_datasets": extract_uci,
    "openml_datasets": extract_openml,
    "aws_registry": extract_aws_registry,
    "worldbank_data360": extract_worldbank,
}


def save_rows(rows: list[Row], out_csv: Path) -> None:
    def domain_output_path(source_output: Path) -> Path:
        if source_output.stem.endswith("_by_source"):
            return source_output.with_name(source_output.name.replace("_by_source", "_by_domain"))
        return source_output.with_name(f"{source_output.stem}_by_domain{source_output.suffix}")

    def cleanup_output_dir(out_dir: Path, keep: set[str]) -> None:
        out_dir.mkdir(parents=True, exist_ok=True)
        for child in out_dir.iterdir():
            if child.is_file() and child.name not in keep:
                try:
                    child.unlink()
                except PermissionError:
                    continue

    def write_csv(path: Path, ordered_rows: list[Row]) -> None:
        fields = ["domain", "dataset_name", "link", "source"]
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for item in ordered_rows:
                writer.writerow(asdict(item))

    source_csv = out_csv
    domain_csv = domain_output_path(source_csv)
    rows = dedupe(rows)
    cleanup_output_dir(source_csv.parent, {source_csv.name, domain_csv.name})

    source_rows = sorted(rows, key=lambda item: (item.source, item.dataset_name.lower(), item.link))
    domain_rows = sorted(rows, key=lambda item: (item.domain, item.source, item.dataset_name.lower(), item.link))

    write_csv(source_csv, source_rows)
    write_csv(domain_csv, domain_rows)

    print(f"saved {len(rows)} rows -> {source_csv}")
    print(f"saved {len(rows)} rows -> {domain_csv}")


def append_log(log_path: Path, event: TargetEvent) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(asdict(event), ensure_ascii=False) + "\n")


def run(targets_path: Path, out_csv: Path) -> tuple[list[Row], list[TargetEvent]]:
    config = yaml.safe_load(targets_path.read_text(encoding="utf-8")) or {}
    targets = config.get("targets", [])
    all_rows: list[Row] = []
    events: list[TargetEvent] = []
    log_path = Path("logs/harvest.jsonl")
    harvester = Harvester()

    try:
        for target in targets:
            if not target.get("enabled", True):
                continue
            kind = clean(target.get("kind"))
            extractor = EXTRACTORS.get(kind)
            if extractor is None:
                event = TargetEvent(
                    source=clean(target.get("source") or kind),
                    kind=kind,
                    url=clean(target.get("url")),
                    status="error",
                    error=f"Unknown extractor kind: {kind}",
                )
                events.append(event)
                append_log(log_path, event)
                continue

            try:
                rows = extractor(harvester, target)
                all_rows.extend(rows)
                event = TargetEvent(
                    source=clean(target.get("source") or kind),
                    kind=kind,
                    url=clean(target.get("url")),
                    status="ok",
                    count=len(rows),
                )
            except Exception as exc:
                event = TargetEvent(
                    source=clean(target.get("source") or kind),
                    kind=kind,
                    url=clean(target.get("url")),
                    status="error",
                    error=clean(str(exc)),
                )

            events.append(event)
            append_log(log_path, event)
    finally:
        harvester.close()

    rows = dedupe(all_rows)
    save_rows(rows, out_csv)
    return rows, events


def main() -> int:
    load_env_file(Path(__file__).resolve().parents[1] / ".env")

    parser = argparse.ArgumentParser(description="Harvest dataset list pages into source/domain CSV outputs.")
    parser.add_argument("--targets", required=True, help="Path to YAML target config")
    parser.add_argument("--out", required=True, help="Output CSV path")
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Exit with status 0 even if one or more targets fail",
    )
    args = parser.parse_args()

    rows, events = run(Path(args.targets), Path(args.out))
    error_count = sum(1 for event in events if event.status == "error")
    if error_count:
        print(f"target errors: {error_count}")
    return 0 if args.allow_partial or error_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

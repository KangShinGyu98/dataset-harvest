"""
Reads output/datasets_by_domain.csv and replaces the '## 결과물-Domain별'
section in README.md with full markdown tables grouped by domain.
"""

import csv
import pathlib
from collections import defaultdict

ROOT = pathlib.Path(__file__).parent.parent
CSV_PATH = ROOT / "output" / "datasets_by_domain.csv"
README_PATH = ROOT / "README.md"
SECTION_HEADER = "## 결과물-Domain별"


def load_csv(path: pathlib.Path) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            groups[row["domain"]].append(row)
    return groups


def build_tables(groups: dict[str, list[dict]]) -> str:
    lines = [SECTION_HEADER, ""]
    for domain, rows in sorted(groups.items(), key=lambda x: -len(x[1])):
        lines.append(f"### {domain} (총 {len(rows)}개)")
        lines.append("")
        lines.append("| dataset_name | source | link |")
        lines.append("|---|---|---|")
        for row in rows:
            name = row["dataset_name"].replace("|", "\\|")
            source = row["source"].replace("|", "\\|")
            link = row["link"].strip()
            lines.append(f"| {name} | {source} | [바로가기]({link}) |")
        lines.append("")
    return "\n".join(lines)


def update_readme(tables: str) -> None:
    text = README_PATH.read_text(encoding="utf-8")
    idx = text.find(SECTION_HEADER)
    if idx == -1:
        text = text.rstrip("\n") + "\n\n" + tables + "\n"
    else:
        text = text[:idx] + tables + "\n"
    README_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    groups = load_csv(CSV_PATH)
    tables = build_tables(groups)
    update_readme(tables)
    total = sum(len(v) for v in groups.values())
    print(f"Done. {len(groups)} domains, {total} rows written to README.md")

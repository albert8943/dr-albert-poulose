#!/usr/bin/env python3
"""Fetch citation metrics from OpenAlex by ORCID and write data/metrics.yaml."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ORCID = "0000-0002-6138-7857"
MAILTO = "albertpoulosepalatty@knu.ac.kr"
API_URL = f"https://api.openalex.org/authors/orcid:{ORCID}?mailto={MAILTO}"
ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "data" / "metrics.yaml"


def fetch_author() -> dict:
    req = urllib.request.Request(
        API_URL,
        headers={"User-Agent": f"albertpoulose.com-metrics/1.0 (mailto:{MAILTO})"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def citations_by_year_series(author: dict) -> list[tuple[int, int]]:
    raw = author.get("counts_by_year") or []
    by_year: dict[int, int] = {}
    for row in raw:
        try:
            year = int(row.get("year"))
            cited = int(row.get("cited_by_count") or 0)
        except (TypeError, ValueError):
            continue
        by_year[year] = cited
    if not by_year:
        return []
    start = min(by_year)
    end = date.today().year
    return [(year, by_year.get(year, 0)) for year in range(start, end + 1)]


def write_metrics(author: dict) -> None:
    stats = author.get("summary_stats") or {}
    openalex_id = (author.get("id") or "").rstrip("/").split("/")[-1]
    series = citations_by_year_series(author)
    lines = [
        "source: OpenAlex",
        f'orcid: "{ORCID}"',
        f'openalex_id: "{openalex_id}"',
        f"citations: {int(author.get('cited_by_count') or 0)}",
        f"h_index: {int(stats.get('h_index') or 0)}",
        f"i10_index: {int(stats.get('i10_index') or 0)}",
        f"works_count: {int(author.get('works_count') or 0)}",
        f'updated: "{date.today().isoformat()}"',
        "citations_by_year:",
    ]
    if series:
        for year, citations in series:
            lines.append(f"  - year: {year}")
            lines.append(f"    citations: {citations}")
    else:
        lines.append("  []")
    lines.append("")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        author = fetch_author()
        write_metrics(author)
        print(f"Wrote {OUT_PATH}")
        return 0
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, KeyError, TypeError) as exc:
        print(f"OpenAlex metrics fetch failed; keeping existing file. Error: {exc}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())

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


def write_metrics(author: dict) -> None:
    stats = author.get("summary_stats") or {}
    openalex_id = (author.get("id") or "").rstrip("/").split("/")[-1]
    lines = [
        "source: OpenAlex",
        f'orcid: "{ORCID}"',
        f'openalex_id: "{openalex_id}"',
        f"citations: {int(author.get('cited_by_count') or 0)}",
        f"h_index: {int(stats.get('h_index') or 0)}",
        f"i10_index: {int(stats.get('i10_index') or 0)}",
        f"works_count: {int(author.get('works_count') or 0)}",
        f'updated: "{date.today().isoformat()}"',
        "",
    ]
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

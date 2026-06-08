from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from typing import Iterable

import arxiv


def parse_keywords(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [item.strip().lower() for item in raw.split(",") if item.strip()]


def ensure_list(values: Iterable[str] | None) -> list[str]:
    return list(values or [])


def paper_matches_keywords(paper: dict, keywords: list[str]) -> bool:
    if not keywords:
        return True
    haystack = " ".join(
        [
            paper.get("title", ""),
            paper.get("abstract", ""),
            " ".join(paper.get("categories", [])),
        ]
    ).lower()
    return any(keyword in haystack for keyword in keywords)


def fetch_arxiv_papers(
    categories: list[str],
    days: int,
    keywords: list[str],
    max_results_per_category: int,
) -> list[dict]:
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=days)
    end = now + timedelta(days=1)
    start_token = start.strftime("%Y%m%d")
    end_token = end.strftime("%Y%m%d")

    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=3)
    papers_by_id: dict[str, dict] = {}

    for category in categories:
        search = arxiv.Search(
            query=f"cat:{category} AND submittedDate:[{start_token}0000 TO {end_token}0000]",
            sort_by=arxiv.SortCriterion.LastUpdatedDate,
            sort_order=arxiv.SortOrder.Descending,
            max_results=max_results_per_category,
        )

        for result in client.results(search):
            paper = {
                "id": result.entry_id,
                "title": result.title,
                "link": result.entry_id,
                "pdf_url": result.pdf_url,
                "abstract": result.summary,
                "authors": [author.name for author in result.authors],
                "categories": result.categories,
                "primary_category": result.primary_category,
                "published": result.published.strftime("%Y-%m-%d"),
                "updated": result.updated.strftime("%Y-%m-%d"),
            }
            if paper_matches_keywords(paper, keywords):
                papers_by_id[paper["id"]] = paper

    return sorted(papers_by_id.values(), key=lambda item: item.get("updated", ""), reverse=True)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fetch recent arXiv paper metadata for an AI paper-radar skill."
    )
    parser.add_argument(
        "--categories",
        nargs="+",
        default=["cs.DC", "cs.OS"],
        help="arXiv categories to search, e.g. cs.DC cs.OS",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=2,
        help="Number of days to look back from now.",
    )
    parser.add_argument(
        "--keywords",
        default="",
        help="Comma-separated local prefilter keywords. Leave empty to keep all fetched papers.",
    )
    parser.add_argument(
        "--max-results-per-category",
        type=int,
        default=30,
        help="Maximum arXiv results to fetch per category before local keyword filtering.",
    )
    parser.add_argument(
        "--out",
        default="",
        help="Optional JSON output file. If omitted, JSON is printed to stdout.",
    )
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    categories = ensure_list(args.categories)
    keywords = parse_keywords(args.keywords)
    papers = fetch_arxiv_papers(
        categories=categories,
        days=args.days,
        keywords=keywords,
        max_results_per_category=args.max_results_per_category,
    )
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "categories": categories,
        "days": args.days,
        "keywords": keywords,
        "count": len(papers),
        "papers": papers,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as file:
            file.write(text + "\n")
    else:
        print(text)


if __name__ == "__main__":
    main()

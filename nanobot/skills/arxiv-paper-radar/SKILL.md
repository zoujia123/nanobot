---
name: arxiv-paper-radar
description: Use this skill when the user wants to find, filter, tag, summarize, or report recent arXiv papers for a research topic, especially LLM systems papers such as serving, inference, training, offloading, kernels, or systems optimization.
---

# Arxiv Paper Radar

Use this skill to turn a user request like "帮我找最近 2 天 cs.DC/cs.OS 里和 LLM serving 相关的论文，给我中文总结" into a small research digest.

## Default Workflow

1. Identify the topic, arXiv categories, date range, and output language.
2. If missing, use these defaults:
   - Topic: LLM systems
   - Categories: `cs.DC cs.OS`
   - Date range: last 2 days
   - Output: Chinese Markdown digest
3. Run `scripts/fetch_arxiv.py` to fetch paper metadata from arXiv.
4. Read `references/relevance.md` and filter papers by title and abstract.
5. Read `references/tags.md` and assign up to 3 strong tags per relevant paper.
6. Read `references/report-format.md` and produce a concise Chinese Markdown report.

## Fetch Command

For the common LLM serving request, run:

```powershell
python arxiv-paper-radar/scripts/fetch_arxiv.py --categories cs.DC cs.OS --days 2 --keywords "llm,large language model,language model,serving,inference,prefill,decode,kv cache,batching,scheduling,speculative,vllm,sglang" --max-results-per-category 200
```

If the skill folder has been copied elsewhere, adjust the path to `scripts/fetch_arxiv.py`.

## Filtering Guidance

- Prefer semantic relevance over keyword matching.
- Include papers that improve large-model serving, inference, scheduling, batching, caching, offloading, networking, kernels, quantization, or resource efficiency.
- Exclude papers that merely use LLMs for an application, benchmark, security study, or pure model-capability improvement.
- If uncertain, include the paper only when the abstract states a systems problem and a systems method.

## Output Guidance

Default to answering in chat. Only create files if the user explicitly asks for a saved Markdown, JSON, README section, or PPT outline.

For each relevant paper, include:

- Chinese title summary or original title
- arXiv link
- Tags
- Why it is relevant
- Chinese TL;DR with problem, method, and result if available

## Dependency Note

The fetch script needs the Python package `arxiv`. If it is missing, install it in the active environment, for example:

```powershell
uv pip install arxiv
```

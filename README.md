# Investment Research Agent

An agentic financial analysis system: given a stock ticker, it plans its research, routes news, earnings, and market signals to specialized analyzers, and critiques and iteratively refines its own output to produce a research brief covering market data, recent news, earnings, and potential risks — combining multi-agent LLM orchestration with classical NLP sentiment analysis.

## Course Information

- **Course:** Natural Language Processing and GenAI (AAI-520-01) — University of San Diego
- **Assignment:** Final Team Project: Multi-Agent System
- **Published:** October 19, 2026
- **Group:** 10

## Team

- Pravin Suranthiran
- Emma Bishop

## Repository Structure

- `notebooks/` — analysis notebooks (project deliverables)
- `data/raw/`, `data/processed/` — data created by the notebooks (not committed)
- `docs/` — project documentation; [`sources.md`](docs/sources.md) records every dataset and API used, with APA 7 citations
- `report/` — final written report

## Setup

Requires [uv](https://docs.astral.sh/uv/). Install dependencies:

```bash
uv sync
```

The notebooks in `notebooks/` run in any Jupyter-compatible editor (VS Code, JupyterLab, etc.); select the interpreter or kernel from the `.venv` this creates.

---

*AI Use Notice: AI was used to assist in the development of this project, but all analysis and conclusions have been verified and directed by the authors.*

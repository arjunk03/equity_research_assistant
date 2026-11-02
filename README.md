# Equitty Research Assistant

Python project managed with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync --group dev
uv run pre-commit install
```

## Checks

```bash
uv run ruff check .
uv run ruff format .
uv run mypy
uv run pytest
uv run pre-commit run --all-files
```

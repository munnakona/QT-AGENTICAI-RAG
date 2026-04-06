# hello-langgraph

Simple LangGraph example that builds a small graph with two nodes (`friends` and
`family`) and invokes it to produce a combined state.

## Overview

- **Graph definition:** `hello.py`
- **LangGraph config:** `langgraph.json`

The graph uses a typed state (`MyState`) and two nodes that populate friends and
family lists. The graph starts at `START`, runs the `friends` node, then the
`family` node, and ends at `END`.

## Requirements

- Python 3.13+
- Dependencies managed via `pyproject.toml`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run the example

```bash
python hello.py
```

You should see output similar to:

```text
{'name': 'John', 'friends': ['Alice', 'Bob', 'Charlie'], 'family': ['Mom', 'Dad', 'Sister'], 'message': 'Hello, World!'}
```

## Project structure

```text
.
├── hello.py          # Graph definition and execution
├── main.py           # Placeholder main entry point
├── langgraph.json    # LangGraph CLI configuration
├── pyproject.toml    # Project metadata and dependencies
└── README.md
```
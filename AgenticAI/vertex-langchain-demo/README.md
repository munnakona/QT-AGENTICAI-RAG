# Vertex LangChain Demo

Small Python example that calls Google Gemini via LangChain (Vertex AI) and prints the response.

## Prerequisites

- Python 3.13+
- Access to Google Cloud Vertex AI
- A `.env` file with your Google Cloud project ID

Example `.env`:

```bash
GOOGLE_CLOUD_PROJECT=your-project-id
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> This project uses `pyproject.toml`. If you prefer, install with `pip install -e .` or `uv pip install -r uv.lock`.

## Run

```bash
python main.py
```

## What it does

- Loads environment variables from `.env`
- Initializes `ChatGoogleGenerativeAI` with the Gemini model on Vertex AI
- Asks a sample question and prints the model response
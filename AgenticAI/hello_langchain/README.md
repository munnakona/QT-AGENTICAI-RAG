# hello-langchain

Minimal LangChain + Google Vertex AI (Gemini) demo project.

## Overview

This repo contains a small example that uses `langchain-google-genai` to query a
Vertex AI Gemini model. The primary script is `gcp_test.py`, which prompts for a
country name and returns the capital with a short educational explanation.

## Requirements

- Python **3.13+**
- Google Cloud project with Vertex AI enabled
- Authenticated Google Cloud credentials

## Setup

1. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -e .
   ```

3. **Configure environment variables** in a `.env` file at the project root:

   ```env
   GOOGLE_CLOUD_PROJECT=your-gcp-project-id
   # Optional but commonly required for local auth:
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
   ```

4. **Authenticate with Google Cloud** (if not already done):

   ```bash
   gcloud auth application-default login
   ```

## Usage

Run the demo script:

```bash
python gcp_test.py
```

You can also run the simple hello script:

```bash
python main.py
```

## Project Structure

- `gcp_test.py` — Vertex AI Gemini demo using LangChain.
- `main.py` — Simple hello-world entrypoint.
- `pyproject.toml` — Project metadata and dependencies.

## Notes

- The model used is `gemini-2.5-flash-lite` with Vertex AI enabled.
- Make sure Vertex AI APIs are enabled in your Google Cloud project.
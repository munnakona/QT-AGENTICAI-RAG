# Tool Calling (LangChain + Gemini)

This project demonstrates basic tool calling with LangChain and Google Gemini (Vertex AI) in a Jupyter notebook.

## Contents

- `tool_calling.ipynb`: Walks through tool definitions, binding tools to the LLM, and invoking responses with and without tools.

## Prerequisites

- Python 3.10+
- A Google Cloud project with Vertex AI enabled
- Environment variables in a `.env` file

Example `.env`:

```bash
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U langchain-core langchain-google-genai python-dotenv jupyter
```

## Run

```bash
jupyter notebook tool_calling.ipynb
```

## Notes

- The notebook uses the `gemini-2.5-flash` model through `ChatGoogleGenerativeAI`.
- If you use a different model or runtime, update the notebook accordingly.

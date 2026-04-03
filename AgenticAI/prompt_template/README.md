# Prompt Templates (LangChain + Gemini)

This project demonstrates prompt templates and message-based prompting with LangChain and Google Gemini (Vertex AI) in a Jupyter notebook.

## Contents

- `prompt_templates.ipynb`: Covers `PromptTemplate`, chained prompts, few-shot examples, and `ChatPromptTemplate` usage.

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
jupyter notebook prompt_templates.ipynb
```

## Notes

- The notebook uses the `gemini-2.5-flash` model through `ChatGoogleGenerativeAI`.
- Update the project ID or model as needed.

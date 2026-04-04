# Tool Calling (LangChain + Gemini)

This project demonstrates basic tool calling with LangChain and Google Gemini (Vertex AI) in a Jupyter notebook.

## Contents

- `tool_calling.ipynb`: Walks through tool definitions, binding tools to the LLM, and invoking responses with and without tools.
- `tools_contd.ipynb`: Continues with additional tools (greetings, Tavily search, and multi-tool agents).

## Prerequisites

- Python 3.10+
- A Google Cloud project with Vertex AI enabled
- Environment variables in a `.env` file
- (Optional) Tavily API key if you want to run the Tavily search examples

Example `.env`:

```bash
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
TAVILY_API_KEY=your-tavily-api-key
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U langchain-core langchain-google-genai python-dotenv langchain-tavily jupyter
```

## Run

```bash
jupyter notebook tool_calling.ipynb
```

You can also run the continuation notebook:

```bash
jupyter notebook tools_contd.ipynb
```

## Notes

- The notebook uses the `gemini-2.5-flash` model through `ChatGoogleGenerativeAI`.
- If you use a different model or runtime, update the notebook accordingly.

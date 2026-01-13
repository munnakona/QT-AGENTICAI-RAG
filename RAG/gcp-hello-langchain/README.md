# GCP Hello LangChain

A simple demonstration project showcasing the integration of LangChain with Google Vertex AI's Gemini models using the uv package manager.

## Description

This project provides a basic example of how to use LangChain to interact with Google's Gemini models through Vertex AI. It initializes a chat model and demonstrates a simple query-response interaction.

## Prerequisites

- Python 3.13 or higher
- uv package manager
- Google Cloud Platform account with Vertex AI enabled
- Authentication configured (e.g., via `gcloud auth application-default login`)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gcp-hello-langchain
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Usage

Run the main script to see a demonstration:

```bash
uv run python main.py
```

This will initialize the Gemini model and ask for the capital of France, printing the response.

## Dependencies

- `langchain>=1.2.3`
- `langchain-google-vertexai>=3.2.1`

## Configuration

Ensure your Google Cloud credentials are set up properly. You can authenticate using:

```bash
gcloud auth application-default login
```

And set your project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

## License

Add your license information here.

# HR Policy RAG

A Retrieval-Augmented Generation (RAG) system for HR policies using LangChain and Google VertexAI.

## Description

This project implements a RAG system designed to process and query HR policy documents. It uses LangChain for building the RAG pipeline, Google VertexAI for language model capabilities, and docx2txt for extracting text from Word documents.

## Features

- Process HR policy documents in DOCX format
- Generate embeddings and store in vector database
- Query policies using natural language
- Generate responses based on policy content

## Installation

1. Ensure you have Python 3.13 or higher installed.

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Set up your Google VertexAI credentials. Refer to the [Google Cloud documentation](https://cloud.google.com/vertex-ai/docs/start) for setup instructions.

## Usage

1. Place your HR policy documents in the `Policies/CompanyPolicies/` directory.

2. Run the data generator notebook `datagenerator.ipynb` to process documents and generate embeddings.

3. Use the main application to query policies:
   ```bash
   uv run python main.py
   ```

## Project Structure

- `main.py`: Main application entry point
- `datagenerator.ipynb`: Jupyter notebook for data processing and generation
- `Policies/`: Directory containing original policy documents
- `GeneratedPolicies/`: Directory for processed/generated policy files
- `pyproject.toml`: Project configuration and dependencies

## Dependencies

- docx2txt: For extracting text from DOCX files
- langchain: Framework for building LLM applications
- langchain-community: Community integrations for LangChain
- langchain-google-vertexai: Google VertexAI integration for LangChain

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
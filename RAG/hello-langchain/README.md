# Hello LangChain

This project provides examples and code for building applications with LangChain, a framework for developing applications powered by language models.

## Project Structure

- `main.py`: Main Python script (if applicable).
- `notebooks/`: Directory containing Jupyter notebooks.
  - `hello-langchain.ipynb`: Introductory notebook demonstrating basic LangChain usage with OpenAI models.
- `pyproject.toml`: Project configuration file.
- `uv.lock`: Dependency lock file.
- `.env`: Environment variables (add your OpenAI API key here).
- `.gitignore`: Git ignore rules.

## Getting Started

1. Ensure you have Python installed (see `.python-version` for the recommended version).
2. Install dependencies using `uv` or `pip`:
   ```
   uv sync
   ```
   or
   ```
   pip install -r requirements.txt  # if you have one
   ```

3. Set up your environment:
   - Copy `.env` and add your OpenAI API key.

4. Run the main script or explore the notebooks.

## Notebooks

### Hello LangChain Notebook

Located in `notebooks/hello-langchain.ipynb`, this notebook provides a simple introduction to:
- Setting up LangChain with OpenAI.
- Making basic API calls to language models.

**Prerequisites for the notebook:**
- Install additional packages: `pip install langchain-openai jupyter`
- Launch Jupyter: `jupyter notebook`
- Open the notebook and run cells.

**Note:** The notebook may have some setup issues (e.g., missing packages or incorrect model initialization). Refer to error messages and install required dependencies.

## Requirements

- Python 3.8+
- LangChain
- OpenAI API key

## License

[Add license if applicable]

For more information, visit the [LangChain documentation](https://python.langchain.com/).

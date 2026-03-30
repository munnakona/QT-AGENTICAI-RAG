# AWS Bedrock Test

A minimal Python example that invokes **Amazon Bedrock** models through
`langchain-aws`. The current script demonstrates a single prompt to the
`amazon.nova-micro-v1:0` model and prints the response.

## Prerequisites

- **Python** >= 3.13
- **AWS credentials** with access to Amazon Bedrock in `us-east-1`
- (Optional) **uv** for faster dependency management

## Setup

### 1) Install dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or with `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r <(python -m piptools compile pyproject.toml)
```

### 2) Configure AWS credentials

Make sure your AWS credentials are available to the SDK. Common options:

- Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
- Shared config: `~/.aws/credentials`
- AWS SSO / IAM role (if running in an AWS environment)

If you prefer `.env` files, add them and load using `python-dotenv`.

## Usage

Run the example script:

```bash
python main.py
```

You should see the model response printed to stdout.

## Project Structure

```text
.
├─ main.py           # Bedrock invocation example
├─ pyproject.toml    # Project metadata and dependencies
└─ README.md
```

## Notes

- The example uses the `amazon.nova-micro-v1:0` model in `us-east-1`.
- Tune `temperature` and `max_tokens` in `main.py` to control responses.

from typing import Optional
import os

from langchain_core.language_models.chat_models import BaseChatModel

# Google Gemini (Vertex AI / GenAI)
from langchain_google_genai import ChatGoogleGenerativeAI

# (Optional future providers)
# from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import AzureChatOpenAI


class LLMConfig:
    """Central config (can extend later)"""

    def __init__(
        self,
        provider: str = "google",
        project: Optional[str] = None,
        location: str = "us-central1",
        temperature: float = 0.2,
    ):
        self.provider = provider
        self.project = project or os.getenv("GOOGLE_CLOUD_PROJECT")
        self.location = location
        self.temperature = temperature


def _get_google_llm(model: str, config: LLMConfig) -> BaseChatModel:
    """Google Gemini / Vertex AI"""
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=config.temperature,
        vertexai=True,  # important for GCP
        project=config.project,
        location=config.location,
    )


# Future extension example
def _get_openai_llm(model: str, config: LLMConfig) -> BaseChatModel:
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=model,
        temperature=config.temperature,
    )


def get_llm(
    model: str,
    provider: str = "google",
    config: Optional[LLMConfig] = None,
) -> BaseChatModel:
    """
    Factory method to return LLM instance

    Example:
        get_llm("gemini-2.5-flash-lite")
        get_llm("gpt-4o-mini", provider="openai")
    """
    config = config or LLMConfig(provider=provider)

    provider = provider.lower()

    if provider == "google":
        return _get_google_llm(model, config)

    elif provider == "openai":
        return _get_openai_llm(model, config)

    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    
# Usage in your LangGraph project   

# from llm_factory import get_llm

# llm = get_llm("gemini-2.5-flash-lite")

"""from llm_factory import get_llm, LLMConfig

config = LLMConfig(
    project="your-project-id",
    location="us-central1",
    temperature=0.3
)

llm = get_llm(
    model="gemini-2.5-flash-lite",
    provider="google",
    config=config
)"""
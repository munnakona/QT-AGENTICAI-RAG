from langchain.chat_models import init_chat_model

gemini_llm = init_chat_model("gemini-2.5-flash-lite", model_provider="google_vertexai")
response = gemini_llm.invoke("What is capital of france?")
response.pretty_print()

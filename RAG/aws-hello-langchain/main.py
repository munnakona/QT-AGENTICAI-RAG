from langchain_aws import ChatBedrock

llm = ChatBedrock(
    model_id="amazon.titan-text-lite-v1",
    region_name="us-east-1",
)

response = llm.invoke("What is capital of France?")
print(response.content)

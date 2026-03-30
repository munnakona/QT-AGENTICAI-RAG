from langchain_aws import ChatBedrockConverse


def main():
    llm  = ChatBedrockConverse(
        model="amazon.nova-micro-v1:0",
        region_name="us-east-1",
        temperature=0,
        max_tokens=256
    )
    # Ask a question
    response = llm.invoke("What is the capital of France?")

    print(response.content)


if __name__ == "__main__":
    main()
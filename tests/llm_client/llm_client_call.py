from app.llm_client import LLMClient  # assuming your code is saved as llm_client.py


def main():
    # Initialize the client
    client = LLMClient()

    # Prepare messages in OpenAI-style format
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short motivational quote about learning."},
    ]

    # Generate response
    response = client.generate(messages)

    # Print the unified response
    print("=== LLMResponse ===")
    print(f"Content: {response.content}")
    print(f"Role: {response.role}")
    print(f"Finish Reason: {response.finish_reason}")
    print(f"Model: {response.model}")
    print(f"Usage: {response.usage}")


if __name__ == "__main__":
    main()

from app.agent import agent


def run_agent(question: str):

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    content = response["messages"][-1].content

    # Gemini may return content as a list of blocks
    if isinstance(content, list):

        text_parts = []

        for item in content:

            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))

            elif isinstance(item, str):
                text_parts.append(item)

        return "\n".join(text_parts)

    return str(content)


if __name__ == "__main__":

    print("=" * 60)
    print("LangChain Tool-Using Agent")
    print("=" * 60)

    while True:

        question = input("\nYou: ").strip()

        # Ignore empty input
        if not question:
            print("Please enter a question.")
            continue

        if question.lower() in ["exit", "quit"]:

            print("Agent stopped.")
            break

        try:

            answer = run_agent(question)

            print("\nAgent:", answer)

        except Exception as e:

            print("\nAgent Error:", e)
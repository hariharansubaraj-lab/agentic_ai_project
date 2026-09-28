from app.graph import graph
from langchain_core.messages import HumanMessage, ToolMessage


# ---------------------------------------------------------
# Run Agent
# ---------------------------------------------------------

def run_agent(question: str):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        }
    )

    messages = result["messages"]

    # -----------------------------------------------------
    # If calculator was used, return exact tool result
    # -----------------------------------------------------

    for message in reversed(messages):

        if isinstance(message, ToolMessage):

            if message.name == "calculator":
                return str(message.content)

    # -----------------------------------------------------
    # Otherwise return final AI response
    # -----------------------------------------------------

    for message in reversed(messages):

        if getattr(message, "type", None) == "ai":

            content = message.content

            if isinstance(content, str):
                return content

            if isinstance(content, list):

                text_parts = []

                for item in content:

                    if isinstance(item, dict):

                        if item.get("type") == "text":
                            text_parts.append(
                                item.get("text", "")
                            )

                    elif isinstance(item, str):
                        text_parts.append(item)

                return "\n".join(text_parts)

    return "No answer generated."


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("LangGraph Tool-Using Agent")
    print("=" * 60)

    while True:

        question = input("\nYou: ").strip()

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
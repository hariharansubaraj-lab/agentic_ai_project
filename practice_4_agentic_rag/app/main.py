from app.graph import graph


def main():

    print("=" * 60)
    print("        PRACTICE 4 - AGENTIC RAG")
    print("=" * 60)

    question = input("\nEnter your question: ")

    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "question": question,
            "context": "",
            "answer": ""
        }
    )

    print("\n" + "=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)

    print(result["answer"])


if __name__ == "__main__":
    main()
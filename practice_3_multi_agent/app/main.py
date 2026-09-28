from app.graph import graph


# ---------------------------------------------------------
# Run Multi-Agent System
# ---------------------------------------------------------

def run_multi_agent(question: str):

    result = graph.invoke({
        "question": question,
        "search_results": "",
        "research": "",
        "final_answer": ""
    })

    return result["final_answer"]


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("LangGraph Multi-Agent System")
    print("Researcher → Writer")
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

            answer = run_multi_agent(question)

            print("\nFinal Answer:")
            print(answer)

        except Exception as e:

            print("\nAgent Error:", e)
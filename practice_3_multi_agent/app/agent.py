from langchain_ollama import ChatOllama


# ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# ---------------------------------------------------------
# Researcher Agent
# ---------------------------------------------------------

def researcher_agent(question: str, search_results: str) -> str:

    prompt = f"""
You are a Researcher Agent.

User Question:
{question}

Web Search Results:
{search_results}

Analyze the search results and identify the important factual
information needed to answer the user's question.

Do not invent information.

Return a concise research summary.
"""

    response = llm.invoke(prompt)

    return response.content


# ---------------------------------------------------------
# Writer Agent
# ---------------------------------------------------------

def writer_agent(question: str, research: str) -> str:

    prompt = f"""
You are a Writer Agent.

User Question:
{question}

Researcher's Findings:
{research}

Write a clear and concise final answer.

Rules:
- Use only the information from the research.
- Do not invent facts.
- Answer the user's question directly.
- Keep the answer easy to understand.
"""

    response = llm.invoke(prompt)

    return response.content
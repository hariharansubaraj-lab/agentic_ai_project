from langchain_ollama import ChatOllama

from app.rag_tool import rag_search


# ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# ---------------------------------------------------------
# Agent with RAG Tool
# ---------------------------------------------------------

agent = llm.bind_tools(
    [rag_search],
    tool_choice="any"
)


# ---------------------------------------------------------
# Final Answer LLM
# ---------------------------------------------------------

answer_llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# ---------------------------------------------------------
# Generate Final Answer
# ---------------------------------------------------------

def generate_final_answer(question: str, context: str):

    prompt = f"""
You are a strict document-based question answering assistant.

User Question:
{question}

Retrieved Document Context:
{context}

Rules:
- Answer ONLY from the retrieved document context.
- Do NOT use outside knowledge.
- Do NOT guess.
- Do NOT assume missing information.
- If the answer is not present in the context, respond exactly:
  "The information is not available in the documents."
- Do not mention tools.
- Do not mention tool calls.
- Do not add greetings.
- Answer directly and concisely.
"""

    response = answer_llm.invoke(prompt)

    return response.content
from pathlib import Path

from langchain_core.tools import tool
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DOCS_PATH = Path(__file__).parent.parent / "documents"


# ---------------------------------------------------------
# Embeddings
# ---------------------------------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# ---------------------------------------------------------
# Load Documents
# ---------------------------------------------------------

def load_documents():

    documents = []

    if not DOCS_PATH.exists():
        DOCS_PATH.mkdir(parents=True)

    for file in DOCS_PATH.glob("*.txt"):

        text = file.read_text(
            encoding="utf-8"
        )

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file.name
                }
            )
        )

    return documents


# ---------------------------------------------------------
# Create Vector Store
# ---------------------------------------------------------

documents = load_documents()

if documents:

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

else:

    vectorstore = None


# ---------------------------------------------------------
# RAG Tool
# ---------------------------------------------------------

@tool
def rag_search(query: str) -> str:
    """
    Search company documents and return relevant information.
    """

    if vectorstore is None:

        return "No documents are available for retrieval."

    results = vectorstore.similarity_search(
        query,
        k=3
    )

    if not results:

        return "No relevant information found."

    output = []

    for doc in results:

        output.append(
            f"Source: {doc.metadata.get('source', 'unknown')}\n"
            f"Content: {doc.page_content}"
        )

    return "\n\n".join(output)


# ---------------------------------------------------------
# Tools
# ---------------------------------------------------------

tools = [rag_search]
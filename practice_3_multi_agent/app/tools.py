import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_tavily import TavilySearch


load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY is missing in .env")


# ---------------------------------------------------------
# Tavily Search
# ---------------------------------------------------------

tavily = TavilySearch(
    max_results=3,
    tavily_api_key=tavily_api_key
)


@tool
def web_search(query: str) -> str:
    """Search the web for current and factual information."""

    try:

        results = tavily.invoke({
            "query": query
        })

        return str(results)

    except Exception as e:

        return f"Search error: {e}"
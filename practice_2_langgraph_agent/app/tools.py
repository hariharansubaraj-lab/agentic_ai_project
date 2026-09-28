import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults


load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY is missing")


# ---------------------------------------------------------
# Calculator
# ---------------------------------------------------------

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception as e:

        return f"Calculation error: {e}"


# ---------------------------------------------------------
# Tavily
# ---------------------------------------------------------

tavily = TavilySearchResults(
    max_results=3,
    tavily_api_key=tavily_api_key
)


@tool
def web_search(query: str) -> str:
    """Search the web for current information."""

    try:

        results = tavily.invoke({
            "query": query
        })

        if not results:
            return "No search results found."

        output = []

        for result in results:

            output.append(
                f"Title: {result.get('title', '')}\n"
                f"Content: {result.get('content', '')}\n"
                f"URL: {result.get('url', '')}"
            )

        return "\n\n".join(output)

    except Exception as e:

        return f"Web search error: {e}"


# ---------------------------------------------------------
# Tools
# ---------------------------------------------------------

tools = [
    calculator,
    web_search
]
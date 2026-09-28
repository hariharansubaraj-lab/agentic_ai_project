import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_tavily import TavilySearch


# Load .env from parent project folder
load_dotenv(
    r"C:\lfyngo task\agentic_ai_project\.env"
)


# ---------------------------------------------------------
# Calculator Tool
# ---------------------------------------------------------

@tool
async def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(expression, {"__builtins__": {}})
        return f"Calculation result: {result}"

    except Exception as e:
        return f"Calculation error: {e}"


# ---------------------------------------------------------
# Tavily Web Search Tool
# ---------------------------------------------------------

tavily = TavilySearch(
    max_results=3,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


@tool
async def web_search(query: str) -> str:
    """Search the web using Tavily."""

    result = await tavily.ainvoke({
        "query": query
    })

    return str(result)
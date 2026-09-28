import os
from dotenv import load_dotenv

load_dotenv()

from langchain_core.tools import tool
from langchain_tavily import TavilySearch


# ---------------------------------------------------------
# Web Search Tool
# ---------------------------------------------------------

search_tool = TavilySearch(
    max_results=3,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


# ---------------------------------------------------------
# Calculator Tool
# ---------------------------------------------------------

@tool
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    """

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
# All Tools
# ---------------------------------------------------------

tools = [
    search_tool,
    calculator
]
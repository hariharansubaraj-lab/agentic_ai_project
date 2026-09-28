from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from app.tools import tools


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a helpful AI agent.

You have access to:
1. A web search tool for current information.
2. A calculator tool for mathematical calculations.

Use web search for current information.
Use calculator for mathematical calculations.

Give clear and concise answers.
"""
)
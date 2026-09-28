from typing import TypedDict

from langchain_core.messages import BaseMessage, ToolMessage
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from app.tools import tools


# ---------------------------------------------------------
# State
# ---------------------------------------------------------

class AgentState(TypedDict):
    messages: list[BaseMessage]


# ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# Force the model to use a tool
llm_with_tools = llm.bind_tools(
    tools,
    tool_choice="any"
)


# ---------------------------------------------------------
# Agent Node
# ---------------------------------------------------------

def agent_node(state: AgentState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# ---------------------------------------------------------
# Tool Node
# ---------------------------------------------------------

tool_node = ToolNode(tools)


# ---------------------------------------------------------
# Agent → Tool / End
# ---------------------------------------------------------

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return "end"


# ---------------------------------------------------------
# After Tool
# ---------------------------------------------------------

def after_tools(state: AgentState):

    last_message = state["messages"][-1]

    # Calculator result can be returned directly
    if isinstance(last_message, ToolMessage):

        if last_message.name == "calculator":
            return "end"

    # Web search result goes back to LLM
    return "agent"


# ---------------------------------------------------------
# Build Graph
# ---------------------------------------------------------

workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

workflow.add_edge(
    START,
    "agent"
)

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)

workflow.add_conditional_edges(
    "tools",
    after_tools,
    {
        "agent": "agent",
        "end": END
    }
)


# ---------------------------------------------------------
# Compile
# ---------------------------------------------------------

graph = workflow.compile()
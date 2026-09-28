from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from app.agent import agent, generate_final_answer
from app.rag_tool import rag_search


# ---------------------------------------------------------
# State
# ---------------------------------------------------------

class AgentState(TypedDict):
    messages: list
    question: str
    context: str
    answer: str


# ---------------------------------------------------------
# Agent Node
# ---------------------------------------------------------

def agent_node(state: AgentState):

    response = agent.invoke(
        state["messages"]
    )

    return {
        "messages": state["messages"] + [response]
    }


# ---------------------------------------------------------
# Tool Node
# ---------------------------------------------------------

tool_node = ToolNode(
    [rag_search]
)


# ---------------------------------------------------------
# Collect Tool Result
# ---------------------------------------------------------

def collect_tool_result(state: AgentState):

    last_message = state["messages"][-1]

    context = ""

    if hasattr(last_message, "content"):
        context = str(last_message.content)

    return {
        "context": context
    }


# ---------------------------------------------------------
# Final Answer Node
# ---------------------------------------------------------

def final_answer_node(state: AgentState):

    answer = generate_final_answer(
        state["question"],
        state["context"]
    )

    return {
        "answer": answer
    }


# ---------------------------------------------------------
# Routing
# ---------------------------------------------------------

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return "final"


# ---------------------------------------------------------
# Build Graph
# ---------------------------------------------------------

workflow = StateGraph(AgentState)


workflow.add_node(
    "agent",
    agent_node
)

workflow.add_node(
    "tools",
    tool_node
)

workflow.add_node(
    "collect_context",
    collect_tool_result
)

workflow.add_node(
    "final_answer",
    final_answer_node
)


# ---------------------------------------------------------
# Edges
# ---------------------------------------------------------

workflow.add_edge(
    START,
    "agent"
)

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "final": "final_answer"
    }
)

workflow.add_edge(
    "tools",
    "collect_context"
)

workflow.add_edge(
    "collect_context",
    "final_answer"
)

workflow.add_edge(
    "final_answer",
    END
)


# ---------------------------------------------------------
# Compile
# ---------------------------------------------------------

graph = workflow.compile()
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.tools import web_search
from app.agent import researcher_agent, writer_agent


# ---------------------------------------------------------
# State
# ---------------------------------------------------------

class AgentState(TypedDict):

    question: str
    search_results: str
    research: str
    final_answer: str


# ---------------------------------------------------------
# Researcher Node
# ---------------------------------------------------------

def researcher_node(state: AgentState):

    question = state["question"]

    # Search the web
    search_results = web_search.invoke({
        "query": question
    })

    # Research the results
    research = researcher_agent(
        question,
        search_results
    )

    return {
        "search_results": search_results,
        "research": research
    }


# ---------------------------------------------------------
# Writer Node
# ---------------------------------------------------------

def writer_node(state: AgentState):

    question = state["question"]
    research = state["research"]

    final_answer = writer_agent(
        question,
        research
    )

    return {
        "final_answer": final_answer
    }


# ---------------------------------------------------------
# Supervisor Node
# ---------------------------------------------------------

def supervisor_node(state: AgentState):

    # For this practice, supervisor starts the workflow.
    return {}


# ---------------------------------------------------------
# Build Graph
# ---------------------------------------------------------

workflow = StateGraph(AgentState)


workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "researcher",
    researcher_node
)

workflow.add_node(
    "writer",
    writer_node
)


# ---------------------------------------------------------
# Edges
# ---------------------------------------------------------

workflow.add_edge(
    START,
    "supervisor"
)

workflow.add_edge(
    "supervisor",
    "researcher"
)

workflow.add_edge(
    "researcher",
    "writer"
)

workflow.add_edge(
    "writer",
    END
)


# ---------------------------------------------------------
# Compile
# ---------------------------------------------------------

graph = workflow.compile()
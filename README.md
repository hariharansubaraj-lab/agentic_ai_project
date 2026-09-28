# 🤖 Agentic AI Project

A comprehensive collection of hands-on implementations and architectures for **Agentic AI systems**, powered by **LangChain**, **LangGraph**, **Google Gemini**, and **Local Ollama (Llama 3.2)**.

---

## 📂 Project Structure

```text
agentic_ai_project/
├── practice_1_langchain_agent/    # Practice 1: ReAct Agent with LangChain & Tavily
│   └── app/
│       ├── agent.py
│       ├── main.py
│       └── tools.py
├── practice_2_langgraph_agent/    # Practice 2: Graph-based Agent with LangGraph & Ollama
│   └── app/
│       ├── graph.py
│       ├── main.py
│       └── tools.py
├── practice_3_multi_agent/        # Practice 3: Multi-Agent Collaboration (Researcher + Writer)
│   └── app/
│       ├── agent.py
│       ├── graph.py
│       ├── main.py
│       └── tools.py
├── practice_4_agentic_rag/        # Practice 4: Agentic RAG with LangGraph & Document Retrieval
│   ├── app/
│   │   ├── agent.py
│   │   ├── graph.py
│   │   ├── main.py
│   │   └── rag_tool.py
│   └── documents/
│       └── company.txt
├── practice_5_async_tools/        # Practice 5: Concurrent Async Tool Execution
│   └── app/
│       ├── async_runner.py
│       ├── main.py
│       └── tools.py
├── .env.example                   # Environment configuration template
├── .gitignore                     # Git exclusion rules
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

---

## 🚀 Practices Overview

### 1. LangChain Tool-Using Agent (`practice_1_langchain_agent`)
- Implements a conversational agent using LangChain and Gemini with tool calling capabilities.
- Integrated with **Tavily Search** for real-time web querying and answer generation.

### 2. LangGraph State-Based Agent (`practice_2_langgraph_agent`)
- Uses **LangGraph** `StateGraph` to build a cyclical agent loop.
- Uses local **ChatOllama (Llama 3.2)** model with custom arithmetic tools (`add`, `multiply`).
- Demonstrates state-driven tool calling and tool node execution.

### 3. Multi-Agent System (`practice_3_multi_agent`)
- Multi-agent collaboration workflow built with LangGraph:
  - **Researcher Node**: Gathers real-time web information using Tavily search.
  - **Writer Node**: Synthesizes and drafts a polished final report based on gathered research.

### 4. Agentic RAG (`practice_4_agentic_rag`)
- Retrieval-Augmented Generation (RAG) agent with decision-making capabilities.
- Intelligently decides when to search local internal documents versus generating direct answers.
- Includes context-grounded final answer synthesis.

### 5. Async Tool Execution (`practice_5_async_tools`)
- Demonstrates high-performance asynchronous tool execution using Python's `asyncio.gather`.
- Concurrently runs slow tools (e.g., external search APIs and compute tasks) in parallel.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Python 3.10+**
- **Ollama** installed with `llama3.2` model pulled:
  ```bash
  ollama run llama3.2
  ```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Fill in your API keys in `.env`:
- `GEMINI_API_KEY`: Google AI Studio API key.
- `TAVILY_API_KEY`: Tavily Search API key.

---

## ▶️ Running the Practices

Run any practice from the root directory:

```bash
# Practice 1: LangChain Agent
python practice_1_langchain_agent/app/main.py

# Practice 2: LangGraph Agent
python practice_2_langgraph_agent/app/main.py

# Practice 3: Multi-Agent Collaboration
python practice_3_multi_agent/app/main.py

# Practice 4: Agentic RAG
python practice_4_agentic_rag/app/main.py

# Practice 5: Async Tools
python practice_5_async_tools/app/main.py
```

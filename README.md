# Mini Company Knowledge Bot

A lightweight document-based QA system that demonstrates simple ingestion, context retrieval, and an agent-style memory structure for company knowledge.

---

## What this project does

This bot allows users to ask questions about internal company policies. It retrieves answers from a small set of structured documents in the `docs/` folder.

The goal is to simulate a minimal "company knowledge system" without using external vector databases or LLM APIs.

---

## How it works (Architecture)

1. The user asks a question via CLI (`app.py`)
2. The system loads documents from the `docs/` folder
3. A simple keyword-based matching algorithm finds relevant document sections
4. The best matching document is returned as the answer

This is intentionally a minimal implementation to keep ingestion logic transparent and easy to debug.

---

## Project Structure

- `docs/`: Knowledge base (policies, FAQs)
- `agentic-brain/`: Memory + evaluation system for agent behavior
- `app.py`: CLI entry point

---

## Agentic Brain

This project includes an experimental "agent memory layer":

- `PROJECT_BRIEF.md`: Defines scope and MVP
- `AGENT_CONTEXT.md`: How the system should be understood by future agents
- `MEMORY.md`: Tracks decisions, mistakes, and learning
- `TASKS.md`: Completed and pending tasks
- `EVALS.md`: Test questions and expected answers

This simulates how an AI agent can continue development over time.

---

## Design Decisions

- No vector database or embeddings are used — retrieval is fully deterministic and keyword-based for transparency and debuggability
- File-based ingestion for easy debugging and portability
- Keyword matching instead of embeddings for MVP simplicity
- Focus on structure and reproducibility over complexity

---

## Run

No dependencies required (pure Python).

```bash
python app.py
# Agent Context

## Project Overview

This project implements a simple company knowledge bot.

The bot reads documents from the docs directory and answers questions using information found in those documents.

## Repository Structure

docs/
- faq.md
- leave_policy.md
- product.md

agentic-brain/
- PROJECT_BRIEF.md
- AGENT_CONTEXT.md
- MEMORY.md
- TASKS.md
- EVALS.md

app.py
README.md
requirements.txt

## Current Status

Completed:
- Repository initialization
- Project structure
- Company documents

Planned:
- Document ingestion
- Question answering logic
- CLI interface
- Docker support

## Development Notes

The initial implementation will use simple keyword-based retrieval.

Future versions may use embeddings and semantic search.

## Entry Point

Main application entry point:

app.py
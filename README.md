# Agentic Software Engineering Workflow

## Overview

This project demonstrates a multi-agent software engineering workflow using LangGraph and Ollama. The system accepts software requirements and coordinates multiple AI agents to generate a FastAPI application.

## Architecture

The workflow consists of four agents:

1. Requirement Agent
   - Analyzes and refines user requirements.

2. Planner Agent
   - Breaks requirements into implementation tasks.

3. Architecture Agent
   - Designs the application structure and components.

4. Code Generation Agent
   - Generates the FastAPI project files.

## Workflow

```
User Requirement
        │
        ▼
Requirement Agent
        │
        ▼
Planner Agent
        │
        ▼
Architecture Agent
        │
        ▼
Code Generation Agent
        │
        ▼
Generated FastAPI Project
```

## Project Structure

```
agentic-engineer/
├── agents/
├── prompts/
├── generated/
├── app.py
├── workflow.py
├── requirements.txt
└── README.md
```

## Technologies

- Python
- LangGraph
- LangChain
- Ollama
- FastAPI

## Installation

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The generated FastAPI application can be started using:

```bash
cd generated
uvicorn main:app --reload
```

## Output

The workflow generates:

- database.py
- models.py
- schemas.py
- routes.py
- main.py
- requirements.txt
- README.md

## Future Improvements

- Validation Agent
- Auto Fix Agent
- Unit Test Generation
- Support for multiple frameworks
- CI/CD integration

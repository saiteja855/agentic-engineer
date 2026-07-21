# 🚀 Agentic Software Engineering Workflow

An AI-powered multi-agent software engineering system that transforms software requirements into a fully structured FastAPI application using **LangGraph**, **LangChain**, and **Ollama**.

---

## 📌 Project Overview

This project demonstrates how multiple AI agents can collaborate to automate the software development lifecycle.

Instead of generating code directly from a prompt, the system follows an agent-based workflow where each agent is responsible for a specific phase of software engineering.

The generated output is a production-style FastAPI project containing the required application files.

---

# 🏗 Architecture

```text
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

---

# 🤖 Agents

## 1️⃣ Requirement Agent

**Responsibilities**

- Analyze user requirements
- Remove ambiguity
- Produce structured functional requirements

---

## 2️⃣ Planner Agent

**Responsibilities**

- Break the problem into implementation tasks
- Identify required components
- Create an execution plan

---

## 3️⃣ Architecture Agent

**Responsibilities**

- Design project architecture
- Define project modules
- Identify dependencies

---

## 4️⃣ Code Generation Agent

**Responsibilities**

Generate:

- database.py
- models.py
- schemas.py
- routes.py
- main.py
- requirements.txt
- README.md

---

# 📂 Project Structure

```
agentic-engineer/
│
├── agents/
│   ├── architecture_agent.py
│   ├── code_generation_agent.py
│   ├── planner_agent.py
│   └── requirement_agent.py
│
├── prompts/
│   ├── database_prompt.txt
│   ├── main_prompt.txt
│   ├── models_prompt.txt
│   ├── readme_prompt.txt
│   ├── requirements_prompt.txt
│   ├── routes_prompt.txt
│   └── schemas_prompt.txt
│
├── generated/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── app.py
├── workflow.py
├── requirements.txt
└── README.md
```

---

# ⚙ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | Agent Workflow |
| LangChain | LLM Orchestration |
| Ollama | Local LLM Execution |
| FastAPI | Generated REST API |
| SQLite | Generated Database |

---

# 🔄 Workflow

1. User provides software requirements.
2. Requirement Agent refines the requirements.
3. Planner Agent creates an implementation plan.
4. Architecture Agent designs the project.
5. Code Generation Agent creates the FastAPI application.
6. Generated files are stored inside the `generated` directory.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/saiteja855/agentic-engineer.git
```

Navigate to the project

```bash
cd agentic-engineer
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Linux

```bash
source .venv/bin/activate
```

Windows

```cmd
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Execute the workflow

```bash
python app.py
```

---

# ▶ Running the Generated FastAPI Application

Navigate to the generated project

```bash
cd generated
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

# 📁 Generated Output

The workflow automatically generates:

- ✔ Database Layer
- ✔ Models
- ✔ Schemas
- ✔ API Routes
- ✔ FastAPI Application
- ✔ Requirements
- ✔ Project Documentation

---

# 💡 Future Enhancements

- Validation Agent
- Auto-Fix Agent
- Unit Test Generation
- Docker Support
- CI/CD Integration
- Multi-language Code Generation
- Support for Spring Boot, Node.js, Django, and Flask

---

# 📷 Sample Execution

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

---

# 📈 Key Features

- Multi-Agent AI Workflow
- LangGraph State Management
- Prompt-based Code Generation
- Modular Agent Design
- Automatic FastAPI Project Generation
- Extensible Architecture

---

# 👨‍💻 Author

**Sai Teja**

Agentic Software Engineering Assessment Project

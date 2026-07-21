from langchain_ollama import ChatOllama


class ArchitectureAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3.1:8b",
            temperature=0
        )

    def design(self, plan: str):

        prompt = f"""
You are a Principal Software Architect.

Implementation Plan

{plan}

Design the software architecture.

STRICT RULES

The application MUST use:

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

Generate ONLY these files:

main.py
database.py
models.py
schemas.py
routes.py
requirements.txt
README.md

Do NOT generate additional folders.

Do NOT use Java.

Do NOT use Spring Boot.

Do NOT use Django.

Do NOT use Flask.

Do NOT use Poetry.

Do NOT invent extra features.

The application requirements are ONLY:

- Accept Long URL
- Generate Short URL
- Redirect using Short URL

Return ONLY the following sections.

# Architecture Overview

# Responsibilities

Explain each file.

main.py

database.py

models.py

schemas.py

routes.py

requirements.txt

README.md

# API Endpoints

POST /shorten

GET /{{short_code}}

GET /stats/{{short_code}}

# Database Schema

Table: urls

Columns

id

long_url

short_code

created_at

# Request Flow

Explain request flow.

Do not explain your reasoning.
"""

        response = self.llm.invoke(prompt)

        return response.content

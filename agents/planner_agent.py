from langchain_ollama import ChatOllama


class PlannerAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3.1:8b",
            temperature=0
        )

    def plan(self, requirements: str):

        prompt = f"""
You are a Principal Software Architect.

Below is the Software Requirement Specification.

{requirements}

Your task is to create a detailed implementation plan.

STRICT RULES

Use ONLY:

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

Do NOT use:

- Java
- Spring Boot
- Maven
- Gradle
- NodeJS
- Express
- Django
- Flask
- Poetry
- Docker
- Kubernetes
- OAuth
- JWT

Do NOT invent features that are not present in the requirements.

Return ONLY the following sections.

# Project Overview

# Modules

Explain every module.

# Files To Generate

List ONLY these files.

main.py

database.py

models.py

schemas.py

routes.py

requirements.txt

README.md

# Folder Structure

Use exactly:

generated/

main.py

database.py

models.py

schemas.py

routes.py

requirements.txt

README.md

# Development Order

Step-by-step implementation order.

# Dependencies

Only Python libraries.

# Risks

Mention only project-related risks.

Do not explain your reasoning.
"""

        response = self.llm.invoke(prompt)

        return response.content

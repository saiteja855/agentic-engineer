from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()


class RequirementAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3.1:8b",
            temperature=0
        )

    def analyze(self, requirement: str):

        prompt = f"""
You are a Principal Software Architect with 20 years of experience.

Your job is to convert a business requirement into a detailed Software Requirement Specification (SRS).

Business Requirement

{requirement}

The application MUST be implemented using:

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- REST APIs

Do NOT suggest Java, Spring Boot, Maven, NodeJS, .NET or any other technology.

Return your answer in the following format.

# Project Summary

Explain the application in 3-5 lines.

# Functional Requirements

List every functional requirement.

# Non Functional Requirements

Performance

Security

Scalability

Maintainability

Availability

# API Requirements

List every REST API required.

Mention:

Method

Endpoint

Purpose

# Database Requirements

List every table.

Mention important columns.

Mention relationships.

# Business Rules

List important business rules.

# Validation Rules

List all validations.

# Edge Cases

List possible edge cases.

# Assumptions

List assumptions.

# Risks

List implementation risks.

Only return the SRS.

Do not explain your reasoning.
"""

        response = self.llm.invoke(prompt)

        return response.content

from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.requirement_agent import RequirementAgent
from agents.planner_agent import PlannerAgent
from agents.architecture_agent import ArchitectureAgent
from agents.code_generation_agent import CodeGenerationAgent


class AgentState(TypedDict):
    requirement: str
    analysis: str
    plan: str
    architecture: str
    code: str


# Initialize Agents
requirement_agent = RequirementAgent()
planner_agent = PlannerAgent()
architecture_agent = ArchitectureAgent()
code_agent = CodeGenerationAgent()


# -------------------------------
# Requirement Agent
# -------------------------------
def analyze_requirement(state: AgentState):

    analysis = requirement_agent.analyze(
        state["requirement"]
    )

    return {
        "analysis": analysis
    }


# -------------------------------
# Planner Agent
# -------------------------------
def create_plan(state: AgentState):

    plan = planner_agent.plan(
        state["analysis"]
    )

    return {
        "plan": plan
    }


# -------------------------------
# Architecture Agent
# -------------------------------
def design_architecture(state: AgentState):

    architecture = architecture_agent.design(
        state["plan"]
    )

    return {
        "architecture": architecture
    }


# -------------------------------
# Code Generation Agent
# -------------------------------
def generate_code(state: AgentState):

    code = code_agent.generate(
        state["architecture"]
    )

    return {
        "code": code
    }


# -------------------------------
# Build Workflow
# -------------------------------
builder = StateGraph(AgentState)

builder.add_node(
    "requirement",
    analyze_requirement
)

builder.add_node(
    "planner",
    create_plan
)

builder.add_node(
    "architecture",
    design_architecture
)

builder.add_node(
    "code",
    generate_code
)

builder.set_entry_point("requirement")

builder.add_edge(
    "requirement",
    "planner"
)

builder.add_edge(
    "planner",
    "architecture"
)

builder.add_edge(
    "architecture",
    "code"
)

builder.add_edge(
    "code",
    END
)

workflow = builder.compile()

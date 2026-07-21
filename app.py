from workflow import workflow

requirement = """
Build a URL Shortener web application.

Requirements:

- Users should submit a long URL.
- Generate a unique short URL.
- Redirect short URL to the original URL.
- Expose REST APIs.
- Use Python FastAPI.
- Use SQLite database.
"""

print("\n===================================================")
print("      AGENTIC SOFTWARE ENGINEERING WORKFLOW")
print("===================================================\n")

result = workflow.invoke(
    {
        "requirement": requirement
    }
)

print("\n========== REQUIREMENT ANALYSIS ==========\n")
print(result["analysis"])

print("\n========== IMPLEMENTATION PLAN ==========\n")
print(result["plan"])

print("\n========== SOFTWARE ARCHITECTURE ==========\n")
print(result["architecture"])

print("\n========== FILE GENERATION ==========\n")
print(result["code"])

print("\n===================================================")
print("           WORKFLOW COMPLETED SUCCESSFULLY")
print("===================================================\n")

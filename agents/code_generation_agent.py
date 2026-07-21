import os
import re
from pathlib import Path
from typing import Dict

from langchain_ollama import ChatOllama


class CodeGenerationAgent:
    """
    Context-aware code generation agent.

    Each generated file becomes context for the next file.

    Generation Order

    1. database.py
    2. models.py
    3. schemas.py
    4. routes.py
    5. main.py
    6. requirements.txt
    7. README.md
    """

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3.1:8b",
            temperature=0
        )

        self.output_dir = Path("generated")
        self.output_dir.mkdir(exist_ok=True)

        self.prompt_dir = Path("prompts")

        self.generation_order = [
            {
                "file": "database.py",
                "prompt": "database_prompt.txt"
            },
            {
                "file": "models.py",
                "prompt": "models_prompt.txt"
            },
            {
                "file": "schemas.py",
                "prompt": "schemas_prompt.txt"
            },
            {
                "file": "routes.py",
                "prompt": "routes_prompt.txt"
            },
            {
                "file": "main.py",
                "prompt": "main_prompt.txt"
            },
            {
                "file": "requirements.txt",
                "prompt": "requirements_prompt.txt"
            },
            {
                "file": "README.md",
                "prompt": "readme_prompt.txt"
            }
        ]

    ####################################################################
    # Prompt Loader
    ####################################################################

    def load_prompt(self, filename: str) -> str:

        prompt_file = self.prompt_dir / filename

        if not prompt_file.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_file}"
            )

        with open(prompt_file, "r", encoding="utf-8") as f:
            return f.read()

    ####################################################################
    # Response Cleaner
    ####################################################################

    def clean_response(self, response: str) -> str:

        response = response.strip()

        response = re.sub(
            r"^```[a-zA-Z0-9]*",
            "",
            response
        )

        response = re.sub(
            r"```$",
            "",
            response
        )

        return response.strip()

    ####################################################################
    # Save Generated File
    ####################################################################

    def save_file(
        self,
        filename: str,
        content: str
    ):

        path = self.output_dir / filename

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✓ Saved {path}")

    ####################################################################
    # Build Context
    ####################################################################

    def build_context(
        self,
        generated_files: Dict[str, str]
    ) -> str:
        if not generated_files:
            return """
No files have been generated yet.

Generate this file independently while following the architecture.
"""

        context = []

        context.append(
            """
=========================================================
PREVIOUSLY GENERATED FILES
=========================================================
"""
        )

        for filename, content in generated_files.items():

            context.append(
                f"""
---------------------------------------------------------
FILE : {filename}
---------------------------------------------------------

{content}

"""
            )

        return "\n".join(context)

    ####################################################################
    # Generate Single File
    ####################################################################

    def generate_file(
        self,
        filename: str,
        prompt_template: str,
        architecture: str,
        previous_context: str
    ) -> str:

        prompt = f"""
You are an Expert Python Software Engineer.

Your task is to generate ONLY ONE file.

=========================================================
TARGET FILE
=========================================================

{filename}

=========================================================
SOFTWARE ARCHITECTURE
=========================================================

{architecture}

=========================================================
PREVIOUSLY GENERATED FILES
=========================================================

{previous_context}

=========================================================
TASK
=========================================================

{prompt_template}

=========================================================
STRICT RULES
=========================================================

1. Generate ONLY {filename}

2. Do NOT generate any explanation.

3. Do NOT generate markdown.

4. Do NOT generate triple backticks.

5. Keep imports consistent with previous files.

6. Reuse existing models/classes/functions whenever possible.

7. Do not duplicate code.

8. Produce production-ready Python code.

9. Return ONLY the file content.
"""

        print(f"Generating {filename}...")

        response = self.llm.invoke(prompt)

        return self.clean_response(response.content)

    ####################################################################
    # Main Generation Workflow
    ####################################################################

    def generate(
        self,
        architecture: str
    ):
        print("\n===================================")
        print("Code Generation Started")
        print("===================================\n")

        generated_files: Dict[str, str] = {}

        summary = []

        for item in self.generation_order:

            filename = item["file"]
            prompt_name = item["prompt"]

            try:

                prompt_template = self.load_prompt(
                    prompt_name
                )

                previous_context = self.build_context(
                    generated_files
                )

                generated_code = self.generate_file(
                    filename=filename,
                    prompt_template=prompt_template,
                    architecture=architecture,
                    previous_context=previous_context
                )

                self.save_file(
                    filename,
                    generated_code
                )

                generated_files[filename] = generated_code

                summary.append(
                    (
                        filename,
                        "SUCCESS"
                    )
                )

            except Exception as ex:

                print(
                    f"✗ Failed to generate {filename}"
                )

                print(ex)

                summary.append(
                    (
                        filename,
                        "FAILED"
                    )
                )

        print("\n===================================")
        print("Generation Summary")
        print("===================================\n")

        success_count = 0

        for filename, status in summary:

            if status == "SUCCESS":

                success_count += 1
                print(f"✓ {filename}")

            else:

                print(f"✗ {filename}")

        print()

        print(
            f"Generated {success_count} of "
            f"{len(self.generation_order)} files."
        )

        if success_count != len(self.generation_order):

            print(
                "\nWARNING: Some files failed to generate."
            )

        print("\n===================================")
        print("Generated Files")
        print("===================================\n")

        for filename in generated_files.keys():

            print(
                f"- {self.output_dir / filename}"
            )

        print("\n===================================")
        print("Code Generation Completed")
        print("===================================\n")

        return {
            "status": "SUCCESS",
            "generated_files": generated_files,
            "summary": summary
        }

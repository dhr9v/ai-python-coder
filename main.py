import json
from llm import get_code
from writer import save_project
from runner import run_file

MAX_FIX_ATTEMPTS = 2

def main():
    user_prompt = input("Enter your prompt: ")

    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    print("\n Generating project...\n")
    raw_response = get_code(system_prompt, user_prompt)

    try:
        project_data = json.loads(raw_response)
    except json.JSONDecodeError:
        print(" AI did not return valid JSON.")
        return

    project_path = save_project(project_data)
    entry_file = project_data["entry_file"]

    print(f" Project created at: {project_path}")

    attempts = 0
    while attempts <= MAX_FIX_ATTEMPTS:
        print("\n▶ Running project...\n")
        result = run_file(project_path, entry_file)

        if result["returncode"] == 0:
            if result["stdout"]:
                print(" OUTPUT:")
                print(result["stdout"])
            print("\n Project executed successfully.")
            return

        print("\n ERROR:")
        print(result["stderr"])

        if attempts == MAX_FIX_ATTEMPTS:
            print("\n Max fix attempts reached.")
            return

        print("\n🔧 Sending error back to AI...\n")
        fix_prompt = f"""
The following multi-file Python project has errors.

ERROR:
{result["stderr"]}

PROJECT JSON:
{json.dumps(project_data)}

Fix the project.
Return ONLY corrected JSON in the SAME FORMAT.
"""
        raw_response = get_code(system_prompt, fix_prompt)
        project_data = json.loads(raw_response)
        project_path = save_project(project_data)
        attempts += 1

if __name__ == "__main__":
    main()

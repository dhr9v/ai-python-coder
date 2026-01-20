# AI Code Generator Agent 

An autonomous Python-based AI agent that generates, executes, and self-fixes code projects from natural language prompts.

This project demonstrates how modern AI coding agents work internally — including multi-file project generation, runtime execution, error detection, and automatic fixing using LLMs.

---

## Features

- Natural language → Python code
- Multi-file project generation
- Automatic execution of generated code
- Self-healing loop (detects errors, sends traceback back to AI, regenerates fixed code)
- Safe execution handling (timeouts, input detection)
- Project-level regeneration instead of single-file hacks



## Architecture Overview
```

aicodegen/
│
├── main.py              # Orchestrates generation, execution, fixing
├── llm.py               # Handles LLM (Gemini) interaction
├── runner.py            # Executes generated code safely
├── writer.py            # Writes single & multi-file projects
├── system_prompt.txt    # Base system instructions for AI
│
└── generated_projects/  # AI-generated project outputs


```
## How It Works

1. User enters a natural language prompt
2. The prompt is combined with a system developer prompt
3. AI returns a strict JSON project structure
4. Files are written to disk automatically
5. The entry file is executed
6. If an error occurs:
   - Traceback is captured
   - Sent back to AI
   - AI regenerates a fixed version
   - Project is re-run (limited retries)

This loop mimics how real autonomous coding agents operate.

---

## AI Output Format (Strict)
```
The AI is instructed to return only valid JSON:

{
  "project_name": "example_project",
  "entry_file": "main.py",
  "files": {
    "main.py": "FULL CODE",
    "utils.py": "FULL CODE"
  }
}

- No markdown
- No explanations
- Only valid JSON

```
---

## Running the Project

1. Create & activate virtual environment
```
Windows:
python -m venv .venv
.venv\Scripts\activate

Linux / macOS:
python -m venv .venv
source .venv/bin/activate
```
2. Install dependencies
```
pip install google-genai
```
3. Set Gemini API key
```
Windows (PowerShell):
setx GEMINI_API_KEY "YOUR_API_KEY"

Linux / macOS:
export GEMINI_API_KEY="YOUR_API_KEY"
```
Restart the terminal after setting the key.

4. Run the agent
```
python main.py
```
```
Example prompt:
Create a multi-file Python task manager using JSON storage
```
---

## Safety Notes

- Generated code is executed locally — do not run untrusted prompts
- Programs requiring user input are detected and skipped from auto-run
- Timeouts prevent infinite loops or hanging executions

Future improvements may include sandboxing or Docker isolation.

---

## License

MIT License

---

## Author

Built by Dhruv Jain.
Exploring AI agents, automation, and applied machine learning

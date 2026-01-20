import subprocess
import sys
import os

def run_file(project_path, entry_file, timeout=10):
    try:
        result = subprocess.run(
            [sys.executable, entry_file],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": "Execution timed out.",
            "returncode": -1
        }

def requires_input(code: str) -> bool:
    return "input(" in code

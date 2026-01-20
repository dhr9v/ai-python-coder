import os

BASE_DIR = "generated_projects"

def save_project(project_data):
    project_name = project_data["project_name"]
    files = project_data["files"]

    project_path = os.path.join(BASE_DIR, project_name)
    os.makedirs(project_path, exist_ok=True)

    for filename, content in files.items():
        file_path = os.path.join(project_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    return project_path

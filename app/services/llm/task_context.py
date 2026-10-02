from app.services.memory import get_memory
from typing import Dict, Any


def build_task_prompt(task: dict, shared_memory: Dict[str, Any] = None) -> str:
    """Build a detailed prompt for the LLM based on task and context."""
    prompt = f"Task: {task['name']}\n"
    prompt += f"Task ID: {task['task_id']}\n"
    prompt += f"Capability: {task['capability']}\n\n"
    
    if task.get("description"):
        prompt += f"Description: {task['description']}\n\n"
    
    if shared_memory and shared_memory.get("data"):
        prompt += "Context from previous tasks:\n"
        for key, value in shared_memory["data"].items():
            if isinstance(value, dict):
                prompt += f"- {key}: {value}\n"
            else:
                prompt += f"- {key}: {value}\n"
        prompt += "\n"
    
    if task.get("input_data"):
        prompt += "Input data:\n"
        for key, value in task["input_data"].items():
            prompt += f"- {key}: {value}\n"
        prompt += "\n"
    
    prompt += "Please provide a detailed and structured response."
    return prompt


def extract_facts(text: str) -> list[str]:
    """Extract key facts from LLM response."""
    lines = text.split("\n")
    facts = [line.strip() for line in lines if line.strip() and len(line.strip()) > 10]
    return facts[:5]


def extract_files(text: str) -> list[str]:
    """Extract file names from code generation response."""
    files = []
    for line in text.split("\n"):
        if ".py" in line or ".js" in line or ".ts" in line:
            file_name = line.split()[-1] if line.split() else None
            if file_name and (file_name.endswith(".py") or file_name.endswith(".js") or file_name.endswith(".ts")):
                files.append(file_name)
    return files if files else ["implementation.py", "service.py"]


def extract_takeaways(text: str) -> list[str]:
    """Extract key takeaways from summary."""
    lines = text.split("\n")
    takeaways = []
    for line in lines:
        if line.strip().startswith(("- ", "* ", "1.", "2.", "3.")):
            takeaways.append(line.strip())
    return takeaways[:3] if takeaways else ["Key insight from analysis"]

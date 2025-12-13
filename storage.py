import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from tasks.json. If file doesn't exist, return empty list."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # Ensure it's the correct type
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks list into tasks.json."""
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

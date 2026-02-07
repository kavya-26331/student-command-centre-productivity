import json
import os
from datetime import datetime, timedelta

TODO_FILE = "data/todos.json"


def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        return []


def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)


def add_task(task_name):
    """Add a new task with timestamp."""
    todos = load_todos()
    todos.append({
        "task": task_name,
        "completed": False,
        "added_at": datetime.now().isoformat()
    })
    save_todos(todos)
    return todos


def remove_completed_tasks():
    """Delete only tasks marked completed."""
    todos = load_todos()
    todos = [t for t in todos if not t["completed"]]
    save_todos(todos)
    return todos


def mark_task_completed(task_name):
    """Mark a task as completed."""
    todos = load_todos()
    for t in todos:
        if t["task"] == task_name:
            t["completed"] = True
    save_todos(todos)
    return todos


def get_pending_reminder():
    """
    Returns reminder message if tasks are pending.
    If tasks were added more than 1 hour ago → stronger reminder.
    """

    todos = load_todos()
    pending = [t for t in todos if not t["completed"]]

    if not pending:
        return None  # No reminder needed

    # Basic reminder
    message = f"🔔 You still have {len(pending)} pending task(s). Stay productive!"

    # Check if tasks are old (1 hour)
    now = datetime.now()

    for p in pending:
        added_time = datetime.fromisoformat(p["added_at"])
        if now - added_time > timedelta(hours=1):
            return (
                "⏰ **Reminder! Some tasks are pending for more than 1 hour.**\n"
                "Please complete them soon!"
            )

    return message




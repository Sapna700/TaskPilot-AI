from .tools import get_available_tools
from .prompts import SYSTEM_PROMPT


class TaskPilot:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task added: {task}"

    def view_tasks(self):
        if not self.tasks:
            return "No tasks available."

        return "\n".join(
            f"{index + 1}. {task}"
            for index, task in enumerate(self.tasks)
        )

    def complete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            return "Invalid task number."

        completed_task = self.tasks.pop(task_number - 1)
        return f"Task completed: {completed_task}"

    def get_tools(self):
        return get_available_tools()

from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT
from tools import get_available_tools


class TaskPilot:
    def __init__(self):
        self.tasks = []
        self.client = OpenAI(api_key=OPENAI_API_KEY)

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

    def ask_ai(self, user_message):
        response = self.client.responses.create(
            model=MODEL_NAME,
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.output_text

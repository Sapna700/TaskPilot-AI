from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT
from tools import get_available_tools


class TaskPilot:
    def __init__(self):
        self.tasks = []
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def add_task(self, task, priority="medium"):
        """
        Add a new task with priority level.
        Priority can be: 'high', 'medium', 'low'
        """
        if priority not in ['high', 'medium', 'low']:
            return "Error: Invalid priority. Use: high, medium, or low"
        
        task_dict = {
            "title": task,
            "priority": priority.lower(),
            "completed": False
        }
        
        self.tasks.append(task_dict)
        return f"Task added: {task} (Priority: {priority.capitalize()})"

    def view_tasks(self, show_completed=False):
        """
        View all tasks with their priority levels.
        """
        if not self.tasks:
            return "No tasks available."
        
        tasks_to_show = self.tasks
        if not show_completed:
            tasks_to_show = [t for t in self.tasks if not t.get('completed', False)]
        
        if not tasks_to_show:
            return "All tasks completed."
        
        priority_labels = {
            'high': '[HIGH]',
            'medium': '[MEDIUM]',
            'low': '[LOW]'
        }
        
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        sorted_tasks = sorted(tasks_to_show, key=lambda x: priority_order.get(x.get('priority', 'medium'), 1))
        
        output_lines = []
        for i, task in enumerate(sorted_tasks, 1):
            title = task['title']
            priority = task.get('priority', 'medium')
            priority_display = priority_labels.get(priority, '[MEDIUM]')
            status = "[DONE]" if task.get('completed') else "[ ]"
            output_lines.append(f"{i}. {status} {priority_display} - {title}")
        
        return "\n".join(output_lines)

    def complete_task(self, task_number):
        """
        Mark a task as completed.
        """
        if task_number < 1 or task_number > len(self.tasks):
            return "Error: Invalid task number."
        
        task = self.tasks[task_number - 1]
        task['completed'] = True
        return f"Task completed: {task['title']}"

    def set_priority(self, task_number, new_priority):
        """
        Change priority of an existing task.
        """
        if new_priority not in ['high', 'medium', 'low']:
            return "Error: Invalid priority. Use: high, medium, or low"
        
        if task_number < 1 or task_number > len(self.tasks):
            return "Error: Invalid task number."
        
        task = self.tasks[task_number - 1]
        old_priority = task.get('priority', 'medium')
        task['priority'] = new_priority
        return f"Priority updated for '{task['title']}': {old_priority.capitalize()} -> {new_priority.capitalize()}"

    def sort_tasks(self):
        """
        Sort tasks by priority (High > Medium > Low).
        """
        if not self.tasks:
            return "No tasks to sort."
        
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        self.tasks.sort(key=lambda x: priority_order.get(x.get('priority', 'medium'), 1))
        return "Tasks sorted by priority."

    def get_priority_summary(self):
        """
        Get a summary of task priorities.
        """
        if not self.tasks:
            return "No tasks to analyze."
        
        priority_counts = {'high': 0, 'medium': 0, 'low': 0}
        for task in self.tasks:
            if not task.get('completed', False):
                priority = task.get('priority', 'medium')
                priority_counts[priority] += 1
        
        total_active = sum(priority_counts.values())
        
        if total_active == 0:
            return "All tasks completed."
        
        summary_lines = []
        if priority_counts['high'] > 0:
            summary_lines.append(f"High priority: {priority_counts['high']} tasks")
        if priority_counts['medium'] > 0:
            summary_lines.append(f"Medium priority: {priority_counts['medium']} tasks")
        if priority_counts['low'] > 0:
            summary_lines.append(f"Low priority: {priority_counts['low']} tasks")
        
        return "\n".join(summary_lines)

    def get_tools(self):
        return get_available_tools()

    def ask_ai(self, user_message):
        task_context = self.view_tasks() if self.tasks else "No tasks available."
        priority_summary = self.get_priority_summary()
        
        enhanced_prompt = f"{SYSTEM_PROMPT}\n\nCurrent tasks:\n{task_context}\n\nPriority summary:\n{priority_summary}"
        
        response = self.client.responses.create(
            model=MODEL_NAME,
            input=[
                {
                    "role": "system",
                    "content": enhanced_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        
        return response.output_text
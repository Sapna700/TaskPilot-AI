class TaskPoilt:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)
    return f"Task added: {task}"

   def show_tasks(self):
     if not self.tasks:
       return"No task found."

   return "\n".join(
     f"{i+1}. {task}"
     for i, task in
enumerate(self.tasks)
   )

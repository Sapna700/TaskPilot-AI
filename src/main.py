from agent import TaskPilot

agent = TaskPilot()

while True:
    command = input("You: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    elif command.lower().startswith("add "):
        task = command[4:]
        print(agent.add_task(task))

    elif command.lower() == "tasks":
        print(agent.show_tasks())

    else:
        print("Try: add <task> or tasks")


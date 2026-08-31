from agent import TaskPilot

agent = TaskPilot()

print("Welcome to TaskPilot AI!")
print("Commands: add <task>, tasks, complete <number>, tools, exit")

while True:
    command = input("\nYou: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    elif command.lower().startswith("add "):
        task = command[4:]
        print(agent.add_task(task))

    elif command.lower() == "tasks":
        print(agent.view_tasks())

    elif command.lower().startswith("complete "):
        try:
            task_number = int(command.split()[1])
            print(agent.complete_task(task_number))
        except (IndexError, ValueError):
            print("Please enter a valid task number.")

    elif command.lower() == "tools":
        print(agent.get_tools())

    else:
        print("Try: add <task>, tasks, complete <number>, tools, or exit")

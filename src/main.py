from agent import TaskPilot

agent = TaskPilot()

print("=" * 50)
print("TaskPilot AI - Task Management System")
print("=" * 50)
print("\nCommands:")
print("  add <task> [--priority high|medium|low]  - Add a new task")
print("  tasks                                     - View all tasks")
print("  complete <number>                         - Complete a task")
print("  priority <number> <high|medium|low>       - Change task priority")
print("  sort                                      - Sort tasks by priority")
print("  summary                                   - Show priority summary")
print("  tools                                     - Show available tools")
print("  ai <your question>                        - Ask TaskPilot AI")
print("  exit                                      - Exit the application")
print("\n" + "-" * 50)

while True:
    command = input("\nYou: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    elif command.lower().startswith("add "):
        parts = command[4:].split()
        task_parts = []
        priority = "medium"
        
        i = 0
        while i < len(parts):
            if parts[i] == "--priority" and i + 1 < len(parts):
                priority = parts[i + 1].lower()
                i += 2
            else:
                task_parts.append(parts[i])
                i += 1
        
        task = " ".join(task_parts)
        print(agent.add_task(task, priority))

    elif command.lower() == "tasks":
        print("\nYour Tasks:")
        print("-" * 50)
        print(agent.view_tasks())

    elif command.lower().startswith("complete "):
        try:
            task_number = int(command.split()[1])
            print(agent.complete_task(task_number))
        except (IndexError, ValueError):
            print("Error: Please enter a valid task number. Example: complete 1")

    elif command.lower().startswith("priority "):
        parts = command.split()
        if len(parts) >= 3:
            try:
                task_number = int(parts[1])
                new_priority = parts[2].lower()
                print(agent.set_priority(task_number, new_priority))
            except ValueError:
                print("Error: Please use: priority <task_number> <level>")
        else:
            print("Error: Please use: priority <task_number> <level>")

    elif command.lower() == "sort":
        print(agent.sort_tasks())
        print("\nSorted Tasks:")
        print(agent.view_tasks())

    elif command.lower() == "summary":
        print("\nPriority Summary:")
        print("-" * 30)
        print(agent.get_priority_summary())

    elif command.lower() == "tools":
        print("\nAvailable Tools:")
        tools = agent.get_tools()
        for tool_name, tool_desc in tools.items():
            print(f"  - {tool_name}: {tool_desc}")

    elif command.lower().startswith("ai "):
        message = command[3:]
        print("\nTaskPilot AI Response:")
        print("-" * 40)
        print(agent.ask_ai(message))

    else:
        print("Unknown command. Try: add, tasks, complete, priority, sort, summary, tools, ai, or exit")
# TaskPilot-AI

An open-source AI task agent built with Python that helps you manage and organize your tasks efficiently through an interactive command-line interface powered by artificial intelligence.

## Features

- ✅ **Task Management** — Add, view, and organize tasks easily
- 🤖 **AI Integration** — Powered by OpenAI's API for intelligent task handling
- 💻 **CLI Interface** — Simple and intuitive command-line interaction
- 🔧 **Extensible** — Easy to extend with new features and capabilities
- 📝 **Lightweight** — Minimal dependencies, fast and efficient
- 🆓 **Open Source** — MIT licensed, contributions welcome

## Prerequisites

Before you begin, ensure you have:
- Python 3.7 or higher installed
- An OpenAI API key (get one at [platform.openai.com](https://platform.openai.com))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sapna700/TaskPilot-AI.git
   cd TaskPilot-AI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```

4. **Add your OpenAI API key:**
   Edit the `.env` file and replace `your_api_key_here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Quick Start

Run the application:
```bash
python src/main.py
```

You'll see an interactive prompt. Here are the available commands:

### Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <task>` | Add a new task | `add Buy groceries` |
| `tasks` | Display all tasks | `tasks` |
| `complete <number>` | Mark a task as complete | `complete 1` |
| `ai <question>` | Ask AI a question | `ai How should I prioritize my tasks?` |
| `exit` | Exit the application | `exit` |

### Example Usage

```
Welcome to TaskPilot AI!
Commands:
add <task>
tasks
complete <number>
ai <your question>
exit

You: add Complete project proposal
Task added: Complete project proposal

You: add Review pull requests
Task added: Review pull requests

You: tasks
1. Complete project proposal
2. Review pull requests

You: ai What should I do first?
TaskPilot AI:
Based on your tasks, I recommend starting with the project proposal as it's often time-sensitive...

You: complete 1
Task completed: Complete project proposal

You: exit
Goodbye!
```

## Project Structure

```
TaskPilot-AI/
├── src/
│   ├── agent.py          # TaskPilot agent class with task management and AI logic
│   └── main.py           # CLI entry point and interactive loop
├── requirements.txt      # Python dependencies
├── .env.example         # Example environment configuration
├── CONTRIBUTING.md      # Contribution guidelines
├── LICENSE              # MIT License
└── README.md           # This file
```

## How It Works

1. **Agent Class** (`src/agent.py`) — Manages task storage and AI interactions
   - `add_task(task)` — Adds a new task to the list
   - `view_tasks()` — Displays all stored tasks
   - `complete_task(task_number)` — Marks a task as complete
   - `ask_ai(user_message)` — Sends questions to OpenAI API for intelligent responses

2. **Main CLI** (`src/main.py`) — Provides user interaction
   - Accepts user commands in an interactive loop
   - Routes commands to the appropriate agent methods
   - Displays AI responses and task updates
   - Provides user-friendly feedback

## Technologies Used

- **Python 3** — Core programming language
- **OpenAI API** — AI-powered task intelligence and suggestions
- **python-dotenv** — Environment variable management

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes and test them
4. Commit your changes (`git commit -m 'Add your feature'`)
5. Push to your branch (`git push origin feature/your-feature`)
6. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## Roadmap

- [x] Basic task management (add, view, complete)
- [x] OpenAI API integration
- [ ] Task persistence (save to database/file)
- [ ] Task prioritization levels
- [ ] Due date support
- [ ] Task categorization/tagging
- [ ] Advanced AI features (task suggestions, auto-completion)
- [ ] Web UI interface
- [ ] API server mode
- [ ] Task scheduling and reminders

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/Sapna700/TaskPilot-AI/issues) page
2. Create a new issue with detailed information
3. Include your Python version and error messages

## Author

[Sapna700](https://github.com/Sapna700)

---

**Happy task management! 🚀**

import pytest
from src.agent import TaskPilot


@pytest.fixture
def agent():
    """Fixture to create a TaskPilot agent instance for testing."""
    return TaskPilot()


class TestTaskPilotInitialization:
    """Test TaskPilot initialization."""
    
    def test_agent_initializes_with_empty_tasks(self, agent):
        """Test that a new agent has an empty task list."""
        assert agent.tasks == []


class TestAddTask:
    """Test task addition functionality."""
    
    def test_add_single_task(self, agent):
        """Test adding a single task."""
        result = agent.add_task("Buy groceries")
        assert result == "Task added: Buy groceries"
        assert len(agent.tasks) == 1
        assert agent.tasks[0] == "Buy groceries"
    
    def test_add_multiple_tasks(self, agent):
        """Test adding multiple tasks."""
        agent.add_task("Task 1")
        agent.add_task("Task 2")
        agent.add_task("Task 3")
        assert len(agent.tasks) == 3
        assert agent.tasks == ["Task 1", "Task 2", "Task 3"]


class TestViewTasks:
    """Test viewing tasks functionality."""
    
    def test_view_empty_tasks(self, agent):
        """Test viewing tasks when list is empty."""
        result = agent.view_tasks()
        assert result == "No tasks available."
    
    def test_view_single_task(self, agent):
        """Test viewing a single task."""
        agent.add_task("Buy milk")
        result = agent.view_tasks()
        assert result == "1. Buy milk"
    
    def test_view_multiple_tasks(self, agent):
        """Test viewing multiple tasks."""
        agent.add_task("Task 1")
        agent.add_task("Task 2")
        agent.add_task("Task 3")
        result = agent.view_tasks()
        expected = "1. Task 1\n2. Task 2\n3. Task 3"
        assert result == expected


class TestCompleteTask:
    """Test task completion functionality."""
    
    def test_complete_valid_task(self, agent):
        """Test completing a valid task."""
        agent.add_task("Task 1")
        agent.add_task("Task 2")
        result = agent.complete_task(1)
        assert result == "Task completed: Task 1"
        assert len(agent.tasks) == 1
        assert agent.tasks[0] == "Task 2"
    
    def test_complete_last_task(self, agent):
        """Test completing the last task."""
        agent.add_task("Only task")
        result = agent.complete_task(1)
        assert result == "Task completed: Only task"
        assert len(agent.tasks) == 0
    
    def test_complete_invalid_task_number_too_high(self, agent):
        """Test completing task with number higher than list size."""
        agent.add_task("Task 1")
        result = agent.complete_task(5)
        assert result == "Invalid task number."
        assert len(agent.tasks) == 1
    
    def test_complete_invalid_task_number_zero(self, agent):
        """Test completing task with number 0."""
        agent.add_task("Task 1")
        result = agent.complete_task(0)
        assert result == "Invalid task number."
        assert len(agent.tasks) == 1
    
    def test_complete_invalid_task_number_negative(self, agent):
        """Test completing task with negative number."""
        agent.add_task("Task 1")
        result = agent.complete_task(-1)
        assert result == "Invalid task number."
        assert len(agent.tasks) == 1

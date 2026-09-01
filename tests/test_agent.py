import pytest
from src.agent import TaskPilot


@pytest.fixture
def agent():
    return TaskPilot()


class TestPriorityFeatures:
    def test_add_task_with_priority(self, agent):
        result = agent.add_task("High task", "high")
        assert "Priority: High" in result
        assert len(agent.tasks) == 1
        assert agent.tasks[0]['priority'] == 'high'
        assert agent.tasks[0]['title'] == 'High task'
    
    def test_add_task_default_priority(self, agent):
        result = agent.add_task("Default task")
        assert "Priority: Medium" in result
        assert agent.tasks[0]['priority'] == 'medium'
    
    def test_invalid_priority(self, agent):
        result = agent.add_task("Invalid task", "urgent")
        assert "Invalid priority" in result
        assert len(agent.tasks) == 0
    
    def test_view_tasks_with_priorities(self, agent):
        agent.add_task("Task 1", "high")
        agent.add_task("Task 2", "medium")
        agent.add_task("Task 3", "low")
        
        result = agent.view_tasks()
        assert "[HIGH]" in result
        assert "[MEDIUM]" in result
        assert "[LOW]" in result
    
    def test_set_priority(self, agent):
        agent.add_task("Test task", "medium")
        result = agent.set_priority(1, "high")
        assert "Priority updated" in result
        assert agent.tasks[0]['priority'] == 'high'
    
    def test_sort_tasks(self, agent):
        agent.add_task("Low task", "low")
        agent.add_task("High task", "high")
        agent.add_task("Medium task", "medium")
        
        result = agent.sort_tasks()
        assert "sorted" in result.lower()
        assert agent.tasks[0]['priority'] == 'high'
        assert agent.tasks[1]['priority'] == 'medium'
        assert agent.tasks[2]['priority'] == 'low'
    
    def test_complete_task(self, agent):
        agent.add_task("Test task", "high")
        result = agent.complete_task(1)
        assert "completed" in result.lower()
        assert agent.tasks[0]['completed'] == True
    
    def test_priority_summary(self, agent):
        agent.add_task("Task 1", "high")
        agent.add_task("Task 2", "medium")
        
        result = agent.get_priority_summary()
        assert "High priority: 1" in result
        assert "Medium priority: 1" in result
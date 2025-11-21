import pytest
from unittest.mock import MagicMock
from university_research_crew import create_university_research_crew

def test_validator_agent_delegation_enabled():
    """
    Tests that the validator_agent is configured with allow_delegation=True.
    """
    # Create the crew with dummy inputs
    crew = create_university_research_crew(country="Testland", program="Test Studies")

    # Find the validator agent in the crew
    validator_agent = None
    for agent in crew.agents:
        if agent.role == 'Report Validator':
            validator_agent = agent
            break

    # Assert that the validator agent exists and has delegation enabled
    assert validator_agent is not None, "Validator agent not found in crew"
    assert validator_agent.allow_delegation is True, "Validator agent should have allow_delegation set to True"

def test_validation_task_has_delegation_instructions():
    """
    Tests that the validation_task description includes instructions for delegation.
    """
    crew = create_university_research_crew(country="Testland", program="Test Studies")

    # Find the validation task
    validation_task = None
    for task in crew.tasks:
        if "Review the curriculum report" in task.description:
            validation_task = task
            break

    # Assert that the task description contains delegation-related keywords
    assert validation_task is not None, "Validation task not found in crew"
    assert "delegate" in validation_task.description.lower(), "Task description should include delegation instructions"
    assert "if deficiencies are found" in validation_task.description.lower(), "Task description should specify when to delegate"

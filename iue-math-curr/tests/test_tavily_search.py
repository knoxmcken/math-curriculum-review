import pytest
from university_research_crew import create_university_research_crew
from crewai_tools import TavilySearchTool


def test_web_search_agent_uses_tavily_tool():
    """
    Tests that the web_search_agent is configured with TavilySearchTool.
    """
    # Create the crew with dummy inputs
    crew = create_university_research_crew(country="Testland", program="Test Studies")

    # Find the web search agent in the crew
    web_search_agent = None
    for agent in crew.agents:
        if agent.role == 'University Program Researcher':
            web_search_agent = agent
            break

    # Assert that the web search agent exists
    assert web_search_agent is not None, "Web search agent not found in crew"

    # Check that one of the agent's tools is an instance of TavilySearchTool
    assert any(isinstance(tool, TavilySearchTool) for tool in web_search_agent.tools), \
        "Web search agent should have TavilySearchTool"

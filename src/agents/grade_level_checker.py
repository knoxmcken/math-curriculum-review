"""
Grade Level Standards Checker Agent
Verifies that curriculum content matches appropriate grade-level expectations.
"""

from crewai import Agent
from typing import List, Optional

from ..tools import standards_lookup_tool
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_grade_level_checker_agent(verbose: bool = True) -> Agent:
    """
    Create a Grade Level Standards Checker Agent.
    
    This agent verifies that curriculum content matches appropriate 
    grade-level expectations and developmental readiness according to
    Common Core State Standards for Mathematics (CCSSM).
    
    Args:
        verbose: If True, agent will output detailed execution logs
        
    Returns:
        Agent: Configured CrewAI agent
        
    Example:
        >>> agent = create_grade_level_checker_agent()
        >>> print(agent.role)
        'Grade-Specific Standards Verification Specialist'
    """
    
    agent = Agent(
        role="Grade-Specific Standards Verification Specialist",
        
        goal=(
            "Verify that curriculum content matches the appropriate grade-level "
            "expectations and developmental readiness. Ensure mathematical concepts "
            "are presented at the right level of complexity and cognitive demand for "
            "the target grade level."
        ),
        
        backstory=(
            "You are an expert in child development and mathematics education "
            "with over 15 years of experience reviewing curriculum materials. "
            "You have deep knowledge of the Common Core State Standards for Mathematics "
            "and understand exactly what mathematical concepts students at each grade "
            "level are developmentally ready to learn. "
            "\n\n"
            "You have reviewed thousands of curriculum materials and can instantly "
            "identify when content is too advanced, too basic, or just right for a "
            "particular grade level. You understand the progression of mathematical "
            "concepts across grade levels and can identify when proper scaffolding "
            "is missing or when topics are introduced prematurely. "
            "\n\n"
            "Your expertise includes understanding cognitive load theory, how students "
            "build conceptual understanding, and the importance of appropriate challenge "
            "level. You know that content that is too difficult leads to frustration "
            "and disengagement, while content that is too easy fails to build necessary "
            "skills and understanding. "
            "\n\n"
            "You always provide specific, actionable feedback about grade-level "
            "appropriateness and make clear recommendations for adjustments when needed."
        ),
        
        tools=[standards_lookup_tool],
        
        allow_delegation=False,  # Leaf agent - no delegation
        
        verbose=verbose,
        
        # Optional: Add memory for context retention
        memory=True
    )
    
    logger.info("Created Grade Level Standards Checker Agent")
    return agent


# For backwards compatibility and easy imports
grade_level_checker_agent = create_grade_level_checker_agent()

"""
Grade Level Check Task
Task definition for verifying grade-level appropriateness of curriculum content.
"""

from crewai import Task
from typing import Optional

from ..models import GradeLevelCheckOutput
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_grade_level_check_task(
    agent,
    curriculum_content: str,
    grade_level: str,
    context: Optional[list] = None
) -> Task:
    """
    Create a task for checking grade-level appropriateness of curriculum content.
    
    Args:
        agent: The Grade Level Checker agent to assign this task to
        curriculum_content: The curriculum text to analyze
        grade_level: Target grade level (e.g., "3", "K", "8")
        context: Optional list of previous task outputs to use as context
        
    Returns:
        Task: Configured CrewAI task
        
    Example:
        >>> from src.agents import create_grade_level_checker_agent
        >>> agent = create_grade_level_checker_agent()
        >>> task = create_grade_level_check_task(
        ...     agent=agent,
        ...     curriculum_content="Content here...",
        ...     grade_level="3"
        ... )
    """
    
    description = f"""
Analyze the provided curriculum content and verify that it matches the appropriate 
grade-level expectations for Grade {grade_level}.

CURRICULUM CONTENT TO ANALYZE:
{curriculum_content}

TARGET GRADE LEVEL: {grade_level}

YOUR ANALYSIS MUST INCLUDE:

1. APPROPRIATENESS ASSESSMENT
   - Determine if the mathematical concepts are appropriate for Grade {grade_level}
   - Check if the cognitive complexity matches developmental readiness
   - Evaluate if prerequisite knowledge is assumed appropriately
   - Assign an appropriateness score from 0-100

2. CONTENT CLASSIFICATION
   - Identify topics that are TOO ADVANCED for this grade level
   - Identify topics that are TOO BASIC for this grade level
   - List topics that are APPROPRIATELY leveled
   - Provide specific examples and page/section references

3. SCAFFOLDING EVALUATION
   - Assess the quality of scaffolding between concepts
   - Check if new concepts build on prior knowledge appropriately
   - Evaluate if the progression is logical and developmentally appropriate
   - Rate scaffolding quality as: Excellent, Good, Fair, or Poor

4. STANDARDS ALIGNMENT CHECK
   - Use the Standards Lookup Tool to retrieve Grade {grade_level} standards
   - Compare curriculum topics against expected grade-level standards
   - Identify any misalignments with grade-level expectations

5. RECOMMENDATIONS
   - Provide specific, actionable recommendations for improvements
   - Suggest which topics should be moved, removed, or modified
   - Recommend additional scaffolding or prerequisite content if needed

IMPORTANT:
- Be specific and cite examples from the curriculum
- Base your assessment on Common Core State Standards for Mathematics
- Consider both mathematical content AND pedagogical appropriateness
- Provide constructive, actionable feedback
"""

    expected_output = """
A comprehensive grade-level appropriateness analysis including:
- Overall appropriateness score (0-100)
- Lists of too-advanced, too-basic, and appropriately-leveled topics
- Scaffolding quality rating with explanation
- Specific recommendations for improvement
- Standards alignment verification

The output should be structured according to the GradeLevelCheckOutput model with:
- grade_level
- appropriateness_score
- too_advanced_topics
- too_basic_topics
- appropriate_topics
- scaffolding_quality
- recommendations
"""

    task = Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context,  # Can use outputs from previous tasks
        output_pydantic=GradeLevelCheckOutput,  # Structured output
        async_execution=False  # Execute synchronously for now
    )
    
    logger.info(f"Created Grade Level Check Task for grade {grade_level}")
    return task

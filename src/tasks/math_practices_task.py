"""
Mathematical Practices Evaluation Task
Task definition for evaluating the 8 Standards for Mathematical Practice.
"""

from crewai import Task
from typing import Optional

from ..models import MathPracticesOutput
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_math_practices_task(
    agent,
    curriculum_content: str,
    grade_level: str,
    context: Optional[list] = None
) -> Task:
    """
    Create a task for evaluating mathematical practices in curriculum content.
    
    Args:
        agent: The Mathematical Practices Evaluator agent to assign this task to
        curriculum_content: The curriculum text to analyze
        grade_level: Target grade level (e.g., "3", "K", "8")
        context: Optional list of previous task outputs to use as context
        
    Returns:
        Task: Configured CrewAI task
        
    Example:
        >>> from src.agents import create_math_practices_evaluator_agent
        >>> agent = create_math_practices_evaluator_agent()
        >>> task = create_math_practices_task(
        ...     agent=agent,
        ...     curriculum_content="Content here...",
        ...     grade_level="3"
        ... )
    """
    
    description = f"""
Analyze the provided Grade {grade_level} curriculum content and evaluate how well it 
develops the 8 Standards for Mathematical Practice (MP1-MP8).

CURRICULUM CONTENT TO ANALYZE:
{curriculum_content}

TARGET GRADE LEVEL: {grade_level}

FIRST, use the Standards Lookup Tool to retrieve the complete list of the 8 Mathematical 
Practices by querying 'practices'. Study each practice carefully.

YOUR COMPREHENSIVE EVALUATION MUST INCLUDE:

1. INDIVIDUAL PRACTICE SCORES (MP1-MP8)
   For EACH of the 8 Mathematical Practices, assign a score from 0-100 based on:
   - How frequently the practice appears in the curriculum
   - The quality and depth of opportunities to develop the practice
   - The appropriateness of the practice for Grade {grade_level}
   - Whether the practice is integrated authentically or superficially
   
   The 8 practices you must evaluate:
   MP1: Make sense of problems and persevere in solving them
   MP2: Reason abstractly and quantitatively
   MP3: Construct viable arguments and critique reasoning of others
   MP4: Model with mathematics
   MP5: Use appropriate tools strategically
   MP6: Attend to precision
   MP7: Look for and make use of structure
   MP8: Look for and express regularity in repeated reasoning

2. OVERALL MATHEMATICAL PRACTICES SCORE
   Calculate an overall score (0-100) that represents the curriculum's 
   effectiveness at developing mathematical practices holistically.

3. STRENGTHS ANALYSIS
   Identify and describe 3-5 specific strengths in how the curriculum 
   develops mathematical practices. Include:
   - Which practices are done particularly well
   - Specific examples from the curriculum (cite lessons, problems, activities)
   - Why these examples are effective

4. WEAKNESSES ANALYSIS
   Identify and describe 3-5 specific weaknesses or missed opportunities.
   Include:
   - Which practices are underdeveloped or missing
   - Specific gaps or problems in the curriculum
   - Impact of these weaknesses on student learning

5. PRACTICE OPPORTUNITIES MAPPING
   For EACH of the 8 practices, identify and list specific opportunities 
   where the curriculum develops that practice. Include:
   - Lesson names or section references
   - Specific problems or activities
   - Brief description of how the practice is developed
   
   Format as: {{
       "MP1": ["Lesson 1: Multi-step problem...", "Lesson 3: Challenge..."],
       "MP2": ["Unit 2: Abstract reasoning...", ...],
       ...
   }}

6. BALANCE AND INTEGRATION ASSESSMENT
   Evaluate:
   - Are all 8 practices given adequate attention?
   - Are practices integrated together or isolated?
   - Do practices appear throughout the curriculum or only in certain sections?
   - Is there appropriate progression in practice development?

7. RECOMMENDATIONS
   Provide 5-7 specific, actionable recommendations for:
   - Strengthening underdeveloped practices
   - Adding new opportunities for specific practices
   - Better integrating practices across lessons
   - Improving the quality or authenticity of practice development
   - Balancing practice coverage across the curriculum

IMPORTANT GUIDELINES:
- Be specific and cite examples with lesson/section references
- Base scores on both FREQUENCY and QUALITY of opportunities
- Consider grade-level appropriateness (Grade {grade_level})
- Distinguish authentic practice development from superficial mentions
- Provide evidence-based, actionable feedback
- Use the Mathematical Practices definitions from the Standards Lookup Tool
"""

    expected_output = """
A comprehensive mathematical practices evaluation including:
- Individual scores for all 8 practices (MP1-MP8) with explanations
- Overall mathematical practices score (0-100)
- 3-5 specific strengths with curriculum examples
- 3-5 specific weaknesses with identified gaps
- Detailed practice opportunities mapping for each of the 8 practices
- Balance and integration assessment
- 5-7 actionable recommendations for improvement

The output should be structured according to the MathPracticesOutput model with:
- practice_scores: Dictionary with scores for MP1-MP8
- overall_score: Overall effectiveness score
- strengths: List of specific strengths
- weaknesses: List of specific weaknesses
- practice_opportunities: Dictionary mapping each practice to specific examples
- recommendations: List of actionable improvements
"""

    task = Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context,
        output_pydantic=MathPracticesOutput,
        async_execution=False  # Execute synchronously
    )
    
    logger.info(f"Created Mathematical Practices Task for grade {grade_level}")
    return task

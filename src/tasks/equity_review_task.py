"""
Equity & Accessibility Review Task
Task definition for evaluating equity, inclusion, and accessibility.
"""

from crewai import Task
from typing import Optional

from ..models import EquityAccessibilityOutput
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_equity_review_task(
    agent,
    curriculum_content: str,
    grade_level: str,
    context: Optional[list] = None
) -> Task:
    """
    Create a task for reviewing equity and accessibility of curriculum content.
    
    Args:
        agent: The Equity Reviewer agent to assign this task to
        curriculum_content: The curriculum text to analyze
        grade_level: Target grade level (e.g., "3", "K", "8")
        context: Optional list of previous task outputs to use as context
        
    Returns:
        Task: Configured CrewAI task
        
    Example:
        >>> from src.agents import create_equity_reviewer_agent
        >>> agent = create_equity_reviewer_agent()
        >>> task = create_equity_review_task(
        ...     agent=agent,
        ...     curriculum_content="Content here...",
        ...     grade_level="3"
        ... )
    """
    
    description = f"""
Analyze the provided Grade {grade_level} curriculum content and conduct a comprehensive 
evaluation of its equity, inclusion, and accessibility.

CURRICULUM CONTENT TO ANALYZE:
{curriculum_content}

TARGET GRADE LEVEL: {grade_level}

YOUR COMPREHENSIVE EQUITY & ACCESSIBILITY EVALUATION MUST INCLUDE:

1. CULTURAL RESPONSIVENESS (Score 0-100)
   Evaluate cultural responsiveness and representation:
   - Diversity of names, contexts, and examples used
   - Representation of different cultures, ethnicities, and backgrounds
   - Avoidance of stereotypes and cultural bias
   - Inclusion of diverse mathematicians and cultural contributions
   - Connections to students' lived experiences
   - Cultural assumptions that may exclude students
   - Use of inclusive, affirming language
   
   Provide specific examples of what you find (both positive and problematic).

2. ACCESSIBILITY FOR STUDENTS WITH DISABILITIES (Score 0-100)
   Assess accessibility features and barriers:
   - Visual accessibility (for students with visual impairments)
   - Auditory accessibility (for students with hearing impairments)
   - Support for learning disabilities (dyslexia, dyscalculia)
   - Physical accessibility (fine motor considerations)
   - Attention and processing support (ADHD, processing disorders)
   - Cognitive accessibility (intellectual disabilities, autism)
   - Multiple means of representation and expression
   - Clear, uncluttered layouts
   - Alt text for images (if mentioned)
   - Flexibility in response methods
   
   Identify specific barriers and accessibility features.

3. ENGLISH LANGUAGE LEARNER (ELL) SUPPORT (Score 0-100)
   Evaluate support for ELL students:
   - Visual supports and graphic organizers
   - Vocabulary scaffolding and definitions
   - Sentence frames and language supports
   - Reduced linguistic complexity where appropriate
   - Multiple representations (reducing language dependence)
   - Cognates and language connections (if applicable)
   - Context clues and examples
   - Word walls or vocabulary lists
   - Language objectives alongside content objectives
   
   Note specific supports present and missing.

4. UNIVERSAL DESIGN FOR LEARNING (UDL) COMPLIANCE (Score 0-100)
   Assess alignment with UDL principles:
   
   **Multiple Means of REPRESENTATION:**
   - Options for perception (visual, auditory, tactile)
   - Options for language and symbols
   - Options for comprehension
   
   **Multiple Means of ACTION & EXPRESSION:**
   - Options for physical action
   - Options for expression and communication
   - Options for executive functions
   
   **Multiple Means of ENGAGEMENT:**
   - Options for recruiting interest
   - Options for sustaining effort and persistence
   - Options for self-regulation
   
   Evaluate how well each UDL principle is implemented.

5. OVERALL EQUITY & ACCESSIBILITY SCORE (Score 0-100)
   Calculate an overall score representing the curriculum's equity and accessibility.
   This should reflect the weighted average of the above components.

6. REPRESENTATION ANALYSIS (List 3-5 observations)
   Analyze representation in the curriculum:
   - Who is represented in examples, names, and contexts?
   - Who is missing or underrepresented?
   - Are representations stereotypical or authentic?
   - Do students from diverse backgrounds see themselves?
   - Are diverse contributions to mathematics acknowledged?

7. BARRIERS IDENTIFIED (List 5-7 specific barriers)
   Identify specific barriers that may prevent or hinder access:
   - Cultural barriers (assumptions, lack of relevance)
   - Language barriers (complex vocabulary, dense text)
   - Visual barriers (poor contrast, small text, no alt text)
   - Cognitive barriers (high cognitive load, lack of scaffolding)
   - Physical barriers (fine motor requirements)
   - Economic barriers (assumptions about resources)
   
   Each barrier should be specific and cite curriculum examples.

8. RECOMMENDATIONS (5-7 actionable recommendations)
   Provide specific recommendations for:
   - Improving cultural responsiveness and representation
   - Enhancing accessibility for students with disabilities
   - Strengthening ELL support
   - Better implementing UDL principles
   - Removing identified barriers
   - Making the curriculum more inclusive overall
   
   Each recommendation should be:
   - Specific and actionable
   - Evidence-based
   - Practical to implement
   - Linked to specific curriculum sections

EVALUATION GUIDELINES:
- Consider Grade {grade_level} context and age-appropriateness
- Base evaluations on research and best practices
- Cite specific examples from curriculum
- Be constructive and solution-focused
- Prioritize recommendations by impact
- Consider intersectionality (students with multiple identities)
- Evaluate through an asset-based lens (what students CAN do)
"""

    expected_output = """
A comprehensive equity and accessibility evaluation including:
- Cultural responsiveness score (0-100) with examples
- Accessibility score (0-100) with barriers identified
- ELL support score (0-100) with analysis
- UDL compliance score (0-100) across all principles
- Overall equity & accessibility score (0-100)
- 3-5 observations about representation
- 5-7 specific barriers identified with examples
- 5-7 actionable recommendations for improvement

The output should be structured according to the EquityAccessibilityOutput model with:
- cultural_responsiveness
- accessibility_score
- ell_support_score
- udl_compliance
- overall_equity_score
- representation_analysis
- barriers_identified
- recommendations
"""

    task = Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context,
        output_pydantic=EquityAccessibilityOutput,
        async_execution=False
    )
    
    logger.info(f"Created Equity Review Task for grade {grade_level}")
    return task

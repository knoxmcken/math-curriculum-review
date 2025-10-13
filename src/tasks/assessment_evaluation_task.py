"""
Assessment Quality Evaluation Task
Task definition for evaluating assessment quality and effectiveness.
"""

from crewai import Task
from typing import Optional

from ..models import AssessmentQualityOutput
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_assessment_evaluation_task(
    agent,
    curriculum_content: str,
    grade_level: str,
    context: Optional[list] = None
) -> Task:
    """
    Create a task for evaluating assessment quality in curriculum content.
    
    Args:
        agent: The Assessment Evaluator agent to assign this task to
        curriculum_content: The curriculum text to analyze
        grade_level: Target grade level (e.g., "3", "K", "8")
        context: Optional list of previous task outputs to use as context
        
    Returns:
        Task: Configured CrewAI task
        
    Example:
        >>> from src.agents import create_assessment_evaluator_agent
        >>> agent = create_assessment_evaluator_agent()
        >>> task = create_assessment_evaluation_task(
        ...     agent=agent,
        ...     curriculum_content="Content here...",
        ...     grade_level="3"
        ... )
    """
    
    description = f"""
Analyze the provided Grade {grade_level} curriculum content and conduct a comprehensive 
evaluation of its assessment quality and effectiveness.

CURRICULUM CONTENT TO ANALYZE:
{curriculum_content}

TARGET GRADE LEVEL: {grade_level}

YOUR COMPREHENSIVE ASSESSMENT EVALUATION MUST INCLUDE:

1. ALIGNMENT WITH CONTENT & STANDARDS (Score 0-100)
   Evaluate alignment between assessments and instruction:
   - Do assessment items match learning objectives?
   - Are assessments aligned with taught content?
   - Do items target appropriate cognitive levels?
   - Is there coverage of all major standards addressed?
   - Use Standards Lookup Tool to verify alignment
   - Are there gaps or mismatches?
   
   Cite specific examples of aligned or misaligned items.

2. QUESTION QUALITY (Score 0-100)
   Assess the quality of individual assessment items:
   - Clarity and precision of wording
   - Appropriate mathematical language
   - Absence of 'trick' questions or ambiguity
   - Quality of distractors (for multiple choice)
   - Depth of mathematical thinking required
   - Balance of procedural vs. conceptual questions
   - Grade-appropriate rigor and complexity
   
   Provide examples of high-quality and problematic items.

3. VARIETY OF ASSESSMENT TYPES (Score 0-100)
   Evaluate diversity in assessment approaches:
   - Range of item types (MC, short answer, extended response, performance)
   - Balance of formative and summative assessments
   - Ongoing monitoring vs. end-of-unit tests
   - Exit tickets, quick checks, observations
   - Projects, portfolios, authentic tasks
   - Self-assessment and peer assessment opportunities
   - Frequency and distribution of assessments
   
   List types of assessments present and missing.

4. VALIDITY (Score 0-100)
   Assess whether assessments measure what they claim:
   - Content validity (covers curriculum content)
   - Construct validity (measures mathematical understanding)
   - Face validity (appears to measure intended outcomes)
   - Appropriate cognitive demand
   - Items test understanding, not just memorization
   - Assessments distinguish between levels of understanding
   
   Identify validity strengths and concerns.

5. ACCESSIBILITY & FAIRNESS (Score 0-100)
   Evaluate assessment accessibility:
   - Language complexity appropriate for Grade {grade_level}
   - Cultural bias or insensitive content
   - Accessibility for students with disabilities
   - Fairness for English Language Learners
   - Multiple ways to demonstrate knowledge
   - Clear, unambiguous instructions
   - Accommodations that preserve construct
   
   Note accessibility features and barriers.

6. OVERALL ASSESSMENT QUALITY (Score 0-100)
   Calculate an overall score representing assessment system quality.
   Weight alignment and question quality most heavily.

7. ASSESSMENT TYPES INVENTORY
   List all types of assessments found in the curriculum:
   - Formative assessments (exit tickets, quick checks, etc.)
   - Summative assessments (unit tests, quizzes, etc.)
   - Performance tasks
   - Projects or portfolios
   - Self-assessments
   - Other assessment types
   
   For each type, note frequency and quality.

8. STRENGTHS (3-5 specific strengths)
   Identify what the assessment system does well:
   - Specific examples of high-quality items
   - Effective assessment types or approaches
   - Good alignment with standards
   - Innovative or exemplary practices
   
   Cite curriculum sections and specific assessments.

9. WEAKNESSES (3-5 specific weaknesses)
   Identify gaps and problems in assessments:
   - Missing assessment types
   - Poorly worded or confusing items
   - Misalignment with content or standards
   - Lack of variety or depth
   - Accessibility issues
   
   Provide specific examples and locations.

10. RECOMMENDATIONS (5-7 actionable recommendations)
    Provide specific recommendations for:
    - Improving alignment with standards and content
    - Enhancing question quality and rigor
    - Adding variety in assessment types
    - Strengthening validity and reliability
    - Improving accessibility and fairness
    - Better balancing formative and summative assessment
    
    Each recommendation should be:
    - Specific and actionable
    - Evidence-based
    - Practical for teachers
    - Prioritized by impact

EVALUATION GUIDELINES:
- Consider Grade {grade_level} developmental level
- Base evaluations on assessment best practices
- Use Standards Lookup Tool to verify standard alignment
- Cite specific assessment examples
- Distinguish quality from quantity (more isn't always better)
- Consider teacher workload and practicality
- Evaluate whether assessments support learning, not just measure it
"""

    expected_output = """
A comprehensive assessment quality evaluation including:
- Alignment score (0-100) with standards verification
- Question quality score (0-100) with item examples
- Variety score (0-100) with types inventory
- Validity score (0-100) with analysis
- Accessibility score (0-100) with barriers noted
- Overall assessment quality score (0-100)
- List of assessment types present in curriculum
- 3-5 specific strengths with examples
- 3-5 specific weaknesses with examples
- 5-7 actionable recommendations prioritized by impact

The output should be structured according to the AssessmentQualityOutput model with:
- alignment_score
- question_quality_score
- variety_score
- validity_score
- accessibility_score
- overall_quality
- assessment_types
- strengths
- weaknesses
- recommendations
"""

    task = Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context,
        output_pydantic=AssessmentQualityOutput,
        async_execution=False
    )
    
    logger.info(f"Created Assessment Evaluation Task for grade {grade_level}")
    return task

"""
Pedagogical Effectiveness Analysis Task
Task definition for evaluating teaching strategies and instructional design.
"""

from crewai import Task
from typing import Optional

from ..models import PedagogicalEffectivenessOutput
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_pedagogical_analysis_task(
    agent,
    curriculum_content: str,
    grade_level: str,
    context: Optional[list] = None
) -> Task:
    """
    Create a task for analyzing pedagogical effectiveness of curriculum content.
    
    Args:
        agent: The Pedagogical Analyst agent to assign this task to
        curriculum_content: The curriculum text to analyze
        grade_level: Target grade level (e.g., "3", "K", "8")
        context: Optional list of previous task outputs to use as context
        
    Returns:
        Task: Configured CrewAI task
        
    Example:
        >>> from src.agents import create_pedagogical_analyst_agent
        >>> agent = create_pedagogical_analyst_agent()
        >>> task = create_pedagogical_analysis_task(
        ...     agent=agent,
        ...     curriculum_content="Content here...",
        ...     grade_level="3"
        ... )
    """
    
    description = f"""
Analyze the provided Grade {grade_level} curriculum content and conduct a comprehensive 
evaluation of its pedagogical effectiveness and instructional design quality.

CURRICULUM CONTENT TO ANALYZE:
{curriculum_content}

TARGET GRADE LEVEL: {grade_level}

YOUR COMPREHENSIVE PEDAGOGICAL EVALUATION MUST INCLUDE:

1. INSTRUCTIONAL DESIGN QUALITY (Score 0-100)
   Evaluate the overall quality of instructional design:
   - Lesson structure and organization
   - Clarity of learning objectives
   - Logical flow and sequencing of concepts
   - Balance of teacher-led and student-centered activities
   - Integration of multiple lesson components
   - Alignment between objectives, activities, and assessments
   
   Provide specific examples and a score.

2. SCAFFOLDING QUALITY (Score 0-100)
   Assess how well the curriculum scaffolds learning:
   - Gradual Release of Responsibility (I do, We do, You do)
   - Support provided for new concepts vs. established skills
   - Bridges between prior knowledge and new learning
   - Appropriate cognitive load management
   - Removal of supports as students gain competence
   - Use of worked examples, guided practice, and independent practice
   
   Cite specific examples of effective or missing scaffolding.

3. DIFFERENTIATION (Score 0-100)
   Evaluate support for diverse learners:
   - Provisions for struggling students (intervention, reteaching)
   - Extensions and challenges for advanced learners
   - Multiple entry points to tasks
   - Varied instructional approaches (visual, verbal, kinesthetic)
   - Flexible grouping suggestions
   - Accommodations and modifications guidance
   
   Identify what differentiation exists and what's missing.

4. ENGAGEMENT STRATEGIES (Score 0-100)
   Analyze approaches to student engagement:
   - Real-world connections and relevance
   - Hands-on activities and manipulatives
   - Collaborative learning opportunities
   - Problem-based learning elements
   - Student choice and voice
   - Cognitive challenge and productive struggle
   - Use of games, technology, or engaging contexts
   
   Provide examples of engagement strategies used.

5. FORMATIVE ASSESSMENT (Score 0-100)
   Examine formative assessment opportunities:
   - Embedded checks for understanding
   - Exit tickets and quick assessments
   - Questioning strategies that reveal student thinking
   - Observation opportunities for teachers
   - Self-assessment and peer-assessment
   - Use of assessment to inform instruction
   - Frequency and variety of formative assessments
   
   Note specific formative assessment opportunities.

6. OVERALL PEDAGOGICAL EFFECTIVENESS (Score 0-100)
   Calculate an overall score representing the curriculum's pedagogical quality.
   This should reflect the weighted average of the above components.

7. TEACHING STRATEGIES IDENTIFICATION
   List and describe 5-7 specific teaching strategies used in the curriculum:
   - Name of strategy (e.g., "Think-Pair-Share", "Concrete-Representational-Abstract")
   - Where it appears in the curriculum
   - How well it's implemented
   - Its effectiveness for Grade {grade_level}

8. DETAILED RECOMMENDATIONS (5-7 specific recommendations)
   Provide actionable recommendations for:
   - Improving instructional design and lesson structure
   - Strengthening scaffolding and support
   - Enhancing differentiation for all learners
   - Increasing student engagement
   - Integrating more effective formative assessment
   - Implementing research-based teaching strategies
   
   Each recommendation should be:
   - Specific and actionable
   - Evidence-based
   - Practical for teachers to implement
   - Linked to specific curriculum sections

ANALYSIS GUIDELINES:
- Base evaluations on research-based best practices in mathematics education
- Cite specific lessons, activities, or sections as evidence
- Consider appropriateness for Grade {grade_level} students
- Distinguish between surface-level and deep implementation of strategies
- Evaluate quality, not just presence, of pedagogical approaches
- Provide balanced feedback (strengths and areas for improvement)
- Make recommendations practical and teacher-friendly
"""

    expected_output = """
A comprehensive pedagogical effectiveness analysis including:
- Instructional design quality score (0-100) with explanation
- Scaffolding quality score (0-100) with examples
- Differentiation score (0-100) with analysis
- Engagement strategies score (0-100) with examples
- Formative assessment score (0-100) with opportunities identified
- Overall pedagogical effectiveness score (0-100)
- List of 5-7 teaching strategies used in curriculum
- 5-7 specific, actionable recommendations for improvement

The output should be structured according to the PedagogicalEffectivenessOutput model with:
- instructional_design_score
- scaffolding_score
- differentiation_score
- engagement_score
- formative_assessment_score
- overall_score
- teaching_strategies
- recommendations
"""

    task = Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context,
        output_pydantic=PedagogicalEffectivenessOutput,
        async_execution=False
    )
    
    logger.info(f"Created Pedagogical Analysis Task for grade {grade_level}")
    return task

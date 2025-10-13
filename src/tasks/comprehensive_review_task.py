"""
Comprehensive Curriculum Review Task
Top-level task for complete curriculum evaluation.
"""

from crewai import Task
from typing import Optional

from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def create_comprehensive_review_task(
    agent,
    curriculum_content: str,
    grade_level: str,
    context: Optional[list] = None
) -> Task:
    """
    Create a task for comprehensive curriculum review.
    
    This task coordinates the entire review process, delegating to specialized
    teams and synthesizing their findings into a final report.
    
    Args:
        agent: The Curriculum Review Manager agent to assign this task to
        curriculum_content: The curriculum text to analyze
        grade_level: Target grade level (e.g., "3", "K", "8")
        context: Optional list of previous task outputs to use as context
        
    Returns:
        Task: Configured CrewAI task
        
    Example:
        >>> from src.agents import create_curriculum_review_manager_agent
        >>> agent = create_curriculum_review_manager_agent()
        >>> task = create_comprehensive_review_task(
        ...     agent=agent,
        ...     curriculum_content="Content here...",
        ...     grade_level="3"
        ... )
    """
    
    description = f"""
Lead a comprehensive review of this Grade {grade_level} mathematics curriculum.

CURRICULUM TO REVIEW:
{curriculum_content}

TARGET GRADE LEVEL: {grade_level}

As the Senior Curriculum Review Director, you must orchestrate a thorough, 
multi-dimensional evaluation by delegating to your specialized review teams:

═══════════════════════════════════════════════════════════════════════════
PHASE 1: DELEGATE TO REVIEW TEAMS
═══════════════════════════════════════════════════════════════════════════

1. **Standards & Content Analysis Team**
   Delegate comprehensive standards review:
   - Grade-level appropriateness analysis
   - Content standards alignment check
   - Mathematical practices evaluation
   - Ask them to provide integrated findings on standards alignment

2. **Teaching & Learning Quality Team**
   Delegate instructional quality review:
   - Pedagogical effectiveness analysis
   - Instructional design evaluation
   - Assessment quality review
   - Ask them to provide integrated findings on teaching effectiveness

3. **Inclusion & Equity Team**
   Delegate equity and access review:
   - Cultural responsiveness analysis
   - Accessibility evaluation
   - UDL compliance check
   - ELL support assessment
   - Ask them to provide findings on equity and inclusion

═══════════════════════════════════════════════════════════════════════════
PHASE 2: SYNTHESIZE FINDINGS
═══════════════════════════════════════════════════════════════════════════

After receiving reports from all three teams, synthesize their findings:

1. **Identify Common Themes**
   - What patterns emerge across multiple analyses?
   - Where do findings reinforce each other?
   - What are the curriculum's core strengths?
   - What are the most critical gaps?

2. **Recognize Tensions**
   - Where do findings conflict or create trade-offs?
   - How do you balance competing priorities?
   - What compromises make sense?

3. **Weigh Importance**
   - Which issues have greatest impact on student learning?
   - What must be addressed vs. nice to have?
   - How do you prioritize across dimensions?

═══════════════════════════════════════════════════════════════════════════
PHASE 3: MAKE STRATEGIC DECISIONS
═══════════════════════════════════════════════════════════════════════════

Provide your executive judgment on:

1. **Overall Quality Rating** (0-100 scale)
   Based on synthesis of all findings, what is the overall curriculum quality?

2. **Readiness for Adoption**
   - Ready to adopt as-is?
   - Adopt with minor modifications?
   - Adopt with major revisions?
   - Not recommended for adoption?

3. **Strongest Features** (3-5 key strengths)
   What does this curriculum do exceptionally well?

4. **Critical Gaps** (3-5 priority areas)
   What are the most important areas for improvement?

5. **Strategic Recommendations** (5-7 prioritized actions)
   What specific actions would have greatest impact?
   - Rank by priority (High/Medium/Low impact)
   - Make actionable and specific
   - Consider implementation feasibility

═══════════════════════════════════════════════════════════════════════════
PHASE 4: EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════════════════

Provide a clear, concise executive summary that:
- States overall recommendation (1-2 paragraphs)
- Highlights key findings (strengths and gaps)
- Lists prioritized recommendations
- Considers educator and student needs
- Is actionable and decision-ready

═══════════════════════════════════════════════════════════════════════════
DELIVERABLES
═══════════════════════════════════════════════════════════════════════════

Your comprehensive review must include:

1. **Overall Quality Rating** (0-100)
2. **Readiness Assessment** (adoption recommendation)
3. **Standards Alignment Summary** (from Team 1)
4. **Teaching Quality Summary** (from Team 2)
5. **Equity & Inclusion Summary** (from Team 3)
6. **Top 3-5 Strengths** with evidence
7. **Top 3-5 Critical Gaps** with evidence
8. **5-7 Prioritized Recommendations** (High/Medium/Low impact)
9. **Executive Summary** (decision-ready overview)

═══════════════════════════════════════════════════════════════════════════
REVIEW PRINCIPLES
═══════════════════════════════════════════════════════════════════════════

Remember to:
- Base all judgments on evidence
- Keep student learning as the priority
- Center equity and inclusion
- Balance ideals with practical realities
- Provide actionable guidance
- Be respectful but honest
- Prioritize by impact

This review will guide critical decisions affecting many students and teachers.
Bring your full expertise, wisdom, and strategic thinking to this work.
"""

    expected_output = """
A comprehensive curriculum review report including:

EXECUTIVE SUMMARY:
- Overall quality rating (0-100)
- Adoption recommendation
- Key findings overview
- Strategic guidance

DETAILED FINDINGS:
- Standards alignment summary (synthesized from Team 1)
- Teaching quality summary (synthesized from Team 2)
- Equity & inclusion summary (synthesized from Team 3)

STRATEGIC ANALYSIS:
- Top 3-5 curriculum strengths (specific, evidence-based)
- Top 3-5 critical gaps (specific, evidence-based)
- 5-7 prioritized recommendations (ranked by impact)

The report should be:
- Evidence-based and specific
- Balanced (strengths AND gaps)
- Actionable and prioritized
- Clear and concise
- Decision-ready
"""

    task = Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context,
        async_execution=False
    )
    
    logger.info(f"Created Comprehensive Review Task for grade {grade_level}")
    return task

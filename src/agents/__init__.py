"""Agent definitions for the curriculum review system."""

# Leaf Agents (Level 3 - No delegation)
from .grade_level_checker import (
    create_grade_level_checker_agent,
    grade_level_checker_agent
)
from .math_practices_evaluator import (
    create_math_practices_evaluator_agent,
    math_practices_evaluator_agent
)
from .pedagogical_analyst import (
    create_pedagogical_analyst_agent,
    pedagogical_analyst_agent
)
from .equity_reviewer import (
    create_equity_reviewer_agent,
    equity_reviewer_agent
)
from .assessment_evaluator import (
    create_assessment_evaluator_agent,
    assessment_evaluator_agent
)

# Mid-Level Coordinator Agents (Level 2 - Can delegate)
from .standards_content_analyst import (
    create_standards_content_analyst_agent,
    standards_content_analyst_agent
)
from .teaching_learning_reviewer import (
    create_teaching_learning_reviewer_agent,
    teaching_learning_reviewer_agent
)
from .inclusion_equity_specialist import (
    create_inclusion_equity_specialist_agent,
    inclusion_equity_specialist_agent
)

# Top-Level Orchestrator (Level 1 - Orchestrates everything)
from .curriculum_review_manager import (
    create_curriculum_review_manager_agent,
    curriculum_review_manager_agent
)

__all__ = [
    # Leaf Agents
    'create_grade_level_checker_agent',
    'grade_level_checker_agent',
    'create_math_practices_evaluator_agent',
    'math_practices_evaluator_agent',
    'create_pedagogical_analyst_agent',
    'pedagogical_analyst_agent',
    'create_equity_reviewer_agent',
    'equity_reviewer_agent',
    'create_assessment_evaluator_agent',
    'assessment_evaluator_agent',
    # Mid-Level Coordinators
    'create_standards_content_analyst_agent',
    'standards_content_analyst_agent',
    'create_teaching_learning_reviewer_agent',
    'teaching_learning_reviewer_agent',
    'create_inclusion_equity_specialist_agent',
    'inclusion_equity_specialist_agent',
    # Top-Level Orchestrator
    'create_curriculum_review_manager_agent',
    'curriculum_review_manager_agent',
]

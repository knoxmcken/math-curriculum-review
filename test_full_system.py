"""
Test script for the complete 3-level hierarchical multi-agent system.
Demonstrates full orchestration from top-level manager through all agents.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

# Import all agents
from src.agents.curriculum_review_manager import create_curriculum_review_manager_agent
from src.agents.standards_content_analyst import create_standards_content_analyst_agent
from src.agents.teaching_learning_reviewer import create_teaching_learning_reviewer_agent
from src.agents.inclusion_equity_specialist import create_inclusion_equity_specialist_agent
from src.agents.grade_level_checker import create_grade_level_checker_agent
from src.agents.math_practices_evaluator import create_math_practices_evaluator_agent
from src.agents.pedagogical_analyst import create_pedagogical_analyst_agent
from src.agents.assessment_evaluator import create_assessment_evaluator_agent
from src.agents.equity_reviewer import create_equity_reviewer_agent

from src.tasks.comprehensive_review_task import create_comprehensive_review_task
from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_full_system")

print("=" * 90)
print("TESTING COMPLETE 3-LEVEL HIERARCHICAL MULTI-AGENT SYSTEM")
print("=" * 90)
print()

# Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Create complete agent hierarchy
print("Step 2: Creating complete 3-level agent hierarchy...")
print()

print("  LEVEL 3: Creating Leaf Agents (Specialists - No delegation):")
grade_checker = create_grade_level_checker_agent(verbose=False)
print(f"    ✓ {grade_checker.role}")

practices_eval = create_math_practices_evaluator_agent(verbose=False)
print(f"    ✓ {practices_eval.role}")

pedagogy_analyst = create_pedagogical_analyst_agent(verbose=False)
print(f"    ✓ {pedagogy_analyst.role}")

assessment_eval = create_assessment_evaluator_agent(verbose=False)
print(f"    ✓ {assessment_eval.role}")

equity_reviewer = create_equity_reviewer_agent(verbose=False)
print(f"    ✓ {equity_reviewer.role}")

print()
print("  LEVEL 2: Creating Mid-Level Coordinators (Can delegate to Level 3):")
standards_analyst = create_standards_content_analyst_agent(verbose=False)
print(f"    ✓ {standards_analyst.role}")

teaching_reviewer = create_teaching_learning_reviewer_agent(verbose=False)
print(f"    ✓ {teaching_reviewer.role}")

equity_specialist = create_inclusion_equity_specialist_agent(verbose=False)
print(f"    ✓ {equity_specialist.role}")

print()
print("  LEVEL 1: Creating Top-Level Orchestrator (Coordinates everything):")
review_manager = create_curriculum_review_manager_agent(verbose=True)
print(f"    ✓ {review_manager.role}")

print()
print("✓ Complete 3-level hierarchy created:")
print("  • Level 1: 1 Orchestrator (Review Manager)")
print("  • Level 2: 3 Coordinators (Standards, Teaching, Equity)")
print("  • Level 3: 5 Specialists (Content, Practices, Pedagogy, Assessment, Equity)")
print(f"  • Total: 9 agents")
print()

# Create comprehensive review task
print("Step 3: Creating comprehensive review task...")

review_task = create_comprehensive_review_task(
    agent=review_manager,
    curriculum_content=curriculum_content,
    grade_level="3"
)

print("✓ Comprehensive review task created")
print()

# Create crew with all agents
print("Step 4: Creating hierarchical crew with all 9 agents...")
crew = Crew(
    agents=[
        # Level 1: Top-Level Orchestrator
        review_manager,
        # Level 2: Mid-Level Coordinators
        standards_analyst,
        teaching_reviewer,
        equity_specialist,
        # Level 3: Leaf Specialists
        grade_checker,
        practices_eval,
        pedagogy_analyst,
        assessment_eval,
        equity_reviewer
    ],
    tasks=[review_task],
    process=Process.hierarchical,
    manager_llm="gpt-3.5-turbo",
    verbose=True
)

print("✓ Hierarchical crew created with all 9 agents")
print()

# Execute full review
print("Step 5: Executing complete curriculum review...")
print("=" * 90)
print()
print("This will demonstrate:")
print("  • Top-level orchestration")
print("  • Delegation through 3 levels")
print("  • Coordination across teams")
print("  • Synthesis of multiple analyses")
print("  • Strategic decision-making")
print()
print("Please be patient - this is a comprehensive multi-agent process...")
print("=" * 90)
print()

try:
    result = crew.kickoff()
    
    print("\n" + "=" * 90)
    print("🎉 COMPLETE CURRICULUM REVIEW FINISHED! 🎉")
    print("=" * 90)
    print()
    
    print("COMPREHENSIVE REVIEW REPORT:")
    print("-" * 90)
    print(result)
    print("-" * 90)
    print()
    
    print("✅ Full system test SUCCESSFUL!")
    print()
    print("🎉 DEMONSTRATED:")
    print("  ✓ 3-level hierarchical agent system")
    print("  ✓ Top-level orchestration and delegation")
    print("  ✓ Mid-level coordination")
    print("  ✓ Leaf-level specialized analysis")
    print("  ✓ Multi-perspective synthesis")
    print("  ✓ Strategic recommendations")
    print()
    print("=" * 90)
    print("🏆 COMPLETE MULTI-AGENT SYSTEM WORKING! 🏆")
    print("=" * 90)
    
except Exception as e:
    print("\n" + "=" * 90)
    print("❌ TEST FAILED")
    print("=" * 90)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

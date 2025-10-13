"""
Test script for mid-level coordinator agents with delegation.
Demonstrates hierarchical multi-agent system with leaf agents.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process, Task

# Import mid-level coordinators
from src.agents.standards_content_analyst import create_standards_content_analyst_agent
from src.agents.teaching_learning_reviewer import create_teaching_learning_reviewer_agent
from src.agents.inclusion_equity_specialist import create_inclusion_equity_specialist_agent

# Import leaf agents
from src.agents.grade_level_checker import create_grade_level_checker_agent
from src.agents.math_practices_evaluator import create_math_practices_evaluator_agent
from src.agents.pedagogical_analyst import create_pedagogical_analyst_agent
from src.agents.assessment_evaluator import create_assessment_evaluator_agent
from src.agents.equity_reviewer import create_equity_reviewer_agent

from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_mid_level_agents")

print("=" * 80)
print("TESTING MID-LEVEL COORDINATOR AGENTS WITH DELEGATION")
print("=" * 80)
print()

# Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Create all agents
print("Step 2: Creating agent hierarchy...")
print()

print("  Creating Leaf Agents (Level 3 - No delegation):")
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
print("  Creating Mid-Level Coordinators (Level 2 - Can delegate):")
standards_analyst = create_standards_content_analyst_agent(verbose=True)
print(f"    ✓ {standards_analyst.role}")

teaching_reviewer = create_teaching_learning_reviewer_agent(verbose=True)
print(f"    ✓ {teaching_reviewer.role}")

equity_specialist = create_inclusion_equity_specialist_agent(verbose=True)
print(f"    ✓ {equity_specialist.role}")

print()
print("✓ Agent hierarchy created:")
print("  • 5 Leaf agents (specialists)")
print("  • 3 Mid-level coordinators")
print()

# Create task for Standards & Content Analyst (will delegate to leaf agents)
print("Step 3: Creating coordinated review task...")

task_description = f"""
Conduct a comprehensive standards and content review of this Grade 3 curriculum.

CURRICULUM TO ANALYZE:
{curriculum_content}

You should coordinate analysis from your team of specialists:
1. Delegate grade-level appropriateness check
2. Delegate mathematical practices evaluation
3. Synthesize their findings
4. Provide integrated recommendations

Focus on:
- Overall standards alignment (content + practices)
- Grade-level appropriateness
- Mathematical practices development
- Integration of content and practices
- Key strengths and priorities for improvement

Provide a strategic summary that synthesizes findings from both specialists.
"""

coordinator_task = Task(
    description=task_description,
    expected_output="Comprehensive standards and content analysis with synthesized findings and strategic recommendations",
    agent=standards_analyst
)

print("✓ Task created for Standards & Content Analyst")
print()

# Create crew with hierarchical structure
print("Step 4: Creating hierarchical crew...")
crew = Crew(
    agents=[
        # Mid-level coordinator (will delegate)
        standards_analyst,
        # Leaf agents (can be delegated to)
        grade_checker,
        practices_eval
    ],
    tasks=[coordinator_task],
    process=Process.hierarchical,  # Hierarchical process enables delegation
    manager_llm="gpt-3.5-turbo",  # LLM for the manager
    verbose=True
)

print("✓ Hierarchical crew created")
print("  • Process: Hierarchical (enables delegation)")
print("  • Coordinator: Standards & Content Analyst")
print("  • Available specialists: Grade Checker, Practices Evaluator")
print()

# Execute
print("Step 5: Executing coordinated review...")
print("=" * 80)
print()

try:
    result = crew.kickoff()
    
    print("\n" + "=" * 80)
    print("COORDINATED REVIEW COMPLETED!")
    print("=" * 80)
    print()
    
    print("RESULT:")
    print("-" * 80)
    print(result)
    print("-" * 80)
    print()
    
    print("✅ Mid-level coordinator test SUCCESSFUL!")
    print()
    print("🎉 Demonstrated:")
    print("  • Hierarchical agent structure")
    print("  • Delegation from coordinator to specialists")
    print("  • Synthesis of multiple analyses")
    print("  • Strategic recommendations")
    
except Exception as e:
    print("\n" + "=" * 80)
    print("❌ TEST FAILED")
    print("=" * 80)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

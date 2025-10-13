"""
Test script for the fourth agent: Equity & Accessibility Reviewer
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.equity_reviewer import create_equity_reviewer_agent
from src.tasks.equity_review_task import create_equity_review_task
from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_fourth_agent")

print("=" * 70)
print("TESTING FOURTH AGENT: Equity & Accessibility Reviewer")
print("=" * 70)
print()

# Step 1: Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Step 2: Create agent
print("Step 2: Creating Equity & Accessibility Reviewer Agent...")
agent = create_equity_reviewer_agent(verbose=True)
print(f"✓ Agent created: {agent.role}")
print()

# Step 3: Create task
print("Step 3: Creating task...")
task = create_equity_review_task(
    agent=agent,
    curriculum_content=curriculum_content,
    grade_level="3"
)
print(f"✓ Task created")
print()

# Step 4: Create and run crew
print("Step 4: Creating crew and executing task...")
print("-" * 70)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

print("\nExecuting agent task...")
print("=" * 70)

try:
    result = crew.kickoff()
    
    print("\n" + "=" * 70)
    print("TASK COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print()
    
    print("RESULT:")
    print("-" * 70)
    print(result)
    print("-" * 70)
    print()
    
    # If result is a Pydantic model, show structured output
    if hasattr(result, 'pydantic'):
        output = result.pydantic
        print("\nSTRUCTURED OUTPUT:")
        print("-" * 70)
        print(f"Overall Equity & Accessibility Score: {output.overall_equity_score}/100")
        print(f"\nComponent Scores:")
        print(f"  • Cultural Responsiveness: {output.cultural_responsiveness}/100")
        print(f"  • Accessibility: {output.accessibility_score}/100")
        print(f"  • ELL Support: {output.ell_support_score}/100")
        print(f"  • UDL Compliance: {output.udl_compliance}/100")
        
        print(f"\nRepresentation Analysis ({len(output.representation_analysis)}):")
        for i, obs in enumerate(output.representation_analysis, 1):
            print(f"  {i}. {obs}")
        
        print(f"\nBarriers Identified ({len(output.barriers_identified)}):")
        for i, barrier in enumerate(output.barriers_identified, 1):
            print(f"  {i}. {barrier}")
        
        print(f"\nRecommendations ({len(output.recommendations)}):")
        for i, rec in enumerate(output.recommendations, 1):
            print(f"  {i}. {rec}")
    
    print("\n✅ Fourth agent test SUCCESSFUL!")
    
except Exception as e:
    print("\n" + "=" * 70)
    print("❌ TASK FAILED")
    print("=" * 70)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

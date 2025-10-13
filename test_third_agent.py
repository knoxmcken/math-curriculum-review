"""
Test script for the third agent: Pedagogical Effectiveness Analyst
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.pedagogical_analyst import create_pedagogical_analyst_agent
from src.tasks.pedagogical_analysis_task import create_pedagogical_analysis_task
from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_third_agent")

print("=" * 70)
print("TESTING THIRD AGENT: Pedagogical Effectiveness Analyst")
print("=" * 70)
print()

# Step 1: Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Step 2: Create agent
print("Step 2: Creating Pedagogical Effectiveness Analyst Agent...")
agent = create_pedagogical_analyst_agent(verbose=True)
print(f"✓ Agent created: {agent.role}")
print()

# Step 3: Create task
print("Step 3: Creating task...")
task = create_pedagogical_analysis_task(
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
        print(f"Overall Pedagogical Score: {output.overall_score}/100")
        print(f"\nComponent Scores:")
        print(f"  • Instructional Design: {output.instructional_design_score}/100")
        print(f"  • Scaffolding: {output.scaffolding_score}/100")
        print(f"  • Differentiation: {output.differentiation_score}/100")
        print(f"  • Engagement: {output.engagement_score}/100")
        print(f"  • Formative Assessment: {output.formative_assessment_score}/100")
        
        print(f"\nTeaching Strategies ({len(output.teaching_strategies)}):")
        for strategy in output.teaching_strategies:
            print(f"  • {strategy}")
        
        print(f"\nRecommendations ({len(output.recommendations)}):")
        for i, rec in enumerate(output.recommendations, 1):
            print(f"  {i}. {rec}")
    
    print("\n✅ Third agent test SUCCESSFUL!")
    
except Exception as e:
    print("\n" + "=" * 70)
    print("❌ TASK FAILED")
    print("=" * 70)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

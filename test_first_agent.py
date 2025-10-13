"""
Test script for the first agent: Grade Level Standards Checker
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.grade_level_checker import create_grade_level_checker_agent
from src.tasks.grade_level_check_task import create_grade_level_check_task
from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_first_agent")

print("=" * 70)
print("TESTING FIRST AGENT: Grade Level Standards Checker")
print("=" * 70)
print()

# Step 1: Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Step 2: Create agent
print("Step 2: Creating Grade Level Checker Agent...")
agent = create_grade_level_checker_agent(verbose=True)
print(f"✓ Agent created: {agent.role}")
print()

# Step 3: Create task
print("Step 3: Creating task...")
task = create_grade_level_check_task(
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
    process=Process.sequential,  # Tasks run one after another
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
        print(f"Grade Level: {output.grade_level}")
        print(f"Appropriateness Score: {output.appropriateness_score}/100")
        print(f"Scaffolding Quality: {output.scaffolding_quality}")
        print(f"\nAppropriate Topics: {len(output.appropriate_topics)}")
        for topic in output.appropriate_topics:
            print(f"  • {topic}")
        print(f"\nToo Advanced: {len(output.too_advanced_topics)}")
        for topic in output.too_advanced_topics:
            print(f"  • {topic}")
        print(f"\nToo Basic: {len(output.too_basic_topics)}")
        for topic in output.too_basic_topics:
            print(f"  • {topic}")
        print(f"\nRecommendations: {len(output.recommendations)}")
        for rec in output.recommendations:
            print(f"  • {rec}")
    
    print("\n✅ First agent test SUCCESSFUL!")
    
except Exception as e:
    print("\n" + "=" * 70)
    print("❌ TASK FAILED")
    print("=" * 70)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

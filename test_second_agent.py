"""
Test script for the second agent: Mathematical Practices Evaluator
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.math_practices_evaluator import create_math_practices_evaluator_agent
from src.tasks.math_practices_task import create_math_practices_task
from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_second_agent")

print("=" * 70)
print("TESTING SECOND AGENT: Mathematical Practices Evaluator")
print("=" * 70)
print()

# Step 1: Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Step 2: Create agent
print("Step 2: Creating Mathematical Practices Evaluator Agent...")
agent = create_math_practices_evaluator_agent(verbose=True)
print(f"✓ Agent created: {agent.role}")
print()

# Step 3: Create task
print("Step 3: Creating task...")
task = create_math_practices_task(
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
        print(f"Overall Score: {output.overall_score}/100")
        print(f"\nIndividual Practice Scores:")
        for practice, score in output.practice_scores.items():
            print(f"  {practice}: {score}/100")
        
        print(f"\nStrengths ({len(output.strengths)}):")
        for strength in output.strengths:
            print(f"  • {strength}")
        
        print(f"\nWeaknesses ({len(output.weaknesses)}):")
        for weakness in output.weaknesses:
            print(f"  • {weakness}")
        
        print(f"\nPractice Opportunities:")
        for practice, opportunities in output.practice_opportunities.items():
            print(f"  {practice}: {len(opportunities)} opportunities")
            for opp in opportunities[:2]:  # Show first 2
                print(f"    - {opp}")
        
        print(f"\nRecommendations ({len(output.recommendations)}):")
        for rec in output.recommendations:
            print(f"  • {rec}")
    
    print("\n✅ Second agent test SUCCESSFUL!")
    
except Exception as e:
    print("\n" + "=" * 70)
    print("❌ TASK FAILED")
    print("=" * 70)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

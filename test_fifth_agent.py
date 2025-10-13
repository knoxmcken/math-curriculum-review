"""
Test script for the fifth agent: Assessment Quality Evaluator
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from src.agents.assessment_evaluator import create_assessment_evaluator_agent
from src.tasks.assessment_evaluation_task import create_assessment_evaluation_task
from src.utils.logger import setup_logger
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Set up logging
logger = setup_logger("test_fifth_agent")

print("=" * 70)
print("TESTING FIFTH AGENT: Assessment Quality Evaluator")
print("=" * 70)
print()

# Step 1: Load sample curriculum
print("Step 1: Loading sample curriculum...")
curriculum_path = "data/input/sample_grade3_curriculum.txt"
curriculum_content = read_text_file(curriculum_path)
print(f"✓ Loaded curriculum ({len(curriculum_content)} characters)")
print()

# Step 2: Create agent
print("Step 2: Creating Assessment Quality Evaluator Agent...")
agent = create_assessment_evaluator_agent(verbose=True)
print(f"✓ Agent created: {agent.role}")
print()

# Step 3: Create task
print("Step 3: Creating task...")
task = create_assessment_evaluation_task(
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
        print(f"Overall Assessment Quality: {output.overall_quality}/100")
        print(f"\nComponent Scores:")
        print(f"  • Alignment: {output.alignment_score}/100")
        print(f"  • Question Quality: {output.question_quality_score}/100")
        print(f"  • Variety: {output.variety_score}/100")
        print(f"  • Validity: {output.validity_score}/100")
        print(f"  • Accessibility: {output.accessibility_score}/100")
        
        print(f"\nAssessment Types ({len(output.assessment_types)}):")
        for atype in output.assessment_types:
            print(f"  • {atype}")
        
        print(f"\nStrengths ({len(output.strengths)}):")
        for i, strength in enumerate(output.strengths, 1):
            print(f"  {i}. {strength}")
        
        print(f"\nWeaknesses ({len(output.weaknesses)}):")
        for i, weakness in enumerate(output.weaknesses, 1):
            print(f"  {i}. {weakness}")
        
        print(f"\nRecommendations ({len(output.recommendations)}):")
        for i, rec in enumerate(output.recommendations, 1):
            print(f"  {i}. {rec}")
    
    print("\n✅ Fifth agent test SUCCESSFUL!")
    print("\n🎉 ALL 5 LEAF AGENTS NOW COMPLETE!")
    
except Exception as e:
    print("\n" + "=" * 70)
    print("❌ TASK FAILED")
    print("=" * 70)
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

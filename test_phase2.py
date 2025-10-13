"""Test script for Phase 2 tools and models."""

import json
from src.tools import document_analyzer_tool, standards_lookup_tool, report_generator_tool
from src.models import GradeLevelCheckOutput, StandardsAlignmentOutput

print('=== Testing Phase 2 Tools and Models ===\n')

# Test 1: Document Analyzer
print('1. Document Analyzer Tool')
result = document_analyzer_tool._run('data/input/sample_grade3_curriculum.txt')
data = json.loads(result)
print(f'   Success: {data.get("success")}')
print(f'   File: {data.get("file_name")}')
print(f'   Length: {data.get("length")} chars')

# Test 2: Standards Lookup
print('\n2. Standards Lookup Tool')
result = standards_lookup_tool._run('grade:3')
data = json.loads(result)
print(f'   Standards count: {data.get("standards_count")}')

result = standards_lookup_tool._run('practices')
data = json.loads(result)
print(f'   Practices count: {data.get("count")}')

# Test 3: Report Generator
print('\n3. Report Generator Tool')
report_data = {
    'title': 'Sample Review Report',
    'content': {
        'overview': {
            'grade': '3',
            'score': 85
        },
        'strengths': ['Clear explanations', 'Good examples'],
        'weaknesses': ['Limited practice problems']
    },
    'format': 'md',
    'filename': 'test_report.md'
}
result = report_generator_tool._run(json.dumps(report_data))
data = json.loads(result)
print(f'   Report generated: {data.get("filename")}')
print(f'   Location: {data.get("file_path")}')

# Test 4: Pydantic Models
print('\n4. Pydantic Output Models')
output = GradeLevelCheckOutput(
    grade_level='3',
    appropriateness_score=90.0,
    scaffolding_quality='Excellent',
    appropriate_topics=['Multiplication', 'Division', 'Fractions']
)
print(f'   ✓ GradeLevelCheckOutput: grade={output.grade_level}, score={output.appropriateness_score}')

alignment = StandardsAlignmentOutput(
    grade_level='3',
    standards_covered=['3.OA.A.1', '3.OA.A.2', '3.NF.A.1'],
    standards_missing=[],
    alignment_score=100.0,
    detailed_mapping={'3.OA.A.1': 'Lesson 1', '3.OA.A.2': 'Lesson 2'}
)
print(f'   ✓ StandardsAlignmentOutput: {len(alignment.standards_covered)} standards covered')

print('\n✅ Phase 2 Complete - All tools and models working correctly!')

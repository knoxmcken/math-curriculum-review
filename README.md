# 📚 Mathematics Curriculum Review System

A sophisticated multi-agent AI system for comprehensive mathematics curriculum analysis and review based on American educational standards.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://github.com/joaomdmoura/crewAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Overview

This system uses **9 specialized AI agents** working in a **3-level hierarchy** to provide thorough, expert-level curriculum reviews. The agents coordinate to analyze:

- ✅ **Standards Alignment** - Grade-level appropriateness and CCSSM coverage
- ✅ **Mathematical Practices** - Development of problem-solving and reasoning skills
- ✅ **Pedagogical Quality** - Evidence-based instructional strategies
- ✅ **Assessment Design** - Quality, alignment, and variety
- ✅ **Equity & Accessibility** - Cultural responsiveness and Universal Design for Learning

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│         LEVEL 1: Top-Level Orchestrator                 │
│                                                           │
│    Senior Curriculum Review Director                     │
│    • Orchestrates entire review process                  │
│    • Synthesizes findings from all teams                 │
│    • Makes strategic decisions                           │
└────────────────────────┬────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│   LEVEL 2:     │ │   LEVEL 2:     │ │   LEVEL 2:     │
│   Standards &  │ │   Teaching &   │ │   Inclusion &  │
│   Content      │ │   Learning     │ │   Equity       │
│   Analyst      │ │   Reviewer     │ │   Specialist   │
└────────┬───────┘ └────────┬───────┘ └────────┬───────┘
         │                  │                  │
    ┌────┴────┐        ┌───┴───┐             │
    ▼         ▼        ▼       ▼             ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ LEVEL 3: Leaf Specialists (Domain Experts)            │
│                                                         │
│ Grade    │ │ Math   │ │Pedagogy│ │Assess. │ │ Equity │
│ Level    │ │Practice│ │Analyst │ │Eval.   │ │Reviewer│
│ Checker  │ │Eval.   │ │        │ │        │ │        │
└──────────┘ └────────┘ └────────┘ └────────┘ └────────┘

Total: 9 AI Agents Working in Coordinated Hierarchy
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for OpenAI (or compatible LLM service)
- Optional: Tavily API key (for web search capabilities)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/knoxmcken/math-curriculum-review.git
   cd math-curriculum-review
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   # Required
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Optional (for web search capabilities)
   TAVILY_API_KEY=your_tavily_api_key_here
   
   # Optional (if using Anthropic)
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

---

## 📖 Usage

### Option 1: Full System Review (Recommended)

Run a complete 9-agent curriculum review:

```bash
python test_full_system.py
```

This demonstrates:
- 3-level hierarchical delegation
- Multi-agent collaboration
- Comprehensive synthesis of findings
- Strategic recommendations

### Option 2: Individual Agent Tests

Test specific agents independently:

```bash
# Test grade-level alignment
python test_agent_1_grade_level.py

# Test mathematical practices
python test_agent_2_math_practices.py

# Test pedagogical effectiveness
python test_agent_3_pedagogical.py

# Test equity & accessibility
python test_agent_4_equity.py

# Test assessment quality
python test_agent_5_assessment.py
```

### Option 3: Mid-Level Coordination Test

Test mid-level coordinators with delegation:

```bash
python test_mid_level_agents.py
```

### Option 4: Custom Integration

Use the system in your own code:

```python
from dotenv import load_dotenv
from crewai import Crew, Process

# Import agents and tasks
from src.agents import create_curriculum_review_manager_agent
from src.tasks import create_comprehensive_review_task
from src.utils.file_utils import read_text_file

# Load environment
load_dotenv()

# Load curriculum content
curriculum_content = read_text_file("path/to/curriculum.txt")

# Create the orchestrator
review_manager = create_curriculum_review_manager_agent()

# Create the review task
review_task = create_comprehensive_review_task(
    agent=review_manager,
    curriculum_content=curriculum_content,
    grade_level="3"  # or K, 1, 2, 4, 5, etc.
)

# Create and run the crew
crew = Crew(
    agents=[review_manager],  # Add other agents as needed
    tasks=[review_task],
    process=Process.hierarchical,
    manager_llm="gpt-3.5-turbo",
    verbose=True
)

result = crew.kickoff()
print(result)
```

---

## 📁 Project Structure

```
math-curriculum-review/
│
├── .github/
│   └── copilot-instructions.md    # Custom instructions for GitHub Copilot
│
├── data/
│   ├── input/
│   │   └── sample_grade3_curriculum.txt  # Sample curriculum for testing
│   └── standards/
│       └── ccssm_standards.json          # Common Core State Standards
│
├── src/
│   ├── agents/                    # AI agent definitions
│   │   ├── curriculum_review_manager.py  # Level 1: Orchestrator
│   │   ├── standards_content_analyst.py  # Level 2: Coordinator
│   │   ├── teaching_learning_reviewer.py # Level 2: Coordinator
│   │   ├── inclusion_equity_specialist.py# Level 2: Coordinator
│   │   ├── grade_level_checker.py        # Level 3: Specialist
│   │   ├── math_practices_evaluator.py   # Level 3: Specialist
│   │   ├── pedagogical_analyst.py        # Level 3: Specialist
│   │   ├── assessment_evaluator.py       # Level 3: Specialist
│   │   └── equity_reviewer.py            # Level 3: Specialist
│   │
│   ├── tasks/                     # Task definitions for agents
│   │   ├── comprehensive_review_task.py
│   │   ├── grade_level_check_task.py
│   │   ├── math_practices_task.py
│   │   ├── pedagogical_analysis_task.py
│   │   ├── assessment_evaluation_task.py
│   │   └── equity_review_task.py
│   │
│   ├── tools/                     # Custom tools for agents
│   │   ├── document_analyzer.py
│   │   └── standards_lookup.py
│   │
│   ├── models/                    # Pydantic data models
│   │   └── review_models.py
│   │
│   └── utils/                     # Utility functions
│       ├── file_utils.py
│       ├── logger.py
│       └── standards_loader.py
│
├── tests/                         # Test scripts
│   ├── test_full_system.py
│   ├── test_mid_level_agents.py
│   └── test_agent_*.py
│
├── references/                    # Reference materials
│   ├── L3_customer_support.ipynb
│   ├── L4_tools_customer_outreach.ipynb
│   ├── L5_tasks_event_planning.ipynb
│   ├── L6_collaboration_financial_analysis.ipynb
│   ├── L7_job_application_crew.ipynb
│   └── notebook_summary.md
│
├── agent_system_architecture.md   # System design documentation
├── implementation_plan.md         # Development roadmap
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment variables
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## 🎯 Key Features

### 🤖 Intelligent Agent System

- **Hierarchical Delegation**: Orchestrator delegates to coordinators who manage specialists
- **Specialized Expertise**: Each agent has domain-specific knowledge and evaluation criteria
- **Memory Enabled**: Agents remember context across interactions
- **Tool Integration**: Custom tools for standards lookup and document analysis

### 📊 Comprehensive Analysis

- **Standards Alignment**: Verifies curriculum alignment with Common Core State Standards for Mathematics (CCSSM)
- **Mathematical Practices**: Evaluates development of all 8 Standards for Mathematical Practice
- **Pedagogical Quality**: Analyzes instructional strategies and learning progressions
- **Assessment Design**: Reviews formative and summative assessment quality
- **Equity & Inclusion**: Ensures accessibility, cultural responsiveness, and UDL principles

### 🔄 Flexible Workflow

- **Full System Review**: Run all 9 agents for comprehensive analysis
- **Targeted Reviews**: Run individual agents for specific aspects
- **Custom Integration**: Import and use agents in your own applications
- **Batch Processing**: Review multiple curricula programmatically

---

## 🛠️ Configuration

### Adjusting Agent Behavior

Each agent can be configured with:

```python
agent = create_grade_level_checker_agent(
    verbose=True  # Set to False for less output
)
```

### Changing LLM Model

Update the model in your crew configuration:

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.hierarchical,
    manager_llm="gpt-4",  # or "gpt-3.5-turbo", "gpt-4-turbo", etc.
    verbose=True
)
```

### Custom Standards

Replace or update `data/standards/ccssm_standards.json` with your own standards:

```json
{
  "grade_3": {
    "operations_algebraic_thinking": [
      {
        "code": "3.OA.A.1",
        "description": "Interpret products of whole numbers..."
      }
    ]
  }
}
```

---

## 📋 Review Output

The system provides comprehensive reviews including:

### Executive Summary
- Overall quality rating (0-100)
- Adoption recommendation
- Key findings overview

### Detailed Analysis
- **Standards Alignment**: Coverage, appropriateness, gaps
- **Teaching Quality**: Pedagogy, scaffolding, differentiation
- **Assessment Quality**: Alignment, variety, accessibility
- **Equity & Inclusion**: Cultural responsiveness, UDL, accessibility

### Strategic Recommendations
- Top 3-5 curriculum strengths
- Top 3-5 critical gaps
- 5-7 prioritized recommendations (ranked by impact)

---

## 🧪 Testing

All agents and the complete system have been thoroughly tested:

```bash
# Run all individual agent tests
python test_agent_1_grade_level.py
python test_agent_2_math_practices.py
python test_agent_3_pedagogical.py
python test_agent_4_equity.py
python test_agent_5_assessment.py

# Test mid-level coordination
python test_mid_level_agents.py

# Test full system
python test_full_system.py
```

**All tests pass successfully** ✅

---

## 📚 Documentation

- **[System Architecture](agent_system_architecture.md)** - Detailed design and agent roles
- **[Implementation Plan](implementation_plan.md)** - Development phases and roadmap
- **[Reference Materials](references/notebook_summary.md)** - CrewAI patterns and examples
- **[Copilot Instructions](.github/copilot-instructions.md)** - Development guidelines

---

## 🤝 Contributing

This is a specialized curriculum review tool, but contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **CrewAI Framework** - For the multi-agent orchestration capabilities
- **Common Core State Standards Initiative** - For the mathematics standards
- **OpenAI** - For the language model capabilities
- **Research Community** - For evidence-based instructional design principles

---

## 📞 Support

For questions, issues, or suggestions:

- **Issues**: [GitHub Issues](https://github.com/knoxmcken/math-curriculum-review/issues)
- **Discussions**: [GitHub Discussions](https://github.com/knoxmcken/math-curriculum-review/discussions)

---

## 🔮 Future Enhancements

Planned features (see `implementation_plan.md` for details):

- [ ] Web interface for curriculum upload and review
- [ ] RESTful API for integration with other systems
- [ ] Support for additional standards (state-specific, international)
- [ ] Multi-grade curriculum analysis
- [ ] Comparison reports across curricula
- [ ] Export to PDF/HTML formats
- [ ] Real-time collaboration features
- [ ] Advanced analytics and visualizations

---

## 🎓 Use Cases

This system is ideal for:

- **School Districts**: Evaluating curricula for adoption decisions
- **Curriculum Publishers**: Quality assurance and improvement
- **Education Researchers**: Analyzing curriculum quality at scale
- **Teachers**: Understanding curriculum strengths and gaps
- **Instructional Coaches**: Identifying professional development needs
- **Policy Makers**: Comparing curricula against standards

---

## ⚡ Performance Notes

- **Review Time**: Approximately 2-5 minutes per curriculum unit (depending on length)
- **API Costs**: Using `gpt-3.5-turbo` costs ~$0.10-0.50 per review
- **Scalability**: Can process multiple curricula in batch mode
- **Accuracy**: Agent analyses are based on research and standards, but should be validated by human experts

---

## 🎉 Quick Example

```python
from dotenv import load_dotenv
from src.agents import create_grade_level_checker_agent
from src.tasks import create_grade_level_check_task
from crewai import Crew

load_dotenv()

# Simple curriculum check
curriculum = """
Grade 3 - Multiplication Unit
Students will learn to multiply numbers 0-10...
"""

agent = create_grade_level_checker_agent()
task = create_grade_level_check_task(agent, curriculum, "3")

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()

print(result)
```

---

**Built with ❤️ for mathematics education**

*Helping educators make informed curriculum decisions to serve all students.*

---

## 📊 System Status

- ✅ **Status**: Production Ready
- ✅ **Version**: 1.0.0
- ✅ **Last Updated**: October 2025
- ✅ **Tested**: All agents and workflows
- ✅ **Documentation**: Complete

**Ready to transform your curriculum review process!** 🚀

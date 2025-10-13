# Math Curriculum Review Project

This project is for reviewing and analyzing mathematics curriculum materials.

## Project Structure

- `.github/`: Contains GitHub-specific configuration files
  - `copilot-instructions.md`: Custom instructions for GitHub Copilot CLI
- `requirements.txt`: Python dependencies
- `.gitignore`: Git ignore file

## Project Purpose

This is a workspace for reviewing mathematics curriculum content, materials, and educational resources.

## Technology Stack

- Python 3.x
- CrewAI framework for AI agents
- LangChain for language model operations
- Tavily for web search capabilities
- Python-dotenv for environment variable management

## How to Get Started

1. **Create a virtual environment**:
   ```powershell
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add necessary API keys (e.g., TAVILY_API_KEY, OPENAI_API_KEY, etc.)

## Development Guidelines

### Working with AI Agents

- This project uses the CrewAI framework for creating and managing AI agents
- Agents can be configured to perform various curriculum review tasks
- Use environment variables for API keys and sensitive configuration

### Creating Agents - IMPORTANT

When the user asks you to create an agent:

1. **First, check the `references/` directory** - Review the Jupyter notebooks (L3-L7) for examples and patterns
2. **Use the reference examples as your primary guide** - Follow the patterns, structures, and best practices demonstrated in the notebooks
3. **If references are insufficient** - Only then search Google, use external resources, or rely on your general knowledge
4. **Reference notebooks contain**:
   - Agent role definitions and goal setting
   - Task configuration patterns
   - Tool integration examples
   - Crew collaboration patterns
   - Best practices for agent coordination

The reference notebooks are located at:
- `references/L3_customer_support.ipynb` - Basic agent setup and cooperation
- `references/L4_tools_customer_outreach.ipynb` - Tool integration
- `references/L5_tasks_event_planning.ipynb` - Task management
- `references/L6_collaboration_financial_analysis.ipynb` - Agent collaboration
- `references/L7_job_application_crew.ipynb` - Complete multi-agent systems

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

## Notes for Copilot

- This is a standalone project with its own virtual environment
- All dependencies are managed locally via `requirements.txt`
- Environment-specific configuration should go in `.env` (not committed to git)

### Handling vim Commands

When the user requests to open a file with vim (e.g., `vim file_path`), always open it in a separate interactive terminal window using:

```powershell
Start-Process powershell -ArgumentList "-NoExit", "-Command", "vim file_path"
```

This approach:
- Opens vim in a new terminal window where the user can interact with it directly
- Keeps the terminal open after vim exits (via `-NoExit`) for any follow-up commands
- Allows the user to edit files normally with vim keybindings and save with `:wq`

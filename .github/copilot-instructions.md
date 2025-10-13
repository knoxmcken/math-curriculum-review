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

"""
Configuration management for the curriculum review system.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Configuration class for managing application settings.
    """
    
    # Project paths
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    SRC_DIR = PROJECT_ROOT / "src"
    DATA_DIR = PROJECT_ROOT / "data"
    STANDARDS_DIR = DATA_DIR / "standards"
    INPUT_DIR = DATA_DIR / "input"
    OUTPUT_DIR = DATA_DIR / "output"
    
    # API Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL_NAME: str = os.getenv("OPENAI_MODEL_NAME", "gpt-4-turbo")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY: Optional[str] = os.getenv("TAVILY_API_KEY")
    
    # Application Settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate that required configuration is present.
        
        Returns:
            bool: True if configuration is valid
            
        Raises:
            ValueError: If required configuration is missing
        """
        if not cls.OPENAI_API_KEY and not cls.ANTHROPIC_API_KEY and not cls.GOOGLE_API_KEY:
            raise ValueError(
                "At least one LLM API key must be configured. "
                "Set OPENAI_API_KEY, ANTHROPIC_API_KEY, or GOOGLE_API_KEY in your .env file."
            )
        return True
    
    @classmethod
    def get_model_name(cls) -> str:
        """
        Get the configured model name.
        
        Returns:
            str: Model name to use
        """
        return cls.OPENAI_MODEL_NAME


# Validate configuration on import
try:
    Config.validate()
except ValueError as e:
    print(f"Warning: {e}")
    print("Create a .env file with your API keys. See .env.example for reference.")

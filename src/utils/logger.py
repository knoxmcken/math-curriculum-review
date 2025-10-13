"""
Logging configuration for the curriculum review system.
"""

import logging
import sys
from pathlib import Path
from .config import Config


def setup_logger(name: str = "curriculum_review", level: str = None) -> logging.Logger:
    """
    Set up a logger with console and file handlers.
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    # Use config level if not specified
    if level is None:
        level = Config.LOG_LEVEL
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Remove existing handlers to avoid duplicates
    logger.handlers = []
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if Config.DEBUG_MODE else logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Optionally add file handler
    if Config.DEBUG_MODE:
        log_dir = Config.PROJECT_ROOT / "logs"
        log_dir.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler(log_dir / f"{name}.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# Create default logger
logger = setup_logger()

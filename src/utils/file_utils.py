"""
File I/O utilities for the curriculum review system.
"""

from pathlib import Path
from typing import List, Optional
import json

from .config import Config
from .logger import setup_logger

logger = setup_logger(__name__)


def ensure_directory(path: Path) -> Path:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path
        
    Returns:
        Path: The directory path
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_json(data: dict, filename: str, directory: Optional[Path] = None) -> Path:
    """
    Save data as JSON file.
    
    Args:
        data: Dictionary to save
        filename: Name of the file
        directory: Directory to save in (default: output directory)
        
    Returns:
        Path: Path to saved file
    """
    if directory is None:
        directory = Config.OUTPUT_DIR
    
    ensure_directory(directory)
    filepath = directory / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    
    logger.info(f"Saved JSON to {filepath}")
    return filepath


def load_json(filepath: Path) -> dict:
    """
    Load data from JSON file.
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        dict: Loaded data
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    logger.info(f"Loaded JSON from {filepath}")
    return data


def list_files(directory: Path, pattern: str = "*", recursive: bool = False) -> List[Path]:
    """
    List files in a directory matching a pattern.
    
    Args:
        directory: Directory to search
        pattern: Glob pattern (e.g., "*.pdf", "*.txt")
        recursive: Whether to search recursively
        
    Returns:
        List[Path]: List of matching file paths
    """
    if recursive:
        files = list(directory.rglob(pattern))
    else:
        files = list(directory.glob(pattern))
    
    # Filter out directories
    files = [f for f in files if f.is_file()]
    
    logger.info(f"Found {len(files)} files matching '{pattern}' in {directory}")
    return files


def read_text_file(filepath: Path) -> str:
    """
    Read content from a text file.
    
    Args:
        filepath: Path to text file
        
    Returns:
        str: File content
    """
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    logger.info(f"Read {len(content)} characters from {filepath}")
    return content


def write_text_file(content: str, filename: str, directory: Optional[Path] = None) -> Path:
    """
    Write content to a text file.
    
    Args:
        content: Text content to write
        filename: Name of the file
        directory: Directory to save in (default: output directory)
        
    Returns:
        Path: Path to saved file
    """
    if directory is None:
        directory = Config.OUTPUT_DIR
    
    ensure_directory(directory)
    filepath = directory / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    logger.info(f"Wrote {len(content)} characters to {filepath}")
    return filepath


def get_file_info(filepath: Path) -> dict:
    """
    Get information about a file.
    
    Args:
        filepath: Path to file
        
    Returns:
        dict: File information
    """
    stat = filepath.stat()
    
    return {
        'name': filepath.name,
        'path': str(filepath),
        'size_bytes': stat.st_size,
        'size_kb': round(stat.st_size / 1024, 2),
        'size_mb': round(stat.st_size / (1024 * 1024), 2),
        'extension': filepath.suffix,
        'created': stat.st_ctime,
        'modified': stat.st_mtime,
        'exists': filepath.exists(),
        'is_file': filepath.is_file(),
        'is_dir': filepath.is_dir(),
    }

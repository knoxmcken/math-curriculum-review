"""
Utility for loading and querying CCSSM standards.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from .config import Config
from .logger import setup_logger

logger = setup_logger(__name__)


class StandardsLoader:
    """
    Load and query Common Core State Standards for Mathematics.
    """
    
    def __init__(self, standards_file: Optional[Path] = None):
        """
        Initialize the standards loader.
        
        Args:
            standards_file: Path to standards JSON file. If None, uses default.
        """
        if standards_file is None:
            standards_file = Config.STANDARDS_DIR / "ccssm_standards.json"
        
        self.standards_file = standards_file
        self.standards_data = self._load_standards()
        logger.info(f"Loaded standards from {standards_file}")
    
    def _load_standards(self) -> Dict:
        """
        Load standards from JSON file.
        
        Returns:
            Dict: Standards data
        """
        try:
            with open(self.standards_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Standards file not found: {self.standards_file}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing standards JSON: {e}")
            return {}
    
    def get_mathematical_practices(self) -> List[Dict]:
        """
        Get all 8 Standards for Mathematical Practice.
        
        Returns:
            List[Dict]: List of mathematical practices
        """
        return self.standards_data.get("mathematical_practices", [])
    
    def get_grade_level_standards(self, grade: str) -> Dict:
        """
        Get all standards for a specific grade level.
        
        Args:
            grade: Grade level (e.g., "K", "1", "2", "3", etc.)
            
        Returns:
            Dict: Grade level standards with domains
        """
        grade_levels = self.standards_data.get("grade_levels", {})
        return grade_levels.get(str(grade), {})
    
    def get_domains(self, grade: str) -> Dict:
        """
        Get all domains for a specific grade level.
        
        Args:
            grade: Grade level
            
        Returns:
            Dict: Domains for the grade level
        """
        grade_data = self.get_grade_level_standards(grade)
        return grade_data.get("domains", {})
    
    def get_domain_standards(self, grade: str, domain: str) -> List[Dict]:
        """
        Get standards for a specific domain within a grade level.
        
        Args:
            grade: Grade level
            domain: Domain code (e.g., "OA", "NBT", "NF")
            
        Returns:
            List[Dict]: List of standards in the domain
        """
        domains = self.get_domains(grade)
        domain_data = domains.get(domain, {})
        return domain_data.get("standards", [])
    
    def search_standard(self, standard_id: str) -> Optional[Dict]:
        """
        Search for a specific standard by ID.
        
        Args:
            standard_id: Standard ID (e.g., "3.OA.A.1")
            
        Returns:
            Optional[Dict]: Standard data if found, None otherwise
        """
        # Parse standard ID (format: grade.domain.cluster.standard)
        parts = standard_id.split(".")
        if len(parts) < 2:
            logger.warning(f"Invalid standard ID format: {standard_id}")
            return None
        
        grade = parts[0]
        domain = parts[1]
        
        standards = self.get_domain_standards(grade, domain)
        for standard in standards:
            if standard.get("id") == standard_id:
                return standard
        
        return None
    
    def get_all_standards_for_grade(self, grade: str) -> List[Dict]:
        """
        Get all standards for a grade level across all domains.
        
        Args:
            grade: Grade level
            
        Returns:
            List[Dict]: All standards for the grade level
        """
        all_standards = []
        domains = self.get_domains(grade)
        
        for domain_code, domain_data in domains.items():
            standards = domain_data.get("standards", [])
            for standard in standards:
                standard_with_domain = standard.copy()
                standard_with_domain["domain"] = domain_code
                standard_with_domain["domain_name"] = domain_data.get("name", "")
                all_standards.append(standard_with_domain)
        
        return all_standards
    
    def get_metadata(self) -> Dict:
        """
        Get standards metadata.
        
        Returns:
            Dict: Metadata about the standards
        """
        return self.standards_data.get("metadata", {})


# Create default loader instance
default_loader = StandardsLoader()

"""
Standards Lookup Tool for querying CCSSM standards.
"""

from typing import Optional
from crewai.tools import BaseTool
from pydantic import Field
import json

from ..utils.standards_loader import StandardsLoader
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


class StandardsLookupTool(BaseTool):
    """
    Tool for looking up Common Core State Standards for Mathematics (CCSSM).
    Provides access to standards by grade level, domain, and standard ID.
    """
    
    name: str = "Standards Lookup"
    description: str = (
        "Looks up Common Core State Standards for Mathematics (CCSSM). "
        "Can retrieve standards by grade level (K-12), domain (e.g., OA, NBT, NF), "
        "or specific standard ID (e.g., 3.OA.A.1). "
        "Also provides access to the 8 Standards for Mathematical Practice. "
        "Input can be: 'grade:3', 'standard:3.OA.A.1', 'practices', or 'domain:3.OA'"
    )
    
    standards_loader: StandardsLoader = Field(default_factory=StandardsLoader)
    
    def _run(self, query: str) -> str:
        """
        Look up standards based on query.
        
        Args:
            query: Query string (e.g., 'grade:3', 'standard:3.OA.A.1', 'practices')
            
        Returns:
            str: JSON string with standards information
        """
        try:
            query = query.strip().lower()
            
            # Handle mathematical practices
            if query == 'practices' or query == 'mathematical practices':
                practices = self.standards_loader.get_mathematical_practices()
                result = {
                    "success": True,
                    "query": query,
                    "type": "mathematical_practices",
                    "count": len(practices),
                    "data": practices
                }
                logger.info("Retrieved mathematical practices")
                return json.dumps(result, indent=2)
            
            # Handle grade level query
            if query.startswith('grade:'):
                grade = query.split(':', 1)[1].strip().upper()
                standards = self.standards_loader.get_all_standards_for_grade(grade)
                domains = self.standards_loader.get_domains(grade)
                
                result = {
                    "success": True,
                    "query": query,
                    "type": "grade_level",
                    "grade": grade,
                    "domain_count": len(domains),
                    "standards_count": len(standards),
                    "domains": list(domains.keys()),
                    "standards": standards
                }
                logger.info(f"Retrieved {len(standards)} standards for grade {grade}")
                return json.dumps(result, indent=2)
            
            # Handle specific standard query
            if query.startswith('standard:'):
                standard_id = query.split(':', 1)[1].strip().upper()
                standard = self.standards_loader.search_standard(standard_id)
                
                if standard:
                    result = {
                        "success": True,
                        "query": query,
                        "type": "specific_standard",
                        "standard_id": standard_id,
                        "data": standard
                    }
                    logger.info(f"Found standard: {standard_id}")
                else:
                    result = {
                        "success": False,
                        "query": query,
                        "error": f"Standard not found: {standard_id}"
                    }
                    logger.warning(f"Standard not found: {standard_id}")
                
                return json.dumps(result, indent=2)
            
            # Handle domain query
            if query.startswith('domain:'):
                parts = query.split(':', 1)[1].strip().split('.')
                if len(parts) >= 2:
                    grade = parts[0].upper()
                    domain = parts[1].upper()
                    
                    standards = self.standards_loader.get_domain_standards(grade, domain)
                    domains = self.standards_loader.get_domains(grade)
                    domain_info = domains.get(domain, {})
                    
                    result = {
                        "success": True,
                        "query": query,
                        "type": "domain",
                        "grade": grade,
                        "domain": domain,
                        "domain_name": domain_info.get("name", "Unknown"),
                        "standards_count": len(standards),
                        "standards": standards
                    }
                    logger.info(f"Retrieved {len(standards)} standards for domain {grade}.{domain}")
                    return json.dumps(result, indent=2)
            
            # Unknown query format
            result = {
                "success": False,
                "query": query,
                "error": "Invalid query format. Use: 'grade:3', 'standard:3.OA.A.1', 'practices', or 'domain:3.OA'"
            }
            return json.dumps(result, indent=2)
            
        except Exception as e:
            logger.error(f"Error looking up standards: {e}")
            return json.dumps({
                "success": False,
                "query": query,
                "error": str(e)
            })


# Create tool instance for easy import
standards_lookup_tool = StandardsLookupTool()

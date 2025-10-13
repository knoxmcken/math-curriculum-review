"""
Report Generation Tool for creating formatted review reports.
"""

from typing import Optional, Dict, Any
from pathlib import Path
from datetime import datetime
from crewai.tools import BaseTool
from pydantic import Field
import json

from ..utils.config import Config
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


class ReportGeneratorTool(BaseTool):
    """
    Tool for generating formatted curriculum review reports.
    Creates reports in Markdown, HTML, or plain text format.
    """
    
    name: str = "Report Generator"
    description: str = (
        "Generates formatted curriculum review reports. "
        "Creates professional reports in Markdown, HTML, or text format. "
        "Input should be a JSON string with 'title', 'content', 'format' (md/html/txt), "
        "and optional 'filename'. Example: {\"title\": \"Review Report\", \"content\": {...}, \"format\": \"md\"}"
    )
    
    def _run(self, report_data: str) -> str:
        """
        Generate a formatted report.
        
        Args:
            report_data: JSON string with report information
            
        Returns:
            str: Path to generated report file or error message
        """
        try:
            data = json.loads(report_data)
            
            title = data.get('title', 'Curriculum Review Report')
            content = data.get('content', {})
            format_type = data.get('format', 'md').lower()
            filename = data.get('filename', self._generate_filename(format_type))
            
            # Generate report based on format
            if format_type == 'md' or format_type == 'markdown':
                report_content = self._generate_markdown(title, content)
            elif format_type == 'html':
                report_content = self._generate_html(title, content)
            elif format_type == 'txt' or format_type == 'text':
                report_content = self._generate_text(title, content)
            else:
                return json.dumps({
                    "success": False,
                    "error": f"Unsupported format: {format_type}. Use 'md', 'html', or 'txt'"
                })
            
            # Save report to file
            output_path = Config.OUTPUT_DIR / filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            result = {
                "success": True,
                "file_path": str(output_path),
                "filename": filename,
                "format": format_type,
                "size_bytes": len(report_content)
            }
            
            logger.info(f"Generated report: {filename}")
            return json.dumps(result, indent=2)
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON input: {e}")
            return json.dumps({
                "success": False,
                "error": f"Invalid JSON input: {str(e)}"
            })
        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return json.dumps({
                "success": False,
                "error": str(e)
            })
    
    def _generate_filename(self, format_type: str) -> str:
        """Generate a timestamped filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"curriculum_review_{timestamp}.{format_type}"
    
    def _generate_markdown(self, title: str, content: Dict[str, Any]) -> str:
        """Generate Markdown report."""
        lines = [
            f"# {title}",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "---",
            ""
        ]
        
        # Add content sections
        for section, data in content.items():
            lines.append(f"## {section.replace('_', ' ').title()}")
            lines.append("")
            
            if isinstance(data, dict):
                for key, value in data.items():
                    lines.append(f"**{key.replace('_', ' ').title()}:** {value}")
                    lines.append("")
            elif isinstance(data, list):
                for item in data:
                    lines.append(f"- {item}")
                lines.append("")
            else:
                lines.append(str(data))
                lines.append("")
        
        return "\n".join(lines)
    
    def _generate_html(self, title: str, content: Dict[str, Any]) -> str:
        """Generate HTML report."""
        lines = [
            "<!DOCTYPE html>",
            "<html>",
            "<head>",
            f"    <title>{title}</title>",
            "    <style>",
            "        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }",
            "        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }",
            "        h2 { color: #34495e; margin-top: 30px; }",
            "        .metadata { color: #7f8c8d; font-style: italic; }",
            "        .section { margin: 20px 0; }",
            "        ul { line-height: 1.8; }",
            "    </style>",
            "</head>",
            "<body>",
            f"    <h1>{title}</h1>",
            f"    <p class='metadata'>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>",
            "    <hr>"
        ]
        
        for section, data in content.items():
            lines.append(f"    <div class='section'>")
            lines.append(f"        <h2>{section.replace('_', ' ').title()}</h2>")
            
            if isinstance(data, dict):
                lines.append("        <ul>")
                for key, value in data.items():
                    lines.append(f"            <li><strong>{key.replace('_', ' ').title()}:</strong> {value}</li>")
                lines.append("        </ul>")
            elif isinstance(data, list):
                lines.append("        <ul>")
                for item in data:
                    lines.append(f"            <li>{item}</li>")
                lines.append("        </ul>")
            else:
                lines.append(f"        <p>{data}</p>")
            
            lines.append("    </div>")
        
        lines.extend([
            "</body>",
            "</html>"
        ])
        
        return "\n".join(lines)
    
    def _generate_text(self, title: str, content: Dict[str, Any]) -> str:
        """Generate plain text report."""
        lines = [
            "=" * 80,
            title.center(80),
            "=" * 80,
            "",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "-" * 80,
            ""
        ]
        
        for section, data in content.items():
            lines.append(section.replace('_', ' ').title().upper())
            lines.append("-" * 40)
            
            if isinstance(data, dict):
                for key, value in data.items():
                    lines.append(f"{key.replace('_', ' ').title()}: {value}")
            elif isinstance(data, list):
                for item in data:
                    lines.append(f"  • {item}")
            else:
                lines.append(str(data))
            
            lines.append("")
        
        lines.append("=" * 80)
        
        return "\n".join(lines)


# Create tool instance for easy import
report_generator_tool = ReportGeneratorTool()

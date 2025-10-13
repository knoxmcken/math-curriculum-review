"""
Document Analysis Tool for curriculum materials.
Parses and extracts content from various document formats.
"""

from typing import Optional, Dict, Any
from pathlib import Path
from crewai.tools import BaseTool
from pydantic import Field
import json

from ..utils.logger import setup_logger

logger = setup_logger(__name__)


class DocumentAnalyzerTool(BaseTool):
    """
    Tool for analyzing curriculum documents.
    Extracts text content, structure, and metadata from PDF, DOCX, TXT, and HTML files.
    """
    
    name: str = "Document Analyzer"
    description: str = (
        "Analyzes curriculum documents and extracts content, structure, and metadata. "
        "Supports PDF, DOCX, TXT, HTML, and Markdown files. "
        "Use this tool when you need to read and analyze curriculum materials. "
        "Input should be a file path."
    )
    
    def _run(self, file_path: str) -> str:
        """
        Analyze a document and extract its content.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            str: JSON string with extracted content and metadata
        """
        try:
            path = Path(file_path)
            
            if not path.exists():
                return json.dumps({
                    "error": f"File not found: {file_path}",
                    "success": False
                })
            
            # Determine file type and extract content
            extension = path.suffix.lower()
            
            if extension == '.txt':
                content = self._extract_text(path)
            elif extension == '.md':
                content = self._extract_markdown(path)
            elif extension == '.pdf':
                content = self._extract_pdf(path)
            elif extension in ['.docx', '.doc']:
                content = self._extract_docx(path)
            elif extension in ['.html', '.htm']:
                content = self._extract_html(path)
            else:
                return json.dumps({
                    "error": f"Unsupported file type: {extension}",
                    "success": False
                })
            
            result = {
                "success": True,
                "file_path": str(path),
                "file_name": path.name,
                "file_type": extension,
                "content": content,
                "length": len(content),
                "metadata": {
                    "size_bytes": path.stat().st_size,
                    "extension": extension
                }
            }
            
            logger.info(f"Successfully analyzed document: {path.name}")
            return json.dumps(result, indent=2)
            
        except Exception as e:
            logger.error(f"Error analyzing document: {e}")
            return json.dumps({
                "error": str(e),
                "success": False
            })
    
    def _extract_text(self, path: Path) -> str:
        """Extract content from plain text file."""
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    
    def _extract_markdown(self, path: Path) -> str:
        """Extract content from Markdown file."""
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    
    def _extract_pdf(self, path: Path) -> str:
        """Extract text from PDF file."""
        try:
            import pdfplumber
            
            text_content = []
            with pdfplumber.open(path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        text_content.append(f"--- Page {page_num} ---\n{text}")
            
            return "\n\n".join(text_content)
            
        except ImportError:
            return "Error: pdfplumber not installed. Install with: pip install pdfplumber"
        except Exception as e:
            return f"Error extracting PDF: {str(e)}"
    
    def _extract_docx(self, path: Path) -> str:
        """Extract text from DOCX file."""
        try:
            from docx import Document
            
            doc = Document(path)
            paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
            return "\n\n".join(paragraphs)
            
        except ImportError:
            return "Error: python-docx not installed. Install with: pip install python-docx"
        except Exception as e:
            return f"Error extracting DOCX: {str(e)}"
    
    def _extract_html(self, path: Path) -> str:
        """Extract text from HTML file."""
        try:
            from bs4 import BeautifulSoup
            
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
            
        except ImportError:
            return "Error: beautifulsoup4 not installed. Install with: pip install beautifulsoup4"
        except Exception as e:
            return f"Error extracting HTML: {str(e)}"


# Create tool instance for easy import
document_analyzer_tool = DocumentAnalyzerTool()

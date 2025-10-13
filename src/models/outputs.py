"""
Pydantic models for structured agent outputs.
Following patterns from L5 reference notebook.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime


class StandardsAlignmentOutput(BaseModel):
    """Output model for Standards Analyst Agent."""
    
    grade_level: str = Field(..., description="Target grade level (e.g., '3', 'K', '8')")
    standards_covered: List[str] = Field(
        default_factory=list,
        description="List of CCSSM standard IDs covered in the curriculum"
    )
    standards_missing: List[str] = Field(
        default_factory=list,
        description="List of expected CCSSM standards not covered"
    )
    alignment_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall alignment score (0-100)"
    )
    detailed_mapping: Dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of standards to curriculum locations"
    )
    recommendations: List[str] = Field(
        default_factory=list,
        description="Recommendations for improving standards alignment"
    )
    timestamp: datetime = Field(default_factory=datetime.now)


class GradeLevelCheckOutput(BaseModel):
    """Output model for Grade Level Standards Checker Agent."""
    
    grade_level: str = Field(..., description="Target grade level")
    appropriateness_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Grade-level appropriateness score (0-100)"
    )
    too_advanced_topics: List[str] = Field(
        default_factory=list,
        description="Topics that are too advanced for the grade level"
    )
    too_basic_topics: List[str] = Field(
        default_factory=list,
        description="Topics that are too basic for the grade level"
    )
    appropriate_topics: List[str] = Field(
        default_factory=list,
        description="Topics at appropriate level"
    )
    scaffolding_quality: str = Field(
        ...,
        description="Assessment of scaffolding between topics (Excellent/Good/Fair/Poor)"
    )
    recommendations: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)


class MathPracticesOutput(BaseModel):
    """Output model for Mathematical Practices Evaluator Agent."""
    
    practice_scores: Dict[str, float] = Field(
        default_factory=dict,
        description="Scores for each of the 8 mathematical practices (MP1-MP8)"
    )
    overall_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall mathematical practices score"
    )
    strengths: List[str] = Field(
        default_factory=list,
        description="Strong areas in mathematical practice development"
    )
    weaknesses: List[str] = Field(
        default_factory=list,
        description="Weak areas needing improvement"
    )
    practice_opportunities: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Identified opportunities for each practice"
    )
    recommendations: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)


class ContentQualityOutput(BaseModel):
    """Output model for Content Reviewer Agent."""
    
    mathematical_accuracy: float = Field(
        ...,
        ge=0,
        le=100,
        description="Mathematical accuracy score"
    )
    clarity_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Clarity and explanation quality score"
    )
    conceptual_understanding: float = Field(
        ...,
        ge=0,
        le=100,
        description="Support for conceptual understanding"
    )
    procedural_fluency: float = Field(
        ...,
        ge=0,
        le=100,
        description="Development of procedural fluency"
    )
    application_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Real-world application and problem-solving"
    )
    overall_quality: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall content quality score"
    )
    strengths: List[str] = Field(default_factory=list)
    weaknesses: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)


class PedagogicalEffectivenessOutput(BaseModel):
    """Output model for Pedagogical Effectiveness Analyst Agent."""
    
    instructional_design_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Quality of instructional design"
    )
    scaffolding_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Quality of scaffolding and support"
    )
    differentiation_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Support for diverse learners"
    )
    engagement_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Student engagement potential"
    )
    formative_assessment_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Formative assessment opportunities"
    )
    overall_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall pedagogical effectiveness"
    )
    teaching_strategies: List[str] = Field(
        default_factory=list,
        description="Identified teaching strategies"
    )
    recommendations: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)


class EquityAccessibilityOutput(BaseModel):
    """Output model for Equity & Accessibility Reviewer Agent."""
    
    cultural_responsiveness: float = Field(
        ...,
        ge=0,
        le=100,
        description="Cultural responsiveness and representation score"
    )
    accessibility_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Accessibility for students with disabilities"
    )
    ell_support_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Support for English Language Learners"
    )
    udl_compliance: float = Field(
        ...,
        ge=0,
        le=100,
        description="Universal Design for Learning compliance"
    )
    overall_equity_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall equity and accessibility score"
    )
    representation_analysis: List[str] = Field(
        default_factory=list,
        description="Analysis of cultural representation"
    )
    barriers_identified: List[str] = Field(
        default_factory=list,
        description="Identified barriers to access"
    )
    recommendations: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)


class AssessmentQualityOutput(BaseModel):
    """Output model for Assessment Quality Evaluator Agent."""
    
    alignment_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Alignment with content and standards"
    )
    question_quality_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Quality of assessment questions"
    )
    variety_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Variety of question types and formats"
    )
    validity_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Assessment validity"
    )
    accessibility_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Accessibility and fairness"
    )
    overall_quality: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall assessment quality"
    )
    assessment_types: List[str] = Field(
        default_factory=list,
        description="Types of assessments included"
    )
    strengths: List[str] = Field(default_factory=list)
    weaknesses: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)


class FinalReviewReport(BaseModel):
    """Comprehensive final review report from QA & Report Generator Agent."""
    
    curriculum_title: str = Field(..., description="Title of curriculum being reviewed")
    grade_level: str = Field(..., description="Target grade level")
    review_date: datetime = Field(default_factory=datetime.now)
    
    # Overall scores
    overall_rating: float = Field(
        ...,
        ge=0,
        le=100,
        description="Overall curriculum rating"
    )
    standards_alignment_score: float = Field(..., ge=0, le=100)
    content_quality_score: float = Field(..., ge=0, le=100)
    pedagogical_score: float = Field(..., ge=0, le=100)
    equity_score: float = Field(..., ge=0, le=100)
    assessment_score: float = Field(..., ge=0, le=100)
    
    # Detailed findings
    key_strengths: List[str] = Field(
        default_factory=list,
        description="Top 5 strengths of the curriculum"
    )
    key_weaknesses: List[str] = Field(
        default_factory=list,
        description="Top 5 areas for improvement"
    )
    
    # Prioritized recommendations
    critical_recommendations: List[str] = Field(
        default_factory=list,
        description="Must-address recommendations"
    )
    important_recommendations: List[str] = Field(
        default_factory=list,
        description="Important recommendations"
    )
    suggested_improvements: List[str] = Field(
        default_factory=list,
        description="Nice-to-have improvements"
    )
    
    # Detailed section references
    standards_analysis: Optional[StandardsAlignmentOutput] = None
    content_review: Optional[ContentQualityOutput] = None
    pedagogical_analysis: Optional[PedagogicalEffectivenessOutput] = None
    equity_review: Optional[EquityAccessibilityOutput] = None
    assessment_review: Optional[AssessmentQualityOutput] = None
    
    # Summary
    executive_summary: str = Field(
        ...,
        description="Executive summary of the review (2-3 paragraphs)"
    )
    recommendation_summary: str = Field(
        ...,
        description="Summary of top recommendations"
    )
    
    # Metadata
    reviewer_notes: Optional[str] = None
    review_metadata: Dict[str, str] = Field(default_factory=dict)


class TaskInput(BaseModel):
    """Generic input model for tasks."""
    
    curriculum_content: str = Field(..., description="Curriculum content to analyze")
    grade_level: str = Field(..., description="Target grade level")
    additional_context: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        description="Additional context for the analysis"
    )

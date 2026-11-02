"""
================================================================================
GrantLens Compliance & Audit Engine - API Schemas (Pydantic Models)
================================================================================
Project: GrantLens (CSE299 Section 3, Group 2)
Milestone: Week 3 - Gemini AI API Integration & Full-Stack Portal
Author: Hasin Anzum Inan, Anas Ibne Majbha, Tazreen Alam, Israt Jahan Susmi
================================================================================
Defines strict Pydantic v2 data transfer objects (DTOs) for incoming request
payloads and outgoing JSON responses. Ensures deterministic serialization,
boundary validation, and OpenAPI Swagger documentation generation.
================================================================================
"""

import uuid
from datetime import datetime
from decimal import Decimal
from typing import Any, List, Optional
from pydantic import BaseModel, EmailStr, Field


# ==============================================================================
# 1. AUTHENTICATION & RESEARCHER SCHEMAS
# ==============================================================================

class UserRegisterRequest(BaseModel):
    """
    Validates institutional user registration requests.
    Requires minimum password complexity and academic metadata.
    """
    email: EmailStr = Field(
        ...,
        description="Institutional academic email address",
        example="researcher@university.edu"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password must contain at least 8 characters",
    )
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=255,
        description="Full academic legal name of researcher"
    )
    institution: str = Field(
        ...,
        min_length=2,
        max_length=255,
        description="University or Research Laboratory name"
    )
    department: Optional[str] = Field(
        None,
        max_length=255,
        description="Academic department or faculty division"
    )


class UserLoginRequest(BaseModel):
    """
    Payload for researcher session login.
    """
    email: EmailStr = Field(..., description="Registered institutional email")
    password: str = Field(..., description="Plaintext password for Bcrypt verification")


class UserResponse(BaseModel):
    """
    Public researcher profile returned upon login or /auth/me session probe.
    (Hashed passwords are never leaked in API responses).
    """
    id: uuid.UUID
    email: str
    full_name: str
    institution: str
    department: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """
    RFC 6749 compliant JWT bearer token response.
    Includes access token (60m) and refresh token (7d).
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse


# ==============================================================================
# 2. HEURISTIC AUDIT SCHEMAS (Week 2 Rule Engine)
# ==============================================================================

class FindingResponse(BaseModel):
    """
    Represents an individual formatting finding detected by PyMuPDF or pdfplumber.
    """
    id: uuid.UUID
    severity: str = Field(..., description="RED | YELLOW | GREEN")
    category: str = Field(..., description="PAGE_LIMIT | FONT_MARGIN | BUDGET | MANDATORY_SECTION")
    message: str = Field(..., description="Detailed diagnostic description of violation")
    remediation_advice: str = Field(..., description="Actionable step to fix violation")


class SubmissionUploadResponse(BaseModel):
    """
    Immediate response returned when a dual-document grant package is uploaded.
    Contains ingestion statistics and preliminary heuristic compliance scores.
    """
    submission_id: uuid.UUID
    title: str
    funding_agency: str
    solicitation_pages: int
    proposal_pages: int
    total_budget_extracted: Decimal
    audit_score: float
    audit_status: str
    institutional_signoff_ready: bool
    findings_count: int
    findings: List[FindingResponse]


# ==============================================================================
# 3. [NEW WEEK 3] GEMINI AI NARRATIVE REVIEW SCHEMAS
# ==============================================================================

class RubricScoresSchema(BaseModel):
    """
    Granular 0-100 rubric scores evaluated by Gemini according to NSF/NIH guidelines.
    """
    intellectual_merit: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Scientific rigor, innovation, and soundness of methodology"
    )
    broader_impacts: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Societal benefit, STEM education reach, and diversity integration"
    )
    solicitation_alignment: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Direct adherence to specific call requirements and constraints"
    )
    budget_feasibility: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Clarity of resource allocation and budget narrative alignment"
    )


class SectionCritiqueSchema(BaseModel):
    """
    Detailed section-level critique identifying weaknesses and providing
    a concrete publication-grade suggested rewrite.
    """
    section_name: str = Field(..., description="Name of proposal section, e.g. 'Broader Impacts'")
    status: str = Field(..., description="NEEDS_IMPROVEMENT | COMPLIANT | DEFICIENT")
    severity: str = Field(..., description="RED | YELLOW | GREEN")
    score: float = Field(..., ge=0.0, le=100.0, description="Section sub-score")
    identified_weakness: str = Field(..., description="Concise analysis of what is missing or weak")
    original_excerpt: str = Field(..., description="Problematic excerpt from proposal manuscript")
    suggested_rewrite: str = Field(..., description="Publication-ready rewritten text suggested by Gemini")
    remediation_rationale: str = Field(..., description="Why this revision satisfies the agency guideline")


class AIReviewResponse(BaseModel):
    """
    Full response model for an AI narrative audit returned to the React frontend.
    """
    id: uuid.UUID
    submission_id: uuid.UUID
    model_version: str
    overall_composite_score: float
    panel_recommendation: str
    rubric_scores: RubricScoresSchema
    executive_summary: str
    section_critiques: List[SectionCritiqueSchema]
    created_at: datetime

    class Config:
        from_attributes = True


class AIRewriteRequest(BaseModel):
    """
    Payload for on-demand paragraph rewriting in the interactive playground.
    """
    section_name: str = Field(..., description="Section title, e.g. 'Project Summary'")
    draft_text: str = Field(..., min_length=20, description="Raw text excerpt to polish")
    target_guideline: Optional[str] = Field(
        "NSF 24-500",
        description="Target agency solicitation standard"
    )
    custom_instructions: Optional[str] = Field(
        "Make it more compelling and quantitatively rigorous for the panel",
        description="Specific guidance for the LLM"
    )


class AIRewriteResponse(BaseModel):
    """
    Response model for an interactive on-demand section rewrite.
    """
    section_name: str
    original_text: str
    rewritten_text: str
    key_improvements: List[str]
    model_used: str

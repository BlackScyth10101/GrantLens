import uuid
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=255)
    institution: str = Field(min_length=2, max_length=255)
    department: Optional[str] = None


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str
    institution: str
    department: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse


class FindingResponse(BaseModel):
    id: uuid.UUID
    severity: str
    category: str
    message: str
    remediation_advice: str


class SubmissionUploadResponse(BaseModel):
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

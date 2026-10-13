import enum
import uuid
from datetime import datetime
from decimal import Decimal
from typing import Any, List, Optional
from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.types import JSON, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class DocumentType(str, enum.Enum):
    SOLICITATION = "SOLICITATION"
    DRAFT_PROPOSAL = "DRAFT_PROPOSAL"


class AuditStatus(str, enum.Enum):
    PASSED = "PASSED"
    WARNINGS = "WARNINGS"
    FAILED = "FAILED"


class FindingSeverity(str, enum.Enum):
    RED = "RED"          # Fatal desk-rejection violation
    YELLOW = "YELLOW"    # Warning / high discrepancy
    GREEN = "GREEN"      # Passed audit rule


class FindingCategory(str, enum.Enum):
    PAGE_LIMIT = "PAGE_LIMIT"
    FONT_MARGIN = "FONT_MARGIN"
    BUDGET = "BUDGET"
    MANDATORY_SECTION = "MANDATORY_SECTION"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    institution: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    department: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    submissions: Mapped[List["GrantSubmission"]] = relationship(
        "GrantSubmission",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class GrantSubmission(Base):
    __tablename__ = "grant_submissions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    funding_agency: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    status: Mapped[str] = mapped_column(
        String(50),
        default="INGESTED",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship("User", back_populates="submissions")
    documents: Mapped[List["Document"]] = relationship(
        "Document",
        back_populates="submission",
        cascade="all, delete-orphan",
    )
    audit_reports: Mapped[List["AuditReport"]] = relationship(
        "AuditReport",
        back_populates="submission",
        cascade="all, delete-orphan",
    )
    budget_items: Mapped[List["BudgetLineItem"]] = relationship(
        "BudgetLineItem",
        back_populates="submission",
        cascade="all, delete-orphan",
    )


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    submission_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("grant_submissions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    doc_type: Mapped[DocumentType] = mapped_column(
        Enum(DocumentType, name="document_type_enum"),
        nullable=False,
    )
    file_path: Mapped[str] = mapped_column(String(1024), nullable=False)
    file_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, nullable=False)
    extracted_metadata: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        nullable=False,
        default=dict,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    submission: Mapped["GrantSubmission"] = relationship(
        "GrantSubmission",
        back_populates="documents",
    )

    __table_args__ = (
        Index("ix_documents_submission_doc_type", "submission_id", "doc_type"),
    )


class AuditReport(Base):
    __tablename__ = "audit_reports"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    submission_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("grant_submissions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    total_score: Mapped[float] = mapped_column(Float, default=100.0, nullable=False)
    status: Mapped[AuditStatus] = mapped_column(
        Enum(AuditStatus, name="audit_status_enum"),
        default=AuditStatus.PASSED,
        nullable=False,
    )
    institutional_signoff_ready: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    submission: Mapped["GrantSubmission"] = relationship(
        "GrantSubmission",
        back_populates="audit_reports",
    )
    findings: Mapped[List["AuditFinding"]] = relationship(
        "AuditFinding",
        back_populates="audit_report",
        cascade="all, delete-orphan",
    )


class AuditFinding(Base):
    __tablename__ = "audit_findings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    audit_report_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("audit_reports.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    severity: Mapped[FindingSeverity] = mapped_column(
        Enum(FindingSeverity, name="finding_severity_enum"),
        nullable=False,
        index=True,
    )
    category: Mapped[FindingCategory] = mapped_column(
        Enum(FindingCategory, name="finding_category_enum"),
        nullable=False,
        index=True,
    )
    message: Mapped[str] = mapped_column(Text, nullable=False)
    remediation_advice: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    audit_report: Mapped["AuditReport"] = relationship(
        "AuditReport",
        back_populates="findings",
    )


class BudgetLineItem(Base):
    __tablename__ = "budget_line_items"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    submission_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("grant_submissions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    category: Mapped[str] = mapped_column(String(255), nullable=False)
    requested_amount: Mapped[Decimal] = mapped_column(
        Numeric(14, 2),
        nullable=False,
    )
    allowed_cap: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(14, 2),
        nullable=True,
    )
    variance: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(14, 2),
        nullable=True,
    )
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    submission: Mapped["GrantSubmission"] = relationship(
        "GrantSubmission",
        back_populates="budget_items",
    )

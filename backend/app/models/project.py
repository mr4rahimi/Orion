from __future__ import annotations

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class Project(BaseModel):
    __tablename__ = "projects"

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    workspace_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
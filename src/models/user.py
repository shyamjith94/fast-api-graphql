from src.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

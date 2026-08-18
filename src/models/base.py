from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import DateTime, func, Integer
from datetime import datetime


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    update_date: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now())

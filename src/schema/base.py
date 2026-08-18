from pydantic import BaseModel, ConfigDict
from datetime import datetime
from dataclasses import dataclass


@dataclass
class BaseResponseSchema:
    id: int
    create_date: datetime
    update_date: datetime


@dataclass
class BaseRequestSchema:
    pass


class RequestBaseModel(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: int | None = None
    create_date: datetime | None = None
    update_date: datetime | None = None

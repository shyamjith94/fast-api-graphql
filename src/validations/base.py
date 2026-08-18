from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.constants.shared import T


class BaseValidation(ABC, Generic[T]):

    @classmethod
    @abstractmethod
    def validate(cls, data) -> T:
        pass

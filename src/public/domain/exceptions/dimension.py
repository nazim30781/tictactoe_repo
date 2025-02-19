from dataclasses import dataclass

from src.public.domain.exceptions.base import EntityException


@dataclass(eq=False)
class NotValidBoardSizeException(EntityException):
    @property
    def message(self) -> str:
        return "Values in board size must be equels"

from src.public.domain.exceptions.base import EntityException


class IndexIsNotInBoardError(EntityException):
    @property
    def message(self) -> str:
        return "row or column index is not at this board"

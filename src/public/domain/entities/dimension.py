from dataclasses import dataclass

from src.public.domain.exceptions.dimension import NotValidBoardSizeException


@dataclass
class Dimension:
    rows: int
    cols: int

    def __post_init__(self):
        if self.rows != self.cols:
            raise NotValidBoardSizeException()

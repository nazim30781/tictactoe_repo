from dataclasses import dataclass
from src.public.domain.enums.cell_value import CellValue


@dataclass
class Cell:
    cell_value: CellValue

    def __repr__(self) -> str:
        return self.cell_value

    def __str__(self) -> str:
        return self.cell_value

    def __hash__(self):
        return hash(self.cell_value)

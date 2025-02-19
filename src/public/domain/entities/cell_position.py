from dataclasses import dataclass


@dataclass
class CellPosition:
    row_idx: int
    col_idx: int

    def __str__(self) -> str:
        return f"x: {self.row_idx} y: {self.col_idx}"

    def __hash__(self):
        return hash((self.row_idx, self.col_idx))

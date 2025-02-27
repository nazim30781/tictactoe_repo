from __future__ import annotations

from src.public.domain.entities.cell import Cell
from src.public.domain.entities.cell_position import CellPosition
from src.public.domain.entities.dimension import Dimension
from src.public.domain.enums.cell_value import CellValue
from src.public.domain.exceptions.board import IndexIsNotInBoardError


class Board:
    def __init__(self, cells: list[list[Cell]]):
        self.__cells = cells

    @property
    def cells(self) -> list[list[Cell]]:
        return self.__cells

    def get_empty_cells(self) -> list[CellPosition]:
        cells = list()

        for row in self.__cells:
            for col in row:
                if self.__cells[row, col].cell_value == CellValue.E:
                    cells.append(CellPosition(row, col))

        return cells

    @classmethod
    def create(cls, dimension: Dimension) -> Board:
        default_value = CellValue.E

        row_count = dimension.rows
        col_count = dimension.cols

        cells: list[list[Cell]] = [
            [Cell(default_value) for col in range(col_count)] for _ in range(row_count)
        ]

        return cls(cells)

    def set_value(self, row_idx, col_idx, value):
        if (
            self.__cells[row_idx][col_idx] is not None
            and self.__cells[row_idx][col_idx].cell_value == CellValue.E
        ):
            self.__cells[row_idx][col_idx].cell_value = value
        else:
            raise IndexIsNotInBoardError()

    # winner check

    def check_winner(self):
        if winner := self.check_horizontal_win():
            return winner
        if winner := self.check_vertical_win():
            return winner
        if winner := self.check_diagonal_win():
            return winner

        return False

    def check_horizontal_win(self) -> bool | str:
        for row in self.__cells:
            if result := self.check_values_list(row):
                return result

        return False

    def check_vertical_win(self) -> bool | str:
        idx = 0
        for _ in range(len(self.__cells)):
            values = []
            for row in self.cells:
                if row[idx] == CellValue.E:
                    break
                values.append(row[idx])

            if result := self.check_values_list(values):
                return result

            idx += 1

        return False

    def check_diagonal_win(self) -> bool | str:
        row1 = col1 = 0
        values1 = []

        for i in range(len(self.__cells)):
            values1.append(self.__cells[row1][col1])

            row1 += 1
            col1 += 1

        if result := self.check_values_list(values1):
            return result

        row2 = len(self.__cells) - 1
        col2 = 0
        values2 = []

        for i in range(len(self.__cells)):
            values2.append(self.__cells[row2][col2])

            row2 -= 1
            col2 += 1

        if result := self.check_values_list(values2):
            return result

    def check_values_list(self, values: list[Cell]):
        if len(set(values)) == 1 and values[0].cell_value != CellValue.E:
            return values[0]

        return False

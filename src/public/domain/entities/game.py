from dataclasses import dataclass, field

from src.public.domain.entities import board
from src.public.domain.entities.base import BaseEntity
from src.public.domain.entities.board import Board
from src.public.domain.entities.player import Player
from src.public.domain.enums.cell_value import CellValue


@dataclass
class Game(BaseEntity):
    player_1: Player | None = field(default=None)
    player_2: Player | None = field(default=None)
    board: Board | None = field(default=None)
    current_cell_value: str | None = field(default=None)

    def start(self, first_cell_value: str = CellValue.X):
        self.current_cell_value = first_cell_value
        cell_values = CellValue.get_random_values()

        self.player_1.cell_value = cell_values[0]
        self.player_2.cell_value = cell_values[1]

        return self

    def move(self):
        if self.current_cell_value == CellValue.O:
            self.current_cell_value = CellValue.X
        else:
            self.current_cell_value = CellValue.O

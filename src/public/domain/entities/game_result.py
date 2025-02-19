from dataclasses import dataclass

from src.public.domain.entities.board import Board
from src.public.domain.entities.player import Player


@dataclass
class GameResult:
    winner_value: str | None
    board: Board

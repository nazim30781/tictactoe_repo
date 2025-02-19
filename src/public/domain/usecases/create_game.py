from src.public.domain.entities.game import Game
from src.public.domain.entities.player import Player
from src.public.domain.interfaces.repositories.game import GameRepository
from src.public.domain.usecases.base import BaseUsecase


class GameCreateUsecase(BaseUsecase):
    def __init__(self, game_repository: GameRepository): ...

    async def execute(self) -> str:
        game = Game()

        return game.oid

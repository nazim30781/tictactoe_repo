from src.public.domain.entities.board import Board
from src.public.domain.entities.dimension import Dimension
from src.public.domain.entities.game import Game
from src.public.domain.entities.player import Player
from src.public.domain.interfaces.repositories.game import GameRepository
from src.public.domain.usecases.base import BaseUsecase


class GameStartUsecase(BaseUsecase):
    def __init__(self, game_repository: GameRepository):
        self._game_repository = game_repository

    async def execute(
        self,
        oid: str,
        player_1: Player,
        player_2: Player,
        dimension: Dimension,
    ):
        board = Board.create(dimension=dimension)
        game = Game(
            oid=oid,
            player_1=player_1,
            player_2=player_2,
            board=board,
        ).start()

        await self._game_repository.save_game(game)

        return game

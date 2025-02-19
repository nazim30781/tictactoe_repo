from src.public.domain.entities.game_result import GameResult
from src.public.domain.entities.player import Player
from src.public.domain.interfaces.repositories.game import GameRepository
from src.public.domain.usecases.base import BaseUsecase


class CheckWinUsecase(BaseUsecase):
    def __init__(self, game_repository: GameRepository):
        self._game_repository = game_repository

    async def execute(self, game_oid: str) -> GameResult | bool:
        game = await self._game_repository.get_game(game_oid)

        winner = game.board.check_winner()

        if winner:
            result = GameResult(winner, game.board)

            return result

        return False

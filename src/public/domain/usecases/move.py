from src.public.domain.interfaces.repositories.game import GameRepository
from src.public.domain.usecases.base import BaseUsecase


class MoveUsecase(BaseUsecase):
    def __init__(self, game_repository: GameRepository):
        self._game_repository = game_repository

    async def execute(
        self,
        game_oid: str,
        player_cell_value: str,
        row_idx: int,
        col_idx: int,
    ):
        game = await self._game_repository.get_game(game_oid)

        if game.current_cell_value == player_cell_value:
            game.board.set_value(row_idx, col_idx, game.current_cell_value)
            game.move()
            await self._game_repository.update_game_after_move(game)

            return game

from src.public.domain.interfaces.repositories.game import GameRepository
from src.public.domain.usecases.check_win import CheckWinUsecase
from src.public.domain.usecases.create_game import GameCreateUsecase
from src.public.domain.usecases.game_start import GameStartUsecase
from src.public.domain.usecases.move import MoveUsecase


class GameUsecasesBuilder:
    def __init__(self, game_repository: GameRepository):
        self._game_repository = game_repository

    def construct_game_start_usecase(self) -> GameStartUsecase:
        return GameStartUsecase(self._game_repository)

    def construct_game_move_usecase(self) -> MoveUsecase:
        return MoveUsecase(self._game_repository)

    def construct_game_check_win_usecase(self) -> CheckWinUsecase:
        return CheckWinUsecase(self._game_repository)

    def construct_game_create_usecase(self) -> GameCreateUsecase:
        return GameCreateUsecase(self._game_repository)

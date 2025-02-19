from typing import Annotated

from fastapi import Depends
from src.public.domain.usecases.check_win import CheckWinUsecase
from src.public.domain.usecases.create_game import GameCreateUsecase
from src.public.domain.usecases.game_start import GameStartUsecase
from src.public.domain.usecases.game_usecases_builder import GameUsecasesBuilder
from src.public.domain.usecases.move import MoveUsecase


game_usecases_builder: GameUsecasesBuilder | None = None


def __get_game_usecses_builder() -> GameUsecasesBuilder:
    if game_usecases_builder is None:
        raise "Usecases must be inizialized"

    return game_usecases_builder


def __get_game_start_usecase():
    return __get_game_usecses_builder().construct_game_start_usecase()


GameStartUsecaseDependency = Annotated[
    GameStartUsecase,
    Depends(__get_game_start_usecase),
]


def __get_game_move_usecase() -> MoveUsecase:
    return __get_game_usecses_builder().construct_game_move_usecase()


GameMoveUsecaseDependency = Annotated[
    MoveUsecase,
    Depends(__get_game_move_usecase),
]


def __get_game_check_win_usecase() -> CheckWinUsecase:
    return __get_game_usecses_builder().construct_game_check_win_usecase()


GameCheckWinUsecaseDependency = Annotated[
    CheckWinUsecase,
    Depends(__get_game_check_win_usecase),
]


def __get_game_create_usecase() -> GameCreateUsecase:
    return __get_game_usecses_builder().construct_game_create_usecase()


GameCreateUsecaseDependency = Annotated[
    GameCreateUsecase,
    Depends(__get_game_create_usecase),
]

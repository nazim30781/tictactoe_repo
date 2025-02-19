from fastapi import APIRouter

from src import settings
from src.public.domain.usecases.game_usecases_builder import GameUsecasesBuilder
from src.public.infrastructure.api.fastapi_.v1.dependencies.usecases import game
from . import games, players


def get_router(game_usecases_builder: GameUsecasesBuilder):
    router = APIRouter(prefix=settings.settings.prefix.v1)

    router.include_router(
        games.router,
        prefix=settings.settings.prefix.game,
        tags=[settings.settings.prefix.game],
    )
    router.include_router(
        players.router,
        prefix=settings.settings.prefix.player,
        tags=[settings.settings.prefix.player],
    )

    game.game_usecases_builder = game_usecases_builder

    return router

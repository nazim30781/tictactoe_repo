from fastapi import FastAPI
from src.public.domain.usecases.game_usecases_builder import GameUsecasesBuilder
from src.public.infrastructure.api.base import ApiServerBase
from src.public.infrastructure.api.fastapi_.v1.routers import get_router


class FastApiServer(ApiServerBase):
    def __init__(
        self,
        game_usecases_builder: GameUsecasesBuilder,
        app_title: str,
    ):
        self._game_usecases_builder = game_usecases_builder
        self._title = app_title

    def _get_asgi_app(self) -> FastAPI:
        app = FastAPI(title=self._title)

        router = get_router(self._game_usecases_builder)

        app.include_router(router)

        return app

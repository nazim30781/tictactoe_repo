from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.public.domain.usecases.game_usecases_builder import GameUsecasesBuilder
from src.public.infrastructure.api.base import ApiServerBase
from src.public.infrastructure.api.fastapi_.v1.routers import get_router

from src.settings import settings


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

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.mount(
            "/static",
            StaticFiles(directory=settings.path.static),
            name="static",
        )

        router = get_router(self._game_usecases_builder)

        app.include_router(router)

        return app

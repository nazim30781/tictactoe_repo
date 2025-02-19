from abc import ABC, abstractmethod

import uvicorn

from src import settings


class ApiServerBase(ABC):
    def run(self):
        config = uvicorn.Config(
            app=self._get_asgi_app(),
            host=settings.settings.run.host,
            port=settings.settings.run.port,
        )

        uvicorn.Server(config).run()

    @abstractmethod
    def _get_asgi_app(self): ...

from src.public.domain.entities.player import Player
from src.public.domain.usecases.base import BaseUsecase


class PlayerCreateUsecase(BaseUsecase):
    async def execute(self, name) -> Player:
        player = Player(name)

        return player

from dataclasses import field
from src.public.domain.entities.game import Game
from src.public.domain.interfaces.repositories.game import GameRepository
from src.public.infrastructure.repositories.convertors.game import (
    dict_from_game,
    game_from_dict,
)
from src.public.infrastructure.repositories.mongo.base import MongoRepository


class MongoGameRepository(MongoRepository, GameRepository):
    async def get_game(self, game_oid: str):
        game_ = self._get_collection().find_one({"oid": game_oid})

        return game_from_dict(game_)

    async def save_game(self, game: Game):
        game_ = dict_from_game(game)

        self._get_collection().insert_one(game_)

    async def update_game_after_move(self, game: Game):
        game_ = dict_from_game(game)

        new_data = {
            "$set": {
                "board": game_["board"],
                "current_cell_value": game_["current_cell_value"],
            }
        }

        self._get_collection().update_one({"oid": game.oid}, new_data)

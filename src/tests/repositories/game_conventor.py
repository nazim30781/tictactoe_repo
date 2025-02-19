import asyncio
from src.public.domain.entities.board import Board
from src.public.domain.entities.game import Game
from src.public.domain.entities.player import Player
from src.public.domain.enums.dimension import SupportedDimensions
from src.public.domain.usecases.game_start import GameStartUsecase
from src.public.domain.usecases.move import MoveUsecase
from src.public.infrastructure.repositories.convertors.game import (
    dict_from_game,
    game_from_dict,
)
from src.public.infrastructure.repositories.mongo.game import MongoGameRepository


player_1 = Player("nazim")
player_2 = Player("zaur")
dimension = SupportedDimensions.TREE_ON_TREE

repo = MongoGameRepository("games")
print(repo.collection)
usecase = GameStartUsecase(repo)
movecase = MoveUsecase(repo)


async def main():
    game = await usecase.execute(player_1, player_2, dimension)

    await movecase.execute(game.oid, "X", 0, 1)
    await movecase.execute(game.oid, "O", 1, 2)
    await movecase.execute(game.oid, "X", 1, 1)
    await movecase.execute(game.oid, "O", 2, 1)
    await movecase.execute(game.oid, "X", 2, 1)

    game = await repo.get_game(game.oid)

    print(game.board.cells)


asyncio.run(main())

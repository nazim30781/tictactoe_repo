import asyncio

import pytest

from src.public.domain.entities.board import Board
from src.public.domain.entities.game import Game
from src.public.domain.entities.player import Player
from src.public.domain.enums.dimension import SupportedDimensions
from src.public.domain.usecases.game_start import GameStartUsecase
from src.public.domain.usecases.move import MoveUsecase
from src.public.infrastructure.repositories.mongo.game import MongoGameRepository

player_1 = Player("nazim")
player_2 = Player("zaur")
dimension = SupportedDimensions.TREE_ON_TREE

repo = MongoGameRepository("games")


@pytest.mark.asyncio
async def test_game_save():
    game = Game(player_1, player_2, Board.create(dimension))

    result = await repo.save_game(game)

    assert result == True


@pytest.mark.asyncio
async def test_game_save_and_get():
    game = Game(player_1, player_2, Board.create(dimension))

    result = await repo.save_game(game)

    game_ = await repo.get_game(game.oid)

    assert game.oid == game_.oid

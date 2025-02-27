from src.public.domain.entities.board import Board
from src.public.domain.entities.game import Game
from src.public.domain.entities.player import Player
from src.public.domain.enums.dimension import SupportedDimensions


def test_game_create():
    player_1 = Player("nazim")
    player_2 = Player("zaur")
    dimension = SupportedDimensions.TREE_ON_TREE

    game = Game(player_1, player_2, Board.create(dimension))

    assert game.player_1.oid == player_1.oid
    assert game.player_2.oid == player_2.oid


def test_game_start():
    player_1 = Player("nazim")
    player_2 = Player("zaur")
    dimension = SupportedDimensions.TREE_ON_TREE

    game = Game(player_1, player_2, Board.create(dimension))
    game.start()

    assert game.player_1.cell_value in ["X", "O"]


def test_game_move():
    player_1 = Player("nazim")
    player_2 = Player("zaur")
    dimension = SupportedDimensions.TREE_ON_TREE

    game = Game(player_1, player_2, Board.create(dimension))
    game.start("X")

    game.move()

    assert game.current_cell_value == "O"

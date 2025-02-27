from src.public.domain.entities.board import Board
from src.public.domain.enums.dimension import SupportedDimensions


def test_board_create():
    dimension = SupportedDimensions.TREE_ON_TREE

    board = Board.create(dimension)

    assert board is not None


def test_board_set_value():
    dimension = SupportedDimensions.SEVEN_ON_SEVEN

    board = Board.create(dimension)

    board.set_value(0, 0, "X")

    assert board.cells[0][0].cell_value == "X"


def test_board_check_win():
    dimension = SupportedDimensions.TREE_ON_TREE

    board = Board.create(dimension)

    board.set_value(0, 0, "X")
    board.set_value(0, 1, "X")
    board.set_value(0, 2, "X")

    assert board.check_winner != False

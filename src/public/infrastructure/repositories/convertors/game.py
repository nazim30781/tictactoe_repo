from src.public.domain.entities.board import Board
from src.public.domain.entities.cell import Cell
from src.public.domain.entities.game import Game
from src.public.domain.entities.player import Player
from src.public.domain.enums.cell_value import CellValue


def dict_from_game(game: Game) -> dict:
    for i in range(len(game.board.cells)):
        for j in range(len(game.board.cells)):
            game.board.cells[i][j] = game.board.cells[i][j].cell_value

    game_ = {
        "oid": game.oid,
        "player_1": {
            "oid": game.player_1.oid,
            "name": game.player_1.name,
            "cell_value": game.player_1.cell_value,
        },
        "player_2": {
            "oid": game.player_2.oid,
            "name": game.player_2.name,
            "cell_value": game.player_2.cell_value,
        },
        "board": game.board.cells,
        "current_cell_value": game.current_cell_value,
    }

    return game_


def game_from_dict(game: dict) -> Game:

    for i in range(len(game["board"])):
        for j in range(len(game["board"])):
            game["board"][i][j] = Cell(CellValue(game["board"][i][j]))

    game_ = Game(
        oid=game["oid"],
        player_1=Player(
            name=game["player_1"]["name"],
            cell_value=game["player_1"]["cell_value"],
            oid=game["player_1"]["oid"],
        ),
        player_2=Player(
            name=game["player_2"]["name"],
            cell_value=game["player_2"]["cell_value"],
            oid=game["player_2"]["oid"],
        ),
        board=Board(game["board"]),
        current_cell_value=game["current_cell_value"],
    )

    return game_

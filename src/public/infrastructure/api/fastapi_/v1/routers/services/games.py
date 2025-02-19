from fastapi import WebSocket

from src.public.domain.entities.game import Game
from src.public.domain.entities.game_result import GameResult
from src.public.domain.entities.player import Player
from src.public.domain.enums.dimension import SupportedDimensions
from src.public.domain.usecases.game_start import GameStartUsecase
from src.public.infrastructure.api.fastapi_.v1.dependencies.usecases.game import (
    GameCheckWinUsecaseDependency,
    GameMoveUsecaseDependency,
)
from src.public.infrastructure.api.fastapi_.v1.routers.rooms.room import (
    Room,
    RoomsManager,
)


async def start_game(
    room: Room,
    rooms_manager: RoomsManager,
    websocket: WebSocket,
    player_oid: str,
    player_name: str,
    start_usecase: GameStartUsecase,
):
    if room and not room.start:
        start = rooms_manager.start(
            room,
            websocket,
            player_oid,
            player_name,
        )

        if start:
            game = await create_game(room, start_usecase)

            await send_game_info_to_players(room, game)


async def create_game(room: Room, start_usecase: GameStartUsecase):
    game = await start_usecase.execute(
        room.game_oid,
        Player(
            oid=room.player_1.player_oid,
            name=room.player_1.name,
        ),
        Player(
            oid=room.player_2.player_oid,
            name=room.player_2.name,
        ),
        SupportedDimensions.TREE_ON_TREE,
    )

    room.start = True

    return game


async def send_game_info_to_players(room: Room, game: Game):
    await room.player_1.websocket.send_json(
        {
            "start": True,
            "cell_value": game.player_1.cell_value,
        }
    )

    await room.player_2.websocket.send_json(
        {
            "start": True,
            "cell_value": game.player_2.cell_value,
        }
    )


async def move(
    room: Room,
    data: dict,
    cookie: dict,
    move_usecase: GameMoveUsecaseDependency,
    check_win_usecase: GameCheckWinUsecaseDependency,
):
    game = await move_usecase.execute(
        room.game_oid,
        cookie["cell_value"],
        int(data["row"]),
        int(data["column"]),
    )

    await send_move_info_to_players(room, data, cookie)

    result = await check_win_usecase.execute(game.oid)

    if result:
        await send_game_result_to_players(room, result)


async def send_move_info_to_players(
    room: Room,
    data: dict,
    cookie: dict,
):
    await room.player_1.websocket.send_json(
        {
            "move": True,
            "row": data["row"],
            "column": data["column"],
            "cell_value": cookie["cell_value"],
        }
    )

    await room.player_2.websocket.send_json(
        {
            "move": True,
            "row": data["row"],
            "column": data["column"],
            "cell_value": cookie["cell_value"],
        }
    )


async def send_game_result_to_players(room: Room, result: GameResult):
    await room.player_1.websocket.send_json(
        {"finish": True, "win_value": str(result.winner_value)}
    )

    await room.player_2.websocket.send_json(
        {"finish": 1, "win_value": str(result.winner_value)}
    )

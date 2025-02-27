from fastapi import APIRouter, Request, Response, WebSocket
from fastapi.templating import Jinja2Templates

from src.public.domain.enums.dimension import SupportedDimensions
from src.public.infrastructure.api.fastapi_.v1.dependencies.usecases.game import (
    GameCreateUsecaseDependency,
    GameMoveUsecaseDependency,
    GameStartUsecaseDependency,
    GameCheckWinUsecaseDependency,
)
from src.public.infrastructure.api.fastapi_.v1.routers.rooms.room import (
    Room,
    RoomsManager,
)
from src.public.infrastructure.api.fastapi_.v1.routers.services.games import (
    move,
    start_game,
)
from src.public.infrastructure.api.fastapi_.v1.routers.utils.get_cookie import (
    get_cookie,
)
from src.settings import settings


router = APIRouter()

temlpates = Jinja2Templates(directory=settings.path.templates)
rooms_manager = RoomsManager()


@router.get("/")
async def get_html(request: Request):
    return temlpates.TemplateResponse(
        request=request,
        name="index.html",
    )


@router.websocket("/3/room")
async def game(
    websocket: WebSocket,
    start_usecase: GameStartUsecaseDependency,
    move_uscase: GameMoveUsecaseDependency,
    check_win_usecase: GameCheckWinUsecaseDependency,
):
    await websocket.accept()

    while True and websocket:
        data = await websocket.receive_json()

        cookie = get_cookie(data["cookie"])
        room_oid = cookie["room_oid"]
        player_oid = cookie["player_oid"]
        player_name = cookie["player_name"]

        room = rooms_manager.get_room_by_id(room_oid)

        if int(cookie["start"]) == 0 and cookie.get("cell_value") == None:
            await start_game(
                room,
                rooms_manager,
                websocket,
                player_oid,
                player_name,
                start_usecase,
            )

        else:
            await move(
                room,
                data,
                cookie,
                move_uscase,
                check_win_usecase,
                rooms_manager,
            )


@router.get("/game_preparing")
async def game_preparing(
    request: Request,
    response: Response,
    game_create_usecase: GameCreateUsecaseDependency,
):
    player_oid = request.cookies["player_oid"]
    player_name = request.cookies["player_name"]

    room = rooms_manager.connect_player(player_oid, player_name)

    game_oid = await game_create_usecase.execute()
    room.game_oid = game_oid

    response.delete_cookie("cell_value", "/v1/game")
    response.delete_cookie("win_value", "/v1/game")
    response.delete_cookie("start", "/v1/game")

    response.set_cookie(key="room_oid", value=room.oid)

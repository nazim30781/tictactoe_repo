from fastapi import APIRouter, Response

from src.public.domain.usecases.player_create import PlayerCreateUsecase


router = APIRouter()


@router.post("/create_player")
async def create_player(
    player_name: str,
    response: Response,
):
    player = await PlayerCreateUsecase().execute(player_name)
    response.set_cookie("player_oid", player.oid)
    response.set_cookie("player_name", player_name)

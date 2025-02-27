from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from src.public.domain.usecases.player_create import PlayerCreateUsecase
from src.public.infrastructure.api.fastapi_.v1.routers.schemas.player import PlayerModel
from src.settings import settings


router = APIRouter()

temlpates = Jinja2Templates(directory=settings.path.templates)


@router.get("/player_create_page")
async def create_player_page(request: Request):
    return temlpates.TemplateResponse(
        request=request,
        name="player_create.html",
    )


@router.post("/create_player")
async def create_player(
    username: PlayerModel,
    response: Response,
):
    player = await PlayerCreateUsecase().execute(username.username)

    response.set_cookie("player_oid", player.oid)
    response.set_cookie("player_name", username.username)

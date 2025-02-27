from pydantic import BaseModel


class PlayerModel(BaseModel):
    username: str

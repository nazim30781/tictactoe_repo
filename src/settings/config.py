from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoConfig(BaseModel):
    host: str = "localhost"
    port: int = 27017
    db_name: str = "tictactoe"


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class PrefixConfig(BaseModel):
    v1: str = "/v1"
    game: str = "/game"
    player: str = "/player"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        extra="ignore",
    )
    run: RunConfig = RunConfig()
    mongo: MongoConfig = MongoConfig()
    prefix: PrefixConfig = PrefixConfig()


settings = Settings()

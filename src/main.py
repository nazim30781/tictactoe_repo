import asyncio
from src.public.domain.usecases.game_usecases_builder import GameUsecasesBuilder
from src.public.infrastructure.api.fastapi_.fastapi_ import FastApiServer
from src.public.infrastructure.repositories.mongo.game import MongoGameRepository


def main():
    print("start")
    game_repo = MongoGameRepository("games")
    game_usecases_builder = GameUsecasesBuilder(game_repo)

    app = FastApiServer(game_usecases_builder, "tictactoe")

    app.run()


main()

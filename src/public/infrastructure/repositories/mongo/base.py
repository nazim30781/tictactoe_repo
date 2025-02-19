from abc import ABC
from dataclasses import dataclass, field

from pymongo import MongoClient

from src.settings import settings


@dataclass
class MongoRepository(ABC):
    collection: str = field(default=None)

    def __get_connection(self):
        client = MongoClient()

        db = client[settings.mongo.db_name]

        return db

    def _get_collection(self):
        return self.__get_connection()[self.collection]

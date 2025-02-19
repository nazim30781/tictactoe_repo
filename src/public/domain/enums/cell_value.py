from enum import Enum
import random


class CellValue(str, Enum):
    E: str = "*"
    X: str = "X"
    O: str = "O"

    def __str__(self) -> str:
        return self

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def get_random_values(cls) -> list[str]:
        items = [cls.O, cls.X]
        random.shuffle(items)

        return items

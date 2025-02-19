from dataclasses import dataclass


@dataclass(eq=False)
class EntityException(Exception):
    @property
    def message(self) -> str:
        return "Entity Error"

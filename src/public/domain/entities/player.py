from dataclasses import dataclass, field

from src.public.domain.entities.base import BaseEntity


@dataclass
class Player(BaseEntity):
    name: str
    cell_value: str | None = field(default=None)

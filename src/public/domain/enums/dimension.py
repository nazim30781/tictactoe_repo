from dataclasses import dataclass
from enum import Enum

from src.public.domain.entities.dimension import Dimension


class SupportedDimensions:
    TREE_ON_TREE = Dimension(3, 3)
    FIVE_ON_FIVE = Dimension(5, 5)
    SEVEN_ON_SEVEN = Dimension(7, 7)
    NINE_ON_NINE = Dimension(9, 9)

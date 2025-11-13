from enum import Enum

class DirectionEnum(Enum):
    RIGHT = 0,
    LEFT = 1,
    UP = 2,
    DOWN = 3,
    DIAGONAL_RIGHT_UP = 4,
    DIAGONAL_LEFT_UP = 5,
    DIAGONAL_RIGHT_DOWN = 6,
    DIAGONAL_LEFT_DOWN = 7
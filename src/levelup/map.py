from levelup.position import Position

from enum import Enum


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    startingPosition = Position(0,0)
    num_positions = 100

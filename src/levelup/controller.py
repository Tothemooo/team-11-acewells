from enum import Enum
from dataclasses import dataclass
from levelup.character import Character
from levelup import map

DEFAULT_CHARACTER_NAME = "Character"
ARBITRARY_INVALID_INITIALIZED_POSITION = (-1,-1)


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


@dataclass
class GameStatus:
    running: bool = False
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    current_position: tuple = ARBITRARY_INVALID_INITIALIZED_POSITION
    moveCount: int = 0

    def getStatus(self):
        return (self.character, self.current_position)


class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def create_character(self, character_name: str) -> None:
        if not character_name:
            character_name = DEFAULT_CHARACTER_NAME
        self.status.character = Character(character_name)
    
    def startGame():
            gamemap = gamemap.GameMap()
            if character == null:
                create_character("")
            character.EnterMap(gameMap)
            self.status.character = character.name
            self.status.current_position = character.position

    def move(self, direction: Direction) -> None:
        character.move(direction)
        status.getStatus()
        print(f"Moved {direction.name}")


    def set_character_position(self, xycoordinates: tuple) -> None:
        print(f"Set character position state for tesing")
        #TODO: IMPLEMENTS THIS
    #    self.status.current_position= xycoordinates

    
    def setTotalPositions(moveCount):
        character.moveCount = moveCount
        self.status.moveCount = character.moveCount


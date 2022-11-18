from levelup.position import Position
from levelup.map import GameMap
#from levelup.controller import Direction

DEFAULT_POSITION = Position(0, 0)


class Character:
    name: str
    current_position: Position = DEFAULT_POSITION

    def __init__(self, name: str):
        self.name = name
   
    def getName():
        name = input("Enter Character Name")
        return ("Nice to meet you brave warrior",(name),"!!")

    def enter_map(self, game_map: GameMap):
        m = int(input())
        return m

    def getPosition(): DEFAULT_POSITION
        
    #def setMap(m):
        #pass

    def move(self):
        pass
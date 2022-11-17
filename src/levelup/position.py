from enum import Enum
from dataclasses import dataclass
# from levelup import GameMap


#for x and y coordinates , values need to be pulled from GameMap, pull the coordinates from there

default_x_position = 1
default_y_position = 1

class Position():
    def __init__(self,default_x_position,default_y_position):
        self.xCoordinates=default_x_position
        self.yCoordinates=default_y_position
        self.position=(self.xCoordinates,self.yCoordinates)

 
    
    

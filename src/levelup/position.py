from enum import Enum
from dataclasses import dataclass

default_x_position = 1
default_y_position = 1

class Position():
    def __init__(self):
        self.xCoordinates=default_x_position
        self.yCoordinates=default_y_position
        self.position=(self.xCoordinates,self.yCoordinates)


    
    

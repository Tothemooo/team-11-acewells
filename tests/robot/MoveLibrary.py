from levelup.controller import GameController
from levelup.controller import Direction

start_x: int
start_y: int

class MoveLibrary:
    def initialize_character_name_with(self, character):
        self.character=character

    def initialize_character_s_Position_x_with(self, S_Position_X):
        self.S_Position_X=S_Position_X
    
    def initialize_character_s_Position_Y_with(self, S_Position_Y):
        self.S_Position_Y=S_Position_Y

    def initialize_S_Move_Count_with(self, S_Move_Count):
        self.S_Move_Count=S_Move_Count

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.set_character_position((self, character, S_Position_X, S_Position_Y, S_Move_Count))
        self.controller.move(Direction[direction])
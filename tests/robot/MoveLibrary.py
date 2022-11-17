from levelup.controller import GameController
from levelup.controller import Direction

start_x: int
start_y: int

class MoveLibrary:
    def initialize_character_name_with(self, character):
        self.character=character

    def initialize_character_s_Position_x_with(self, S_Position_X):
        self.start_x=x_position
    
    def initialize_character_s_Position_Y_with(self, S_Position_Y):
        self.start_y=y_position

    def initialize_S_Move_Count_with(self, S_Move_Count):
        self.S_Move_Count=S_Move_Count

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.set_character_position((self, character, S_Position_X, S_Position_Y, S_Move_Count))
        self.controller.move(Direction[direction])

    def character_xposition_should_be(self, expected):
        e_position_x = self.controller.status.current_position[0]
        if e_position_x != expected:
            raise AssertionError(
                "%s != %s" % (e_position_x, expected)
            )

    def character_yposition_should_be(self, expected):
        e_position_y = self.controller.status.current_position[0]
        if e_position_y != expected:
            raise AssertionError(
                "%s != %s" % (e_position_y, expected)
            )
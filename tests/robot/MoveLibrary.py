from levelup.controller import GameController
from levelup.controller import Direction

start_x: int
start_y: int
S_Move_Count: int


class MoveLibrary:
    def initialize_character_xposition_with(self, x_position):
        self.start_x= x_position
    
    def initialize_character_yposition_with(self, y_position):
        self.start_y= y_position

    def initialize_S_Move_Count_with(self, S_Move_Count):
        self.S_Move_Count=S_Move_Count

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.set_character_position((self, self.start_x, self.start_y))
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
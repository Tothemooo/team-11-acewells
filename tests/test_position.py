from dataclasses import dataclass
from unittest import TestCase
from levelup import position


class TestPosition(TestCase):
    def test_init(self):
        self.test_position = position.Position()
        self.assertEqual((1,1), self.test_position.position)

    


    
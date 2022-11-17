from levelup.map import Map
from unittest import TestCase
from levelup.position import Position



class TestMap(TestCase):
    def test_initialization(self):
        testobj = Map()
        expected_starting_position = Position(0,0)
        self.assertEqual(testobj.startingPosition.to_str(), expected_starting_position.to_str())

        expected_number_positions = 100
        self.assertEqual(testobj.num_positions, expected_number_positions)
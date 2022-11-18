from unittest import TestCase
from levelup.character import Character, DEFAULT_POSITION
from levelup.controller import Direction


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        self.assertEqual(testobj.current_position, DEFAULT_POSITION)
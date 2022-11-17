from unittest import TestCase
from levelup.controller import GameController, DEFAULT_CHARACTER_NAME
from levelup.character import Character


class TestCharacter(TestCase):
    expected_value: str
    actual_value: str

    def test_initialization(self):
        testobj = Character("")
        expected_value = ""
        actual_value = testobj.name
        self.assertNotEqual(actual_value, expected_value)

from unittest import TestCase
from levelup.controller import GameController, DEFAULT_CHARACTER_NAME

class TestGameController(TestCase):
    def test_init(self):
        test_controller = GameController()
        self.assertEqual(DEFAULT_CHARACTER_NAME, test_controller.status.character.name)

    def test_create_default_character(self):
        test_controller = GameController()
        test_controller.create_character("")
        self.assertEqual(DEFAULT_CHARACTER_NAME, test_controller.status.character.name)

    def test_create_character(self):
        test_controller = GameController()
        expected_character_name = "ArbitraryName"
        test_controller.create_character(expected_character_name)
        self.assertEqual(expected_character_name, test_controller.status.character.name)

    def test_get_gamestatus(self):
        test_controller = GameController()
        self.assertIsNotNone(test_controller.status.getStatus());

  #  def test_set_character_position(self):
   #     test_controller = GameController()
   #     expected_character_position = (3,4)
   #     test_controller.set_character_position(expected_character_position)
  #      self.assertEqual(expected_character_position,test_controller.status.current_position)


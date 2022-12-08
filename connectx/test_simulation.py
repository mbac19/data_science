import unittest

from .simulation import Configuration, Game


class TestGame(unittest.TestCase):
    def test_is_board_full(self):
        config = Configuration(columns=1, rows=1, inarow=2)
        game = Game(config)

        self.assertFalse(game.is_board_full())

        game.drop(player=1, column=0)

        self.assertTrue(game.is_board_full())


if __name__ == 'main':
    unittest.main()
import numpy as np
import unittest

from utils import print_board, possible_moves
from simulation import Configuration
from .search_agent import SearchAgent

class TestSearchAgent(unittest.TestCase):
    def test_agent_depth_1_makes_valid_move_on_empty_board(self):
        config = Configuration(columns=10, rows=10, inarow=4, first_move_agent=1)
        board = config.make_empty_board()

        agent = SearchAgent(search_depth=1)
        agent.start_run(player=1)
        column = agent.choose_action(board, configuration=config)

        self.assertTrue(column >= 0 and column < 10)


    def test_agent_depth_3_makes_valid_move_on_empty_board(self):
        config = Configuration(columns=15, rows=15, inarow=4, first_move_agent=1)
        board = config.make_empty_board()

        agent = SearchAgent(search_depth=3)
        agent.start_run(player=1)
        column = agent.choose_action(board, configuration=config)

        self.assertTrue(column >= 0 and column < 15)        


    def test_agent_depth_1_makes_valid_move_on_board_with_only_one_open_column(self):
        config = Configuration(columns=8, rows=8, inarow=8, first_move_agent=1)
        board = config.make_empty_board()

        for i in range(7):
            board[:, i] = [1, 2, 1, 2, 1, 2, 1, 2]

        agent = SearchAgent(search_depth=1)
        agent.start_run(player=1)
        column = agent.choose_action(board, configuration=config)

        self.assertEqual(column, 7)


    def test_agent_depth_1_finds_winning_move(self):
        config = Configuration(columns=8, rows=8, inarow=4, first_move_agent=1)
        board = config.make_empty_board()
        board[:, 2] = [1, 1, 1, 0, 0, 0, 0, 0]

        agent = SearchAgent(search_depth=1)
        agent.start_run(player=1)
        column = agent.choose_action(board, configuration=config)

        self.assertEqual(column, 2)


    def test_agent_does_not_modify_original_board(self):
        config = Configuration(columns=8, rows=8, inarow=4, first_move_agent=1)
        board = config.make_empty_board()

        agent = SearchAgent(search_depth=4)
        agent.start_run(player=1)
        agent.choose_action(board, configuration=config)

        self.assertTrue(np.array_equal(board, config.make_empty_board()))

    
if __name__ == '__main__':
    unittest.main()

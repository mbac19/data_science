import numpy as np
import unittest

from utils import check_win, drop_piece

class TestUtils(unittest.TestCase):
    def test_drop_piece_in_empty_board(self):
        board = np.zeros((10, 10), dtype=np.int8)
        drop_piece(board, column=2, player=1)

        expected = np.zeros_like(board)
        expected[0, 2] = 1

        self.assertTrue(np.array_equal(board, expected))


    def test_drop_multiple_pieces_different_columns(self):
        board = np.zeros((20, 20), dtype=np.int8)
        drop_piece(board, column=4, player=1)
        drop_piece(board, column=8, player=2)

        expected = np.zeros_like(board)
        expected[0, 4] = 1
        expected[0, 8] = 2

        self.assertTrue(np.array_equal(board, expected))

    
    def test_drop_multiple_pieces_same_column(self):
        board = np.zeros((5, 5), dtype=np.int8)
        drop_piece(board, column=2, player=2)
        drop_piece(board, column=2, player=1)

        expected = np.zeros_like(board)
        expected[0, 2] = 2
        expected[1, 2] = 1

        self.assertTrue(np.array_equal(board, expected))


    def test_winning_pattern_row(self):
        board = np.zeros((5, 5), dtype=np.int8)
        drop_piece(board, column=2, player=1)
        drop_piece(board, column=3, player=1)
        drop_piece(board, column=4, player=1)

        self.assertTrue(check_win(board, ))



if __name__ == '__main__':
    unittest.main()

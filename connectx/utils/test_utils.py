import numpy as np
import unittest

from utils import check_win, drop_piece, possible_moves

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

        last_drop_row = 0
        last_drop_column = 4
        self.assertTrue(check_win(board, row=last_drop_row, col=last_drop_column, player=1, inarow=3))

    
    def test_winning_pattern_col(self):
        board = np.zeros((5, 5), dtype=np.int8)
        drop_piece(board, column=1, player=2)
        drop_piece(board, column=1, player=2)
        drop_piece(board, column=1, player=2)
        drop_piece(board, column=1, player=2)

        last_drop_row = 3
        last_drop_column = 1
        self.assertTrue(check_win(board, row=last_drop_row, col=last_drop_column, player=2, inarow=4))

    
    def test_winning_pattern_diag1(self):
        board = np.zeros((5, 5), dtype=np.int8)
        drop_piece(board, column=1, player=1)
        drop_piece(board, column=2, player=2)
        drop_piece(board, column=2, player=1)

        last_drop_row = 1
        last_drop_column = 2
        self.assertTrue(check_win(board, row=last_drop_row, col=last_drop_column, player=1, inarow=2))

    
    def test_winning_pattern_diag2(self):
        board = np.zeros((5, 5), dtype=np.int8)
        drop_piece(board, column=3, player=2)
        drop_piece(board, column=2, player=1)
        drop_piece(board, column=2, player=2)

        last_drop_row = 1
        last_drop_column = 2
        self.assertTrue(check_win(board, row=last_drop_row, col=last_drop_column, player=2, inarow=2))


    def test_diag_pattern_one_short_of_winning(self):
        board = np.zeros((5, 5), dtype=np.int8)
        drop_piece(board, column=3, player=2)
        drop_piece(board, column=2, player=1)
        drop_piece(board, column=2, player=2)

        last_drop_row = 1
        last_drop_column = 2
        self.assertFalse(check_win(board, row=last_drop_row, col=last_drop_column, player=2, inarow=3))

    
    def test_returns_all_columns_as_possible_moves_on_empty_board(self):
        board = np.zeros((5, 5), dtype=np.int8)
        cols = possible_moves(board)
        self.assertEqual(cols, [x for x in range(5)])

    
    def test_does_not_return_full_column_as_possible_moves(self):
        board = np.zeros((10, 10), dtype=np.int8)
        board[:, 0] = [1 for _ in range(10)]
        cols = possible_moves(board)
        self.assertEqual(cols, [x for x in range(1, 10)])


if __name__ == '__main__':
    unittest.main()

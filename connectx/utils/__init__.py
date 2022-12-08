import numpy as np


class InvalidActionException(Exception):
    pass


def is_board_full(board):
    slots = np.prod(board.shape)
    return np.sum(board != 0) == slots


def is_board_col_full(board, column):
    count = board.shape[1]
    return np.sum(board[:, column] != 0) == count


def drop_piece(board, column, player):
        """
        Drop a piece in a slot. Returns the row that the piece ended up in.
    i   Raises exception if the slot is full.
        """
        total_rows, total_cols = np.shape(board)

        count = np.sum(board[:, column] != 0)

        if count >= total_rows:
            raise InvalidActionException("Cannot drop piece in full column")

        board[count, column] = player

        # Now we need to check for a winner. Should check 
        # TODO: Figure out if player has won.
        # Need to check 4 directions.

        col = board[:count, column] == player

        return count

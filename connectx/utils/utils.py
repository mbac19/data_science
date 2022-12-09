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


def check_win(board, row, col, player, inarow):
    """
    Check if the indicated player has won. To narrow the search, we indicate
    a row / column to check for the win condition.
    """

    row_seq = board[row, :] == player
    
    if _is_win(row_seq, inarow):
        return True

    col_seq = board[:, col] == player

    if _is_win(col_seq, inarow):
        return True

    row_count, col_count = np.shape(board)

    # Diag 1
    dist_to_bottom_left = min(row, col)
    dist_to_top_right = min(row_count - row - 1, col_count - col - 1)
    diag1_len = dist_to_bottom_left + dist_to_top_right
    diag1_row0 = row - dist_to_bottom_left
    diag1_col0 = col - dist_to_bottom_left
    diag1_seq = board[range(diag1_row0, diag1_row0 + diag1_len), range(diag1_col0, diag1_col0 + diag1_len)]

    if _is_win(diag1_seq, inarow):
        return True

    # Diag 2
    dist_to_bottom_right = min(row, col_count - col - 1)
    dist_to_top_left = min(row_count - row - 1, col)
    diag2_len = dist_to_bottom_right + dist_to_top_left
    diag2_row0 = row - dist_to_bottom_right
    diag2_col0 = col + dist_to_bottom_right
    diag2_seq = board[range(diag2_row0, diag2_row0 + diag2_len), range(diag2_col0, diag2_col0 - diag2_len, -1)]

    if _is_win(diag2_seq, inarow):
        return True

    return False


def _is_win(seq, inarow):
    if len(seq) < inarow:
        return False

    count = 0

    for el in seq:
        if el == 1:
            count += 1
            if count >= inarow:
                return True
        else:
            count = 0

    return False

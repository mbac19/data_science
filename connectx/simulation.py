import math
import numpy as np

from utils import drop_piece, is_board_full

class Configuration:
    def __init__(self, columns, rows, inarow):
        self.columns = columns
        self.rows = rows
        self.inarow = inarow


class Simulation:
    def __init__(self, configuration, agent1, agent2):
        self._configuration = configuration
        self._agent1 = agent1
        self._agent2 = agent2


    def run(self):
        board = np.zeros((self._configuration.rows, self._configuration.columns), dtype=np.int8)
        actions = []

        while not is_board_full(board):
            column = self._agent1.choose_action(board, self._configuration)
            dropped_row = drop_piece(board=board, player=1, column=column)

            if _check_win(board, dropped_row, column, player=1, inarow=self._configuration.inarow):
                return board, 1, actions

            actions.append(column)

            column = self._agent2.choose_action(board, self._configuration)
            dropped_row = drop_piece(board=board, player=2, column=column)

            if _check_win(board, dropped_row, column, player=2, inarow=self._configuration.inarow):
                return board, 2, actions

            actions.append(column)
        
        return board, 0, actions



def _check_win(board, row, col, player, inarow):
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

    # TODO: Diagonals 
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

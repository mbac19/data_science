import math
import numpy as np

class Configuration:
    def __init__(self, columns, rows, inarow):
        self.columns = columns
        self.rows = rows
        self.inarow = inarow


class InvalidActionException(Exception):
    pass


class Simulation:
    def __init__(self, configuration, agent1, agent2):
        self._configuration = configuration
        self._agent1 = agent1
        self._agent2 = agent2


    def run(self):
        board = np.zeros((self.configuration.rows, self.configuration.columns))
        actions = []

        while not _is_board_full(board):
            column = self._agent1.choose_action(board)
            actions.append(column)

            if self._drop(board=board, player=1, column=column):
                return board, 1, actions

            column = self._agent2.choose_action(board)
            actions.append(column)
            if self._drop(board=board, player=2, column=column):
                return board, 2, actions
        
        return board, 0, actions


    def _drop(self, board, player, column):
        """
        Drop a piece in a slot. Returns True if the player has won, False
    i    otherwise. Raises exception if the slot is full.
        """
        count = np.sum(board[:, column] != 0)

        if count == self.configuration.columns:
            raise InvalidActionException("Cannot drop piece in full column")

        board[count, column] = player

        # Now we need to check for a winner. Should check 
        # TODO: Figure out if player has won.
        # Need to check 4 directions.

        col = board[:count, column] == player

        if _is_win(col):
            return True

        row0 = max(0, count - self.configuration.inarow + 1)
        row1 = min(self.configuration.row, count + self.configuration.inarow)
        row = board[count, row0:row1] == player

        if _is_win(row):
            return True

        # TODO: Handle diagonals
        return False


def _is_board_full(board):
        slots = np.prod(board.shape)
        return np.sum(board != 0) == slots


def _is_win(seq, inarow):
    if len(seq) < inarow:
        return False

    count = 0

    for el in seq:
        if el == 1.0:
            count += 1
            if count >= inarow:
                return True
        
        count = 0

    return False

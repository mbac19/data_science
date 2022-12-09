import math
import numpy as np

from utils import check_win, drop_piece, is_board_full

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

            if check_win(board, dropped_row, column, player=1, inarow=self._configuration.inarow):
                return board, 1, actions

            actions.append(column)

            column = self._agent2.choose_action(board, self._configuration)
            dropped_row = drop_piece(board=board, player=2, column=column)

            if check_win(board, dropped_row, column, player=2, inarow=self._configuration.inarow):
                return board, 2, actions

            actions.append(column)
        
        return board, 0, actions

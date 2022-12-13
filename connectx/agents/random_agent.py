import random

from utils import is_board_col_full

class RandomAgent:
    def __init__(self):
        self.name = 'Random Agent'


    def start_run(self, player):
        pass


    def choose_action(self, board, configuration):
        while True:
            col = random.randint(0, configuration.columns - 1)

            if not is_board_col_full(board, col):
                return col


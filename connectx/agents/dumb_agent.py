from utils import is_board_col_full

class DumbAgent:
    def __init__(self):
        self.name = 'Dumb Agent'


    def start_run(self, player):
        pass


    def choose_action(self, board, configuration):
        for i in range(configuration.columns):
            if not is_board_col_full(board, i):
                return i

        raise Exception("No valid moves available")

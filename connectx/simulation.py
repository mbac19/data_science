import numpy as np

from utils import check_win, drop_piece, is_board_full

class Configuration:
    def __init__(self, columns, rows, inarow, first_move_agent):
        self.columns = columns
        self.rows = rows
        self.inarow = inarow
        self.first_move_agent = first_move_agent


class Simulation:
    def __init__(self, config, agent1, agent2):
        self.config = config

        if config.first_move_agent == 1:
            self.first_move_agent = agent1
            self.first_move_agent_label = 1
            self.second_move_agent = agent2
            self.second_move_agent_label = 2
        else:
            self.first_move_agent = agent2
            self.first_move_agent_label = 2
            self.second_move_agent = agent1
            self.second_move_agent_label = 1


    def run(self):
        config = self.conf

        first_move_agent = self.first_move_agent
        first_move_agent_label = self.first_move_agent_label

        second_move_agent = self.second_move_agent
        second_move_agent_label = self.second_move_agent_label

        board = np.zeros((config.rows, config.columns), dtype=np.int8)
        actions = []

        while True:
            column = first_move_agent.choose_action(board, config)
            dropped_row = drop_piece(board=board, player=first_move_agent_label, column=column)
            actions.append(column)

            if check_win(board, row=dropped_row, col=column, player=first_move_agent_label, inarow=config.inarow):
                return board, first_move_agent_label, actions

            if is_board_full(board):
                return board, 0, actions
            
            column = second_move_agent.choose_action(board, config)
            dropped_row = drop_piece(board=board, player=second_move_agent_label, column=column)
            actions.append(column)

            if check_win(board, dropped_row, column, player=second_move_agent_label, inarow=config.inarow):
                return board, second_move_agent_label, actions

            if is_board_full(board):
                return board, 0, actions

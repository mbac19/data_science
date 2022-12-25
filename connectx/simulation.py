import numpy as np
import time

from utils import check_win, drop_piece, is_board_full

class Configuration:
    def __init__(self, columns, rows, inarow, first_move_agent):
        self.columns = columns
        self.rows = rows
        self.inarow = inarow
        self.first_move_agent = first_move_agent

    
    def make_empty_board(self):
        return np.zeros((self.rows, self.columns), dtype=np.int8)


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
        config = self.config

        first_move_agent = self.first_move_agent
        first_move_agent_label = self.first_move_agent_label

        second_move_agent = self.second_move_agent
        second_move_agent_label = self.second_move_agent_label

        board = config.make_empty_board()
        actions = []

        first_move_agent.start_run(player=first_move_agent_label)
        second_move_agent.start_run(player=second_move_agent_label)

        stats = {'avg_move_time': [0.0, 0.0], 'move_count': 1}

        while True:
            n = stats['move_count']

            start = time.time()
            column = first_move_agent.choose_action(board, config)
            end = time.time()

            dropped_row = drop_piece(board=board, player=first_move_agent_label, column=column)
            actions.append(column)

            delta_time = end - start
            stats['avg_move_time'][first_move_agent_label - 1] = stats['avg_move_time'][first_move_agent_label - 1] + 1.0 / n * (delta_time - stats['avg_move_time'][first_move_agent_label - 1])

            if check_win(board, row=dropped_row, col=column, player=first_move_agent_label, inarow=config.inarow):
                return board, first_move_agent_label, actions, stats

            if is_board_full(board):
                return board, 0, actions, stats
            
            start = time.time() 
            column = second_move_agent.choose_action(board, config)
            end = time.time()

            dropped_row = drop_piece(board=board, player=second_move_agent_label, column=column)
            actions.append(column)

            delta_time = end - start
            stats['avg_move_time'][second_move_agent_label - 1] = stats['avg_move_time'][second_move_agent_label - 1] + 1.0 / n * (delta_time - stats['avg_move_time'][second_move_agent_label - 1])

            if check_win(board, dropped_row, column, player=second_move_agent_label, inarow=config.inarow):
                return board, second_move_agent_label, actions, stats

            if is_board_full(board):
                return board, 0, actions, stats

            stats['move_count'] += 1

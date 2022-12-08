import numpy as np

from agents.random_agent import RandomAgent
from simulation import Configuration, Simulation
from utils import drop_piece

VAL_TO_CHAR = {
    1: 'X',
    2: 'O',
    0: '•',
}

def main():
    config = Configuration(columns=10, rows=10, inarow=4)
    sim = Simulation(config, agent1=RandomAgent(), agent2=RandomAgent())
    board, winner, actions = sim.run()
    _print_board(board)


def _print_board(board):
    rows, cols = np.shape(board)

    print('')

    for row in range(rows - 1, -1, -1):
        for col in range(cols):
            ch = VAL_TO_CHAR[board[row, col]]
            print(f"{ch} ", end='')
        print()


if __name__ == '__main__':
    main()
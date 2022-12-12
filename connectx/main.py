import numpy as np

from judge import Judge
from agents.random_agent import RandomAgent
from simulation import Configuration, Simulation
from utils import check_win, drop_piece

VAL_TO_CHAR = {
    1: 'X',
    2: 'O',
    0: '•',
}

def main():
    configs = [
        Configuration(columns=10,  rows=10,  inarow=4,  first_move_agent=1),
        Configuration(columns=10,  rows=10,  inarow=4,  first_move_agent=2),
        # Configuration(columns=20,  rows=20,  inarow=5,  first_move_agent=1),
        # Configuration(columns=20,  rows=20,  inarow=5,  first_move_agent=2),
        # Configuration(columns=40,  rows=40,  inarow=6,  first_move_agent=1),
        # Configuration(columns=40,  rows=40,  inarow=6,  first_move_agent=2),
        # Configuration(columns=80,  rows=80,  inarow=10, first_move_agent=1),
        # Configuration(columns=80,  rows=80,  inarow=10, first_move_agent=2),
        # Configuration(columns=120, rows=120, inarow=20, first_move_agent=1),
        # Configuration(columns=120, rows=120, inarow=20, first_move_agent=2),
    ]

    judge = Judge(configs=configs, agent1=RandomAgent(), agent2=RandomAgent())
    print(judge.run(runs_per_config=100))


if __name__ == '__main__':
    main()
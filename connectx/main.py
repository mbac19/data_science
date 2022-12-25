import pandas as pd

from agents import DumbAgent, RandomAgent, SearchAgent
from itertools import combinations
from judge import Judge
from simulation import Configuration

def main():
    configs = [
        Configuration(columns=10,  rows=10,  inarow=4,  first_move_agent=1),
        Configuration(columns=10,  rows=10,  inarow=4,  first_move_agent=2),
        Configuration(columns=20,  rows=20,  inarow=5,  first_move_agent=1),
        Configuration(columns=20,  rows=20,  inarow=5,  first_move_agent=2),
        Configuration(columns=40,  rows=40,  inarow=6,  first_move_agent=1),
        Configuration(columns=40,  rows=40,  inarow=6,  first_move_agent=2),
        # Configuration(columns=80,  rows=80,  inarow=10, first_move_agent=1),
        # Configuration(columns=80,  rows=80,  inarow=10, first_move_agent=2),
        # Configuration(columns=120, rows=120, inarow=20, first_move_agent=1),
        # Configuration(columns=120, rows=120, inarow=20, first_move_agent=2),
    ]

    agents = [
        RandomAgent(),
        DumbAgent(),
        SearchAgent(search_depth=1),
    ]

    results = None

    for agent1, agent2 in combinations(agents, r=2):
        print(f'{agent1.name} vs {agent2.name} ...')

        judge = Judge(configs=configs, agent1=agent2, agent2=agent1)
        _results = judge.run(runs_per_config=100)
        results = _results if results is None else pd.concat([results, _results], ignore_index=True)

    print(results)


if __name__ == '__main__':
    main()
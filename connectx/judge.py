import pandas as pd

from simulation import Configuration, Simulation

class Judge:
    def __init__(self, agent1, agent2, configs):
        self._agent1 = agent1
        self._agent2 = agent2
        self._configs = configs


    def run(self, runs_per_config):
        column_names = ['row_count', 'col_count', 'inarow', 'agent_1_starts', 'agent_1_wins', 'agent_2_wins', 'ties']

        rows = []
    
        for config in self._configs:
            agent1_win_count = 0
            agent2_win_count = 0
            tie_count = 0

            for _ in range(runs_per_config):
                sim = Simulation(config, agent1=self._agent1, agent2=self._agent2)
                _, winner, _ = sim.run()

                if winner == sim.first_move_agent_label:
                    agent1_win_count += 1
                elif winner == 0:
                    tie_count += 1
                else:
                    agent2_win_count += 1
            
            rows.append([
                config.rows,
                config.columns,
                config.inarow,
                config.first_move_agent == 1,
                agent1_win_count,
                agent2_win_count,
                tie_count,
            ])

        return pd.DataFrame(rows, columns=column_names)

import pandas as pd

from simulation import Configuration, Simulation

class Judge:
    def __init__(self, agent1, agent2, configs):
        self._agent1 = agent1
        self._agent2 = agent2
        self._configs = configs


    def run(self, runs_per_config, log=True):
        column_names = [
            'agent1_name',
            'agent2_name',
            'row_count',
            'col_count',
            'inarow',
            'agent_1_starts',
            'agent_1_wins',
            'agent_2_wins',
            'ties',
            'agent_1_avg_time_per_move',
            'agent_2_avg_time_per_move',
            'avg_moves_until_win',
        ]

        rows = []
    
        for ci, config in enumerate(self._configs):
            if log:
                print(f'Running Config: [{ci+1} / {len(self._configs)}]')

            agent1_win_count = 0
            agent2_win_count = 0
            tie_count = 0

            agent1_avg_move_time = 0.0
            agent2_avg_move_time = 0.0
            avg_move_count = 0.0

            for i in range(1, runs_per_config + 1):
                if log and i % 10 == 1:
                    print(f'Starting New Simulation: [{i} / {runs_per_config}]')
        
                sim = Simulation(config, agent1=self._agent1, agent2=self._agent2)
                _, winner, _, stats = sim.run()

                if winner == sim.first_move_agent_label:
                    agent1_win_count += 1
                elif winner == 0:
                    tie_count += 1
                else:
                    agent2_win_count += 1

                agent1_avg_move_time = agent1_avg_move_time + (1.0 / i) * (stats['avg_move_time'][0] - agent1_avg_move_time)
                agent2_avg_move_time = agent2_avg_move_time + (1.0 / i) * (stats['avg_move_time'][1] - agent2_avg_move_time)
                avg_move_count = avg_move_count + (1.0 / i) * (stats['move_count'] - avg_move_count)
            
            rows.append([
                self._agent1.name,
                self._agent2.name,
                config.rows,
                config.columns,
                config.inarow,
                config.first_move_agent == 1,
                agent1_win_count,
                agent2_win_count,
                tie_count,
                agent1_avg_move_time,
                agent2_avg_move_time,
                avg_move_count,
            ])

        return pd.DataFrame(rows, columns=column_names)

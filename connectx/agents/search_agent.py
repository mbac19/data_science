import numpy as np

from utils import check_win, drop_piece, is_board_full, possible_moves, toggle_player, undo_drop_piece

class SearchAgent:
    def __init__(self, max_depth, player):
        self.max_depth = max_depth
        self.player = player


    def choose_actions(self, board, configuration):
        return 0


    # Returns the best move at a given board position, and the value of that
    # move.
    def _evaluate(self, board, depth, active_player, inarow):
        columns = possible_moves(board)
        values = np.zeros(len(columns), dtype=np.int8)

        unknown_moves = []
        tie_moves = []

        for column in columns:
            row = drop_piece(board, column=column, player=active_player)

            if check_win(board, row=row, col=column, player=toggle_player(active_player), inarow=inarow):
                return (column, 1)
            elif is_board_full(board):
                tie_moves.append(column)
            elif depth == 0:
                # Unable to determine the value of this move. True value is
                # beyond the horizon.
                unknown_moves.append(column)
            else:
                # Exploring the subtree:
                # We are negating the value at this particular position. That
                # is because we are evaluating the position with respect to
                # the player making the move, which is the opponent.
                _, value = -self._evaluate_move(
                    board,
                    column=column,
                    depth=depth - 1,
                    player=toggle_player(active_player)
                )

                if value == 1:
                    return 1

            undo_drop_piece(board, column=column, player=active_player)

            np.argmax(best_move)
            return np.max(values)
        

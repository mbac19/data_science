import numpy as np

from utils import check_win, drop_piece, is_board_full, possible_moves, toggle_player, undo_drop_piece

class SearchAgent:
    def __init__(self, search_depth):
        assert(search_depth > 0)
        self.name = f'Search Agent (depth = {search_depth})'
        self.search_depth = search_depth


    def start_run(self, player):
        self.player = player


    def choose_action(self, board, configuration):
        return self._find_best_move(
            board,
            self.search_depth - 1,
            self.player,
            configuration.inarow
        )[0]


    # Returns the best move at a given board position, and the value of that
    # move.
    def _find_best_move(self, board, depth, active_player, inarow):
        columns = possible_moves(board)

        unknown_moves = []
        tie_moves = []

        for column in columns:
            row = drop_piece(board, column=column, player=active_player)

            if check_win(board, row=row, col=column, player=active_player, inarow=inarow):
                undo_drop_piece(board, column=column, player=active_player)
                return (column, 1)
            elif is_board_full(board):
                tie_moves.append(column)
            elif depth == 0:
                # Unable to determine the value of this move. True value is
                # beyond the search horizon.
                unknown_moves.append(column)
            else:
                # Exploring the subtree:
                # We are negating the value at this particular position. That
                # is because we are evaluating the position with respect to
                # the player making the move, which is the opponent.
                value = -self._find_best_move(
                    board=board,
                    depth=depth - 1,
                    active_player=toggle_player(active_player),
                    inarow=inarow
                )[1]

                # The opponent only saw losing moves when looking ahead from
                # this move. This is a winning move.
                if value == 1:
                    undo_drop_piece(board, column=column, player=active_player)
                    return (column, 1)
                elif value == 0:
                    unknown_moves.append(column)

            # Undo the changes we made to the board as we evaluated the subtree
            # of games from this point on. Allows us to explore subtree without
            # making copies of the board at each recursive step.
            undo_drop_piece(board, column=column, player=active_player)

        # Could not find a guaranteed win.
        if len(tie_moves) > 0:
            return (tie_moves[0], 0)
        elif len(unknown_moves) > 0:
            return (unknown_moves[0], 0)

        # No wins, ties, or unknown outcomes. We are in a losing position.
        return (columns[0], -1)
        

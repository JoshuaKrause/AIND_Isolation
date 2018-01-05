"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players
import timeit

from importlib import reload

TIME_LIMIT = 150
TIME_MILLIS = lambda: 1000 * timeit.default_timer()

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score)
        self.player2 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score_3)
        self.game = isolation.Board(self.player1, self.player2)

    def next_move(self, game, player):        
        time_limit = TIME_LIMIT
        move_start = TIME_MILLIS()
        time_left = lambda : time_limit - (TIME_MILLIS() - move_start)
        return player.get_move(game, time_left)

    def cycle_moves(self):
        self.game.apply_move(self.next_move(self.game, self.game.active_player))

    def test_quick_run(self):
        self.game.apply_move((2,2))
        for i in range(10):
            print(self.game.active_player)
            self.cycle_moves()
            print(self.game.to_string())

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise

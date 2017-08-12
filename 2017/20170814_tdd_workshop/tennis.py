"""
Tennis Game Kata

http://codingdojo.org/kata/Tennis/

This Kata is about implementing a simple tennis game.

The scoring system is rather simple:

1. Each player can have either of these points in one game 0 15 30 40

2. If you have 40 and you win the ball you win the game, however there are special rules.

3. If both have 40 the players are deuce.

  a. If the game is in deuce, the winner of a ball will have advantage and game ball.
  b. If the player with advantage wins the ball he wins the game
  c. If the player without advantage wins they are back at deuce.
"""
import unittest
from collections import OrderedDict


class Game(object):
    def __init__(self, *serves):
        self.scores = OrderedDict((
            (1, 0),
            (2, 0)
        ))

        for winner in serves:
            self.serve(winner)

    @property
    def score(self):
        return list(self.scores.values())

    @property
    def winner(self):
        pass

    def serve(self, winner):
        pass


class TennisGameTest(unittest.TestCase):
    def test_empty_score(self):
        game = Game()
        self.assertEqual([0, 0], game.score)


if __name__ == '__main__':
    unittest.main(exit=False)

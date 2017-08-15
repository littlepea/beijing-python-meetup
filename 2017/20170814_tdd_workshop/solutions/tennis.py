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
    SCORE_MAP = {
        0: 15,
        15: 30,
        30: 40
    }

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
        score1 = self.scores[1]
        score2 = self.scores[2]

        if score1 > 40 and score1 - score2 > 1:
            return 1

        if score2 > 40 and score2 - score1 > 1:
            return 2

    def serve(self, winner):
        if self.winner:
            return

        score = self.scores[winner]
        if score < 40:
            self.scores[winner] = self.SCORE_MAP[score]
        else:
            self.scores[winner] += 1


class TennisGameTest(unittest.TestCase):
    def test_empty_score(self):
        game = Game()
        self.assertEqual([0, 0], game.score)

    def test_blowout_game(self):
        game = Game(1, 1, 1, 1)
        self.assertEqual(1, game.winner)

    def test_blowout_game_for_player2(self):
        game = Game(2, 2, 2, 2)
        self.assertEqual(2, game.winner)

    def test_normal_game(self):
        game = Game(2, 1, 1, 2, 2, 2)
        self.assertEqual(2, game.winner)

    def test_simple_deuce(self):
        game = Game(1, 1, 1, 2, 2, 2, 2, 2)
        self.assertEqual(2, game.winner)

    def test_complex_deuce(self):
        game = Game(1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1)
        self.assertEqual(2, game.winner)


if __name__ == '__main__':
    unittest.main(exit=False)

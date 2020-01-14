class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    @property
    def game_over(self):
        diff = abs(self.p1points - self.p2points)
        max_score = max(self.p1points, self.p2points)
        return diff >= 2 and max_score >= 4

    @property
    def whos_winning(self):
        if self.p1points > self.p2points:
            return self.player1Name
        else:
            return self.player2Name

    @property
    def advantage_who(self):
        if self.p1points >= 4 or self.p2points >= 4 and \
                abs(self.p1points - self.p2points) == 1:
            return self.whos_winning

    def score(self):
        if self.game_over:
            return "Win for " + self.whos_winning
        if self.equal_points:
            return self.handle_equal_points()
        if self.advantage_who:
            return "Advantage " + self.advantage_who
        return self.handle_ongoing_score()

    def handle_ongoing_score(self):
        return f'{self.point_to_word(self.p1points)}-{self.point_to_word(self.p2points)}'

    def handle_equal_points(self):
        word = self.point_to_word(self.p1points)
        return word + '-All' if word else 'Deuce'

    @classmethod
    def point_to_word(cls, point):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }.get(point)

    @property
    def equal_points(self):
        return self.p1points == self.p2points

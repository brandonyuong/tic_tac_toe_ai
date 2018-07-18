import random


class PlayerTurn:

    # class helps determine player turn
    def __init__(self):
        self.first = None
        self.turn = None

        if not self.first:
            self.first = self.coinFlipForFirst()
        if not self.turn:
            self.turn = self.first

    @staticmethod
    def coinFlipForFirst():
        if random.randint(0, 1) == 0:
            return 'Player Two'
        else:
            return 'Player One'

    def setTurnOver(self):
        if self.turn == 'Player One':
            self.turn = 'Player Two'
        else:
            self.turn = 'Player One'

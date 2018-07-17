import random


class PlayerTurn:

    # class deals with the evaluation of a player turn
    def __init__(self):
        self.first = ""
        self.turn = ""

        if not self.first:
            self.first = self.coinFlipForFirst()
        if not self.turn:
            self.turn = self.first

    def coinFlipForFirst(self):
        if random.randint(0, 1) == 0:
            return 'Player Two'
        else:
            return 'Player One'

    def setTurnOver(self):
        if self.turn == 'Player One':
            self.turn = 'Player Two'
        else:
            self.turn = 'Player One'

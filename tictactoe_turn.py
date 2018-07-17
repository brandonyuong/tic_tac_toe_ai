import random


class PlayerTurn:

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

    def makeMove(self, board, letter, key):
        # Create move on board
        board[key - 1] = letter

    def isMoveOpen(self, board, key):
        # Return true if the passed key is free on the passed board.
        return board[key - 1] == ' '

    def getPlayerMove(self, board):
        # Let the player type in their move.
        key = ' '
        # make sure key is valid, and associated move is available
        while key not in '1 2 3 4 5 6 7 8 9'.split() or \
                not self.isMoveOpen(board, int(key)):
            print('What is your next move? (Use numpad 1-9)')
            key = input()
        return int(key)

    def setPlayerTurn(self, player):
        if player == 'Player One':
            self.turn = 'Player Two'
        else:
            self.turn = 'Player One'

    def playerOnePlays(self, board, playerLetter, saveState):
        # Player One's turn
        print(playerLetter + "'s turn.")
        key = self.getPlayerMove(board)
        self.makeMove(board, playerLetter, key)
        saveState.addState(self.turn, key)

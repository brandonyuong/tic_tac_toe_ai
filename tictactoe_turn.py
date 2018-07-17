
"""
class GameTurn:

    self.__first = self.coinFlipForFirst()
    self.turn = self.__first

"""
import random

def coinFlipForFirst():
    if random.randint(0, 1) == 0:
        return 'Player Two'
    else:
        return 'Player One'

def makeMove(board, letter, key):
    board[key - 1] = letter


def isMoveOpen(board, key):
    # Return true if the passed key is free on the passed board.

    return board[key - 1] == ' '


def getPlayerMove(board):
    # Let the player type in their move.

    key = ' '
    while key not in '1 2 3 4 5 6 7 8 9'.split() or \
            not isMoveOpen(board, int(key)):
        print('What is your next move? (Use numpad 1-9)')
        key = input()
    return int(key)


def isWinner(position, occupant):
    # Given a board and a player’s letter, check if player has won.

    return ((position[6] == occupant and position[7] == occupant and
             position[8] == occupant) or  # top row

            (position[3] == occupant and position[4] == occupant and
             position[5] == occupant) or  # middle row

            (position[0] == occupant and position[1] == occupant and
             position[2] == occupant) or  # bottom row

            (position[6] == occupant and position[3] == occupant and
             position[0] == occupant) or  # left column

            (position[7] == occupant and position[4] == occupant and
             position[1] == occupant) or  # middle column

            (position[8] == occupant and position[5] == occupant and
             position[2] == occupant) or  # right column

            (position[6] == occupant and position[4] == occupant and
             position[2] == occupant) or  # diagonal

            (position[8] == occupant and position[4] == occupant and
             position[0] == occupant))  # other diagonal


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.

    for k in range(1, 10):
        if isMoveOpen(board, k):
            return False
    return True
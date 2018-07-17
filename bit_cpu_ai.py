import random
from tictactoe_turn import isMoveOpen, makeMove, isWinner


"""
Bit is explicitly programmed to choose its move based on a set of predetermined rules:
1. If it can make a winning move, it will.
2. If it can prevent the player from winning, it will.
3. If the center position is open, it will take it.
4. If a corner position is open, it will take one.
5. Finally, if a side position is open, it will take one.
"""


def dupeBoard(board):
    # Make a duplicate of the board list and return the duplicate.

    duplicateBoard = []
    for i in board:
        duplicateBoard.append(i)
    return duplicateBoard


def chooseRandomMoveFromList(board, indexList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.

    possibleKeys = []
    for i in indexList:
        if isMoveOpen(board, i + 1):
            possibleKeys.append(i + 1)

    if len(possibleKeys) != 0:
        return random.choice(possibleKeys)
    else:
        return None

def getBitMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move

    for k in range(1, 10):
        copy = dupeBoard(board)
        if isMoveOpen(copy, k):
            makeMove(copy, computerLetter, k)
            if isWinner(copy, computerLetter):
                return k

    # Check if the player could win on their next move, and block them.

    for k in range(1, 10):
        copy = dupeBoard(board)
        if isMoveOpen(copy, k):
            makeMove(copy, playerLetter, k)
            if isWinner(copy, playerLetter):
                return k

    # Try to take the center, if it is free.

    if isMoveOpen(board, 5):
        return 5

    # Try to take one of the corners, if they are free.

    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
    if move != None:
        return move

    # Move on one of the sides.

    return chooseRandomMoveFromList(board, [1, 3, 5, 7])
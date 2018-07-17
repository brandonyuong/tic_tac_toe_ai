import random
from tictactoe_turn import PlayerTurn


def dupeBoard(board):
    # Make a duplicate of the board list and return the duplicate.

    duplicateBoard = []
    for i in board:
        duplicateBoard.append(i)
    return duplicateBoard


def chooseRandomMoveFromList(board, indexList, playerTurn):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.

    possibleKeys = []
    for i in indexList:
        if playerTurn.isMoveOpen(board, i + 1):
            possibleKeys.append(i + 1)

    if len(possibleKeys) != 0:
        return random.choice(possibleKeys)
    else:
        return None


def getBitMove(board, computerLetter, playerTurn):
    # use scripted algorithm to determine the best move and return that move

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # First, check if we can win in the next move
    for k in range(1, 10):
        copy = dupeBoard(board)
        if playerTurn.isMoveOpen(copy, k):
            playerTurn.makeMove(copy, computerLetter, k)
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


def getByteMove(saveState):
    # using class SaveStates, determine the best move from stored memory

    listOpenIndices = []
    for x in range(0, 9):
        if isMoveOpen(saveState.currentBoard, x + 1):
            listOpenIndices.append(x)

    """Print for testing:
    print('Open Spaces: {}'.format(listOpenIndices))
    print('Board image: {}'.format(self.currentBoard))
    """

    best = -1  # initialize bookmark for finding best p-value
    dictAfterstates = {}  # dictionary of P-values and possible move indices

    # Find P-value for each possible move from database.  Choose the best move.
    for y in listOpenIndices:
        copy = dupeBoard(saveState.currentBoard)
        copy[y] = saveState.player2
        retrieved = saveState.retrieveState(copy)

        # store p-value as dict-key; move index as dict-value
        if retrieved:
            # retrieved[2] is the retrieved p-value
            dictAfterstates[str(retrieved[2])] = y + 1
            if retrieved[2] > best:
                best = retrieved[2]
        else:
            # default p-value is 0.5 when no save state is retrieved
            dictAfterstates['0.5'] = y + 1
            if best < 0.5:
                best = 0.5

    """ Print for Testing:
        print('Best P-value = {}, Best move: {}, P-values: Moves = {}'
        .format(best, dictAfterstates[str(best)], dictAfterstates))
    """
    return dictAfterstates[str(best)]


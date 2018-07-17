import random


def makeMove(board, letter, key):
    # Create move on board
    board[key - 1] = letter


def isMoveOpen(board, key):
    # Return true if the passed key is free on the passed board.
    return board[key - 1] == ' '


def getPlayerMove(board):
    # Let the player type in their move.
    key = ' '
    keyStrList = list(map(str, range(1, 10)))

    # make sure key is valid, and associated move is available
    while key not in keyStrList or not isMoveOpen(board, int(key)):
        print('What is your next move? (Use numpad 1-9)')
        key = input()
    return int(key)


def isWinner(board, playerLetter):
    # Given a player’s letter, check if player has won.
    return ((board[6] == playerLetter and board[7] == playerLetter and
             board[8] == playerLetter) or  # top row

            (board[3] == playerLetter and board[4] == playerLetter and
             board[5] == playerLetter) or  # middle row

            (board[0] == playerLetter and board[1] == playerLetter and
             board[2] == playerLetter) or  # bottom row

            (board[6] == playerLetter and board[3] == playerLetter and
             board[0] == playerLetter) or  # left column

            (board[7] == playerLetter and board[4] == playerLetter and
             board[1] == playerLetter) or  # middle column

            (board[8] == playerLetter and board[5] == playerLetter and
             board[2] == playerLetter) or  # right column

            (board[6] == playerLetter and board[4] == playerLetter and
             board[2] == playerLetter) or  # diagonal

            (board[8] == playerLetter and board[4] == playerLetter and
             board[0] == playerLetter))  # other diagonal


def isBoardFull(board):
    # Test to see if every space on the board has been taken
    for k in range(1, 10):
        if isMoveOpen(board, k):
            return False
    return True


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
    # use scripted algorithm to determine the best move and return that move

    if computerLetter == 'X':
        opponentLetter = 'O'
    else:
        opponentLetter = 'X'

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
            makeMove(copy, opponentLetter, k)
            if isWinner(copy, opponentLetter):
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
    # input SaveStates object, determine the best move (key) from stored memory

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

        # store p-value as dict-key; move (key) as dict-value
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
    # return key, not index
    return dictAfterstates[str(best)]


def setTrainCount():
    print("How many games to train? Enter 1 or more: ")
    counter = input()
    while True:
        try:
            counter = int(counter)
            if counter > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Entered: {}. Must enter positive integer!".format(
                counter))
            counter = input()
    return counter

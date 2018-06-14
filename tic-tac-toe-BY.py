import random


def printBoard(board):
    # 'board' is a string list that represents the board
    print( '\n -----------')
    print( '| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print( ' -----------')
    print( '| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print( ' -----------')
    print( '| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print( ' -----------\n')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def selectCPU():
    selection = ''
    while not (selection =='bit' or selection =='byte'):
        print('Play vs. Bit or Byte? (Bit = Unbeatable AI; Byte = Machine Learning AI)?')
        selection = input().lower()
    if selection == 'bit':
        return 'bit'
    else:
        return 'byte'


def coinFlipForFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def restart():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def isWinner(position, occupant):
    # Given a board and a player’s letter, this function returns True if that player has won.

    return ((position[6] == occupant and position[7] == occupant and position[8] == occupant) or  # top row
            (position[3] == occupant and position[4] == occupant and position[5] == occupant) or  # middle row
            (position[0] == occupant and position[1] == occupant and position[2] == occupant) or  # bottom row
            (position[6] == occupant and position[3] == occupant and position[0] == occupant) or  # left column
            (position[7] == occupant and position[4] == occupant and position[1] == occupant) or  # middle column
            (position[8] == occupant and position[5] == occupant and position[2] == occupant) or  # right column
            (position[6] == occupant and position[4] == occupant and position[2] == occupant) or  # diagonal
            (position[8] == occupant and position[4] == occupant and position[0] == occupant))    # other diagonal


def dupeBoard(board):
    # Make a duplicate of the board list and return the duplicate.

    duplicateBoard = []
    for i in board:
        duplicateBoard.append(i)
    return duplicateBoard


def makeMove(board, letter, key):
    board[key - 1] = letter


def isMoveOpen(board, key):
    # Return true if the passed key is free on the passed board.

    return board[key - 1] == ' '


def getPlayerMove(board):
    # Let the player type in their move.

    key = ' '
    while key not in '1 2 3 4 5 6 7 8 9'.split() or not isMoveOpen(board, int(key)):
        print('What is your next move? (Use numpad 1-9)')
        key = input()
    return int(key)


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


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.

    for k in range(1, 10):
        if isMoveOpen(board, k):
            return False
    return True


# Start new game
print('Welcome to Tic Tac Toe!')
playerLetter, computerLetter = inputPlayerLetter()
bitOrByte = selectCPU()


while True:
# Initiate infinite Restart loop until broken

    theBoard = [' '] * 9
    turn = coinFlipForFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':
            # Player’s turn.

            printBoard(theBoard)
            key = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, key)
            if isWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.

            if bitOrByte == 'bit':
                key = getBitMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, key)
                if isWinner(theBoard, computerLetter):
                    printBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        printBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

            if bitOrByte == 'byte':
                pass

    if not restart():
        # Restart the board or not
        break
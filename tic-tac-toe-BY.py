import random


def printBoard(board):
    # 'board' is a string list that represents the board (ignoring index 0)
    print( '\n -----------')
    print( '| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print( ' -----------')
    print( '| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print( ' -----------')
    print( '| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
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


def coinFlipForFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def restart():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(position, occupant):
    # Given a board and a player’s letter, this function returns True if that player has won.

    return ((position[7] == occupant and position[8] == occupant and position[9] == occupant) or  # top row
            (position[4] == occupant and position[5] == occupant and position[6] == occupant) or  # middle row
            (position[1] == occupant and position[2] == occupant and position[3] == occupant) or  # bottom row
            (position[7] == occupant and position[4] == occupant and position[1] == occupant) or  # left column
            (position[8] == occupant and position[5] == occupant and position[2] == occupant) or  # middle column
            (position[9] == occupant and position[6] == occupant and position[3] == occupant) or  # right column
            (position[7] == occupant and position[5] == occupant and position[3] == occupant) or  # diagonal
            (position[9] == occupant and position[5] == occupant and position[1] == occupant))    # other diagonal


def dupeBoard(board):
    # Make a duplicate of the board list and return the duplicate.

    duplicateBoard = []
    for i in board:
        duplicateBoard.append(i)
    return duplicateBoard


def isSpaceOpen(board, move):
    # Return true if the passed move is free on the passed board.

    return board[move] == ' '


def getPlayerMove(board):
    # Let the player type in their move.

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceOpen(board, int(move)):
        print('What is your next move? (Use numpad 1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.

    possibleMoves = []
    for i in movesList:
        if isSpaceOpen(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move

    for i in range(1, 10):
        copy = dupeBoard(board)
        if isSpaceOpen(copy, i):
             makeMove(copy, computerLetter, i)
             if isWinner(copy, computerLetter):
                 return i

    # Check if the player could win on their next move, and block them.

    for i in range(1, 10):
        copy = dupeBoard(board)
        if isSpaceOpen(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.

    if isSpaceOpen(board, 5):
        return 5

    # Move on one of the sides.

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.

    for i in range(1, 10):
        if isSpaceOpen(board, i):
            return False
    return True


# Start new game
print('Welcome to Tic Tac Toe!')
playerLetter, computerLetter = inputPlayerLetter()


while True:
# Initiate infinite Restart loop until broken

    theBoard = [' '] * 10
    turn = coinFlipForFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':
            # Player’s turn.

            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
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

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
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

    if not restart():
        # Restart the board or not
        break
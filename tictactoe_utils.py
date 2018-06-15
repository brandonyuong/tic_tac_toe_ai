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


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.

    for k in range(1, 10):
        if isMoveOpen(board, k):
            return False
    return True
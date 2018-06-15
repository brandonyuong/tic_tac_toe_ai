from tictactoe_utils import inputPlayerLetter, coinFlipForFirst, selectCPU, printBoard, getPlayerMove, makeMove, \
    isWinner, isBoardFull, restart

from bit_cpu_ai import getBitMove
from byte_cpu_ai import SaveStates
from database import Database

# Start new game
print('Welcome to Tic Tac Toe! Initiating game...')
username = input("PostgreSQL user: ")
userpw = input("PostgreSQL password: ")
Database.initialise(user=username, password=userpw, host='localhost', database='learning2')
playerLetter, computerLetter = inputPlayerLetter()
bitOrByte = selectCPU()



while True:
# Initiate infinite Restart loop until broken

    theBoard = [' '] * 9
    first = coinFlipForFirst()
    turn = first
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    gameSave = SaveStates(first)
    numberTurns = -1

    while gameIsPlaying:

        if turn == 'player':
            # Player’s turn.

            printBoard(theBoard)
            key = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, key)
            gameSave.addState(turn, key)
            numberTurns += 1

            if isWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print('Hooray! You have won the game!')
                gameSave.recordState(numberTurns)
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
                gameSave.addState(turn, key)
                numberTurns += 1

                if isWinner(theBoard, computerLetter):
                    printBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameSave.recordState(numberTurns)
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
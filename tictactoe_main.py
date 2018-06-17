from tictactoe_utils import inputPlayerLetter, coinFlipForFirst, selectCPU, printBoard, getPlayerMove, makeMove, \
    isWinner, isBoardFull, restart

from bit_cpu_ai import getBitMove
from byte_cpu_ai import SaveStates
from database import Database

# Start new game
print('Welcome to Tic Tac Toe! Initiating game...')
# Showing database details in the code is not good practice. Should be stored in a separate config file.
# In this case, this database is a read-only demo so you can try the current sample of the machine learning AI.
Database.initialise(dbname='learning', user='guestbyml@bymlserv', password='sinc0320', host='bymlserv.postgres.database.azure.com', port='5432', sslmode='require')
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
                    print('Bit has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        printBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

            if bitOrByte == 'byte':
                key = gameSave.getByteMove()
                makeMove(theBoard, computerLetter, key)
                gameSave.addState(turn, key)
                numberTurns += 1

                if isWinner(theBoard, computerLetter):
                    printBoard(theBoard)
                    print('Byte has beaten you! You lose.')
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

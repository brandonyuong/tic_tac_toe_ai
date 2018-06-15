from tictactoe_utils import inputPlayerLetter, coinFlipForFirst, printBoard, getPlayerMove, makeMove, \
    isWinner, isBoardFull, restart

from cpu_ai import selectCPU, getBitMove
from save_states import SaveStates

# Start new game
print('Welcome to Tic Tac Toe!')
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

    while gameIsPlaying:

        if turn == 'player':
            # Player’s turn.

            printBoard(theBoard)
            key = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, key)
            gameSave.addState(turn, key)
            print(gameSave) # Testing

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
                print(gameSave) # Testing
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
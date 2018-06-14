from tictactoe_utils import inputPlayerLetter, coinFlipForFirst, printBoard, getPlayerMove, makeMove, \
    isWinner, isBoardFull, restart

from cpu_ai import selectCPU, getBitMove


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
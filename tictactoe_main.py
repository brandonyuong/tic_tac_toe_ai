from tictactoe_game import TicTacToeGame
from tictactoe_turn import makeMove, getPlayerMove, isWinner, isBoardFull, \
    coinFlipForFirst
from bit_cpu_ai import getBitMove
from byte_cpu_ai import SaveStates
from database import Database

# Start new game
print('Welcome to Tic Tac Toe! Loading game...')
"""
This database is a read-only demo so you can try the current sample of the 
machine learning AI, Byte.  I.e. the AI has already learned, and the learning 
function is disabled.
"""
Database.initialise(dbname='learning', user='guestbyml@bymlserv',
                    password='sinc0320',
                    host='bymlserv.postgres.database.azure.com',
                    port='5432', sslmode='require')

# initial game settings
game = TicTacToeGame()
game.selectHumanOrCpu()
game.setPlayerLetter()

while True:

    game.resetGame()
    first = coinFlipForFirst()
    turn = first
    print('Game begins, ' + turn + ' will go first.')
    gameSave = SaveStates(first)

    while game.playing:
        if turn == 'Player One':
            # Player’s turn.

            game.printBoard()
            print(game.playerOneLetter + "'s turn.")
            key = getPlayerMove(game.board)
            makeMove(game.board, game.playerOneLetter, key)
            gameSave.addState(turn, key)
            game.numberTurns += 1

            if isWinner(game.board, game.playerOneLetter):
                game.printBoard()
                print('Player One has won the game!')
                game.playing = False
            else:
                if isBoardFull(game.board):
                    game.printBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player Two'

        else:
            # Player 2’s turn.

            if game.playerTwo == 'human':
                game.printBoard()
                print(game.playerTwoLetter + "'s turn.")
                key = getPlayerMove(game.board)
                makeMove(game.board, game.playerTwoLetter, key)
                gameSave.addState(turn, key)
                game.numberTurns += 1

                if isWinner(game.board, game.playerTwoLetter):
                    game.printBoard()
                    print('Player Two has won the game!')
                    game.playing = False
                else:
                    if isBoardFull(game.board):
                        game.printBoard()
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player One'

            if game.playerTwo == 'bit':
                key = getBitMove(game.board, game.playerTwoLetter)
                makeMove(game.board, game.playerTwoLetter, key)
                gameSave.addState(turn, key)
                game.numberTurns += 1

                if isWinner(game.board, game.playerTwoLetter):
                    game.printBoard()
                    print('Bit has beaten you! You lose.')
                    game.playing = False
                else:
                    if isBoardFull(game.board):
                        game.printBoard()
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player One'

            if game.playerTwo == 'byte':
                key = gameSave.getByteMove()
                makeMove(game.board, game.playerTwoLetter, key)
                gameSave.addState(turn, key)
                game.numberTurns += 1

                if isWinner(game.board, game.playerTwoLetter):
                    game.printBoard()
                    print('Byte has beaten you! You lose.')
                    game.playing = False
                else:
                    if isBoardFull(game.board):
                        game.printBoard()
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player One'

    # Restart the board or not
    endChoice = game.endMenu()
    if endChoice == 'p':
        continue
    if endChoice == 'q':
        break

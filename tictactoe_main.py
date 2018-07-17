# -----------------------------------------------------------------------------
# Name:        Tic Tac Toe
# Purpose:     Program plays Tic Tac Toe from console
#
# Author:      Brandon Yuong
# -----------------------------------------------------------------------------
"""
A Python Tic Tac Toe game that plays from the console.

User has several options in the game: 2 players, 1 player vs AI.
AI includes scripted algorithm version and machine learning version.
"""

from tictactoe_game import TicTacToeGame
from tictactoe_turn import PlayerTurn
from cpu_ai import getBitMove, getByteMove
from savestates import SaveStates
from database import Database

print('Welcome to Tic Tac Toe! Loading game...')

"""
This database is a read-only demo so you can try a sample of the machine 
learning AI, Byte.
The AI has already learned, and the learning function is disabled.
"""
Database.initialise(dbname='learning', user='guestbyml@bymlserv',
                    password='sinc0320',
                    host='bymlserv.postgres.database.azure.com',
                    port='5432', sslmode='require')

# initial game settings
game = TicTacToeGame()
game.selectHumanOrCpu()
game.setPlayerLetter()

# start game loop
while True:

    game.resetGame()
    whoseTurn = PlayerTurn()
    print('Game begins, ' + whoseTurn.turn + ' will go first.')
    gameSave = SaveStates(whoseTurn.first)

    while game.playing:
        if whoseTurn.turn == 'Player One':
            if game.playerOne == 'human':
                game.printBoard()
            whoseTurn.playerOnePlays(game.board,
                                     game.playerOneLetter, gameSave)
            game.numberTurns += 1

            game.isEnding(whoseTurn.turn)

        else:
            # Player 2’s turn
            if game.playerTwo == 'human':
                game.printBoard()
                print(game.playerTwoLetter + "'s turn.")
                key = getPlayerMove(game.board)
                makeMove(game.board, game.playerTwoLetter, key)
                gameSave.addState(whoseTurn.turn, key)
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
                        whoseTurn.turn = 'Player One'

            if game.playerTwo == 'bit':
                key = getBitMove(game.board, game.playerTwoLetter)
                makeMove(game.board, game.playerTwoLetter, key)
                gameSave.addState(whoseTurn.turn, key)
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
                        whoseTurn.turn = 'Player One'

            if game.playerTwo == 'byte':
                key = getByteMove(gameSave)
                makeMove(game.board, game.playerTwoLetter, key)
                gameSave.addState(whoseTurn.turn, key)
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
                        whoseTurn.turn = 'Player One'

    # Restart the board or not
    endChoice = game.endMenu()
    if endChoice == 'p':
        continue
    if endChoice == 'q':
        break

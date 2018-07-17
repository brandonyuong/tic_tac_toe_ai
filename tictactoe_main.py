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
game.playerOne = 'human'
game.playerTwo = game.setHumanOrCpu()
game.setPlayerLetter()

# start game loop
while True:

    game.resetGame()
    whoseTurn = PlayerTurn()
    print('Game begins, ' + whoseTurn.turn + ' will go first.')
    gameSave = SaveStates(whoseTurn.first)

    while game.playing:
        game.playTurn(whoseTurn.turn, gameSave)
        if not game.isContinuing(whoseTurn.turn):
            break
        else:
            whoseTurn.setTurnOver()

    # Restart the board or not
    endChoice = game.endMenu()
    if endChoice == 'p':
        continue
    if endChoice == 'q':
        break

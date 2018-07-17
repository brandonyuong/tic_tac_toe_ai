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
from tictactoe_player import Player
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
playerOne = Player()
playerTwo = Player()

# set human or AI (Bit or Byte)
playerTwo.setController()

# set player letters
print("Player One,")
playerOne.setLetter()
if playerOne.letter == 'X':
    playerTwo.setLetter('O')
else:
    playerTwo.setLetter('X')

while True:
    # start new game
    game.resetGame()
    whoseTurn = PlayerTurn()
    print('Game begins, ' + whoseTurn.turn + ' will go first.')
    gameSave = SaveStates(whoseTurn.first)

    # players take turns until game ends
    while game.playing:
        if whoseTurn.turn == "Player One":
            player = playerOne
        else:
            player = playerTwo

        game.playTurn(player, whoseTurn, gameSave)
        if not game.isContinuing(player):
            break
        else:
            whoseTurn.setTurnOver()

    # Restart the game or not
    endChoice = game.endMenu()
    if endChoice == 'p':
        continue
    elif endChoice == 'q':
        break
    else:
        playerTwo.setController()
        print("Player One,")
        playerOne.setLetter()
        if playerOne.letter == 'X':
            playerTwo.setLetter('O')
        else:
            playerTwo.setLetter('X')
        continue

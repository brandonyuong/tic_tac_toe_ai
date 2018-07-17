from game_utils import isWinner, isBoardFull, makeMove, getBitMove, \
    getByteMove, getPlayerMove

class TicTacToeGame:

    # class deals with board and macro aspects of the game
    def __init__(self):
        self.board = [' '] * 9
        self.playing = True
        self.playerOneLetter = ''
        self.playerTwoLetter = ''
        self.numberTurns = -1
        self.playerOne = ''
        self.playerTwo = ''

    def resetGame(self):
        self.board = [' '] * 9
        self.playing = True

    def printBoard(self):
        # 'board' is a string list that represents the board
        print('\n -----------')
        for i in range(0, 3):
            row = "| "
            for j in range(6 - i * 3, 9 - i * 3):
                row += (self.board[j] + ' | ')
            print(row)
            print(' -----------')

    def setPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Player One, do you want to be X or O?')
            letter = input().upper()

        if letter == 'X':
            self.playerOneLetter = 'X'
            self.playerTwoLetter = 'O'
        else:
            self.playerOneLetter = 'O'
            self.playerTwoLetter = 'X'

    @staticmethod
    def setHumanOrCpu():
        selection = ''
        while not (selection == 'human' or selection == 'bit' or
                   selection == 'byte'):
            print(
                'Play vs. human, Bit, or Byte? (Bit = Scripted AI; '
                'Byte = Machine Learning AI (unbeatable)?')
            selection = input().lower()
        if selection == 'human':
            return 'human'
        elif selection == 'bit':
            return 'bit'
        else:
            return 'byte'

    def playTurn(self, playerTurn, saveState):
        # input game and save states. Process turn and record
        if playerTurn == "Player One":
            playerLetter = self.playerOneLetter
            controllerType = self.playerOne
        else:
            playerLetter = self.playerTwoLetter
            controllerType = self.playerTwo

        self.printBoard()
        print(playerTurn + "'s turn.")

        # decide key based on what is playing
        if controllerType == "human":
            key = getPlayerMove(self.board)
        if controllerType == "bit":
            key = getBitMove(self.board, playerLetter)
        if controllerType == "byte":
            key = getByteMove(saveState)

        makeMove(self.board, playerLetter, key)
        saveState.addState(playerTurn, key)
        self.numberTurns += 1

    def isContinuing(self, playerTurn):
        # input name of the player whose turn it is, see if game ends or not
        if playerTurn == "Player One":
            playerLetter = self.playerOneLetter
        else:
            playerLetter = self.playerTwoLetter
        if isWinner(self.board, playerLetter):
            self.printBoard()
            print(playerLetter + ' has won the game!')
            self.playing = False
            return False
        else:
            if isBoardFull(self.board):
                self.printBoard()
                print('The game is a tie!')
                self.playing = False
                return False
            else:
                return True

    def endMenu(self):
        letter = ''
        while not (letter == 'p' or letter == 'q' or letter == 'r'):
            print("\n*** Menu ***\n"
                  "p - Play again\n"
                  "q - Quit game\n"
                  "r - Reset settings")
            letter = input().lower()
        if letter == 'p':
            return 'p'
        if letter == 'q':
            return 'q'
        if letter == 'r':
            self.playerTwo = self.setHumanOrCpu()
            self.setPlayerLetter()
            return 'p'

class TicTacToeGame:

    def __init__(self):
        self.board = [' '] * 9
        self.playing = True
        self.playerOneLetter = ''
        self.playerTwoLetter = ''
        self.numberTurns = -1
        self.playerOne = 'human'
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

    def selectHumanOrCpu(self):
        selection = ''
        while not (selection == 'human' or selection == 'bit' or
                   selection == 'byte'):
            print(
                'Play vs. human, Bit, or Byte? (Bit = Scripted AI; '
                'Byte = Machine Learning AI (unbeatable)?')
            selection = input().lower()
        if selection == 'human':
            self.playerTwo = 'human'
        elif selection == 'bit':
            self.playerTwo = 'bit'
        else:
            self.playerTwo = 'byte'

    def setTrainCount(self):
        print("How many games to train? Enter 1 or more: ")
        counter = input()
        while True:
            try:
                counter = int(counter)
                if counter > 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Entered: {}. Must enter positive integer!".format(
                    counter))
                counter = input()
        return counter

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
            self.selectHumanOrCpu()
            self.setPlayerLetter()
            return 'p'

    def isWinner(self, playerLetter):
        # Given a player’s letter, check if player has won.
        return ((self.board[6] == playerLetter and self.board[7] == playerLetter and
                 self.board[8] == playerLetter) or  # top row

                (self.board[3] == playerLetter and self.board[4] == playerLetter and
                 self.board[5] == playerLetter) or  # middle row

                (self.board[0] == playerLetter and self.board[1] == playerLetter and
                 self.board[2] == playerLetter) or  # bottom row

                (self.board[6] == playerLetter and self.board[3] == playerLetter and
                 self.board[0] == playerLetter) or  # left column

                (self.board[7] == playerLetter and self.board[4] == playerLetter and
                 self.board[1] == playerLetter) or  # middle column

                (self.board[8] == playerLetter and self.board[5] == playerLetter and
                 self.board[2] == playerLetter) or  # right column

                (self.board[6] == playerLetter and self.board[4] == playerLetter and
                 self.board[2] == playerLetter) or  # diagonal

                (self.board[8] == playerLetter and self.board[4] == playerLetter and
                 self.board[0] == playerLetter))  # other diagonal

    def isBoardFull(self):
        # Test to see if every space on the board has been taken
        for k in range(1, 10):
            if self.isMoveOpen(self.board, k):
                return False
        return True

    def isEnding(self, turn):
        if turn == "Player One":
            playerLetter = self.playerOneLetter
        else:
            playerLetter = self.playerTwoLetter
        if self.isWinner(playerLetter):
            self.printBoard()
            print('Player One has won the game!')
            self.playing = False
            return
        else:
            if self.isBoardFull():
                self.printBoard()
                print('The game is a tie!')
                self.playing = False
                return
            else:
                return turn

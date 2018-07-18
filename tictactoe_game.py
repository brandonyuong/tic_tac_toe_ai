from game_utils import isWinner, isMoveOpen, makeMove, getBitMove, \
    getByteMove, getPlayerMove


class TicTacToeGame:

    # class deals with game board and macro aspects of the game
    def __init__(self):
        self.board = [' '] * 9
        self.playing = True
        self.numberTurns = -1
        self.ties = 0
        self.totalGames = 0

    def resetGame(self):
        self.board = [' '] * 9
        self.playing = True
        self.numberTurns = -1

    def printBoard(self):
        print('\n -----------')
        for i in range(0, 3):
            row = "| "
            for j in range(6 - i * 3, 9 - i * 3):
                row += (self.board[j] + ' | ')
            print(row)
            print(' -----------')

    def playTurn(self, player, playerTurn, saveState):
        # input player, turn, and savestate objects. Process turn and record
        self.printBoard()
        print(player.letter + " / " + playerTurn.turn + "'s turn.")

        # decide key based on what is playing
        if player.controller == "human":
            key = getPlayerMove(self.board)
        if player.controller == "bit":
            key = getBitMove(self.board, player.letter)
        if player.controller == "byte":
            key = getByteMove(saveState)

        makeMove(self.board, player.letter, key)
        saveState.addState(playerTurn.turn, key)
        self.numberTurns += 1

    def isContinuing(self, player):
        # input player, check if game ends
        if isWinner(self.board, player.letter):
            self.printBoard()
            print(player.letter + ' has won the game!')
            player.wins += 1
            self.totalGames += 1
            self.playing = False
            return False
        else:
            if self.isBoardFull():
                self.printBoard()
                print('The game is a tie!')
                self.ties += 1
                self.totalGames += 1
                self.playing = False
                return False
            else:
                return True

    def isBoardFull(self):
        # Test to see if every space on the board has been taken
        for k in range(1, 10):
            if isMoveOpen(self.board, k):
                return False
        return True

    @staticmethod
    def endMenu():
        letter = ''
        while not (letter == 'p' or letter == 'q' or letter == 'r'):
            print("\n*** Menu ***\n"
                  "p - Play again\n"
                  "q - Quit game\n"
                  "r - Reset settings & counters")
            letter = input().lower()
        if letter == 'p':
            return 'p'
        elif letter == 'q':
            return 'q'
        else:
            return 'r'

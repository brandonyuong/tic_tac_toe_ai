from game_utils import isWinner, isBoardFull, makeMove, getBitMove, \
    getByteMove, getPlayerMove

class TicTacToeGame:

    # class deals with game board and macro aspects of the game
    def __init__(self):
        self.board = [' '] * 9
        self.playing = True
        self.numberTurns = -1

    def resetGame(self):
        self.board = [' '] * 9
        self.playing = True

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

    @staticmethod
    def endMenu():
        letter = ''
        while not (letter == 'p' or letter == 'q' or letter == 'r'):
            print("\n*** Menu ***\n"
                  "p - Play again\n"
                  "q - Quit game\n"
                  "r - Reset settings")
            letter = input().lower()
        if letter == 'p':
            return 'p'
        elif letter == 'q':
            return 'q'
        else:
            return 'r'



class SaveStates:
    def __init__(self, first):
        self.statesBoard = []
        self.currentBoard = [' '] * 9
        self.pValue = 0.5

        if first == 'player':
            self.player = 'A'
            self.cpu = 'B'
        elif first == 'computer':
            self.player = 'B'
            self.cpu = 'A'

    def __repr__(self):
        return "<Current ANN Board: {}".format(self.currentBoard)

    def addState(self, whoseTurn, moveKey):
        if whoseTurn == 'player':
            agent = self.player
        else:
            agent = self.cpu
        self.currentBoard[moveKey - 1] = agent

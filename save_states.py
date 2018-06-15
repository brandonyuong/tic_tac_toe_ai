

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
        return "<Current Turn Image: {}\n" \
               "Save States: {}".format(self.currentBoard, self.statesBoard)


    def addState(self, whoseTurn, moveKey):
        if whoseTurn == 'player':
            agent = self.player
        else:
            agent = self.cpu
        self.currentBoard[moveKey - 1] = agent
        image = []
        for i in self.currentBoard:
            image.append(i)
        self.statesBoard.append(image)
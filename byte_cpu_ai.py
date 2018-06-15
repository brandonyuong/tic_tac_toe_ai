from database import CursorFromConnectionFromPool


"""
Byte is based on an artificial neural network (ANN). Byte learns every time the game is played. At the start of its
turns, Byte retrieves recorded game states for its possible moves and picks the one with the highest P-value
(probability of winning). Byte records the game state of each turn and adjusts the recorded P-value of each game state
at the end of a game based on the outcome. Byte is able to learn from players and other computer AI.
"""


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

    def retrievePvalue(self, gameState):
        pass # retrieve P-value from database

    def recordState(self):
        # Reward winning state by assigning 1 to its P-value
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'INSERT INTO ann_ttt (savestate, pvalue) VALUES (%s, %s)',
                (self.statesBoard[9], 1))
        afterstate_pvalue = 1
        counter = 8
        while counter:
            alpha = 0.1 # learning rate
            retrieved = retrievePvalue(self.statesBoard[counter])
            if retrieved:
                recorded_pvalue = retrieved
            else:
                recorded_pvalue = 0.5
            new_pvalue = recorded_pvalue + alpha * (afterstate_pvalue - recorded_pvalue)
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'INSERT INTO ann_ttt (savestate, pvalue) VALUES (%s, %s)',
                    (self.statesBoard[counter], new_pvalue))
            afterstate_pvalue = new_pvalue
            counter -= 1


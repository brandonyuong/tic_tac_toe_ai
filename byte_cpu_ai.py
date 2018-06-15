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


    def retrieveState(self, gameState):
        # Returns data from database as list [id, savestate, pvalue]
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM ann_ttt WHERE savestate=%s', (gameState,))  # Cursor stores data
            retrievedData = cursor.fetchone()  # fetchone is first row
            # id=retrievedData[0], savestate=retrievedData[1], pvalue=retrievedData[2]
            return retrievedData


    def recordState(self, numTurns):
        # Reward winning state by assigning 1 to its P-value
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'INSERT INTO ann_ttt (savestate, pvalue) VALUES (%s, %s)',
                (self.statesBoard[numTurns], 1))
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'INSERT INTO ann_ttt (savestate, pvalue) VALUES (%s, %s)',
                (self.statesBoard[numTurns - 1], 0))
        afterstate_pvalue = 1
        numTurns = numTurns - 2
        while numTurns >= 0:
            alpha = 0.1 # learning rate
            retrieved = self.retrieveState(self.statesBoard[numTurns])
            if retrieved:
                recorded_pvalue = retrieved[2]
                new_pvalue = recorded_pvalue + alpha * (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'UPDATE ann_ttt SET pvalue=%s WHERE savestate=%s',
                        (new_pvalue, self.statesBoard[numTurns]))
                afterstate_pvalue = new_pvalue
                numTurns -= 1
            else:
                recorded_pvalue = 0.5
                new_pvalue = recorded_pvalue + alpha * (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'INSERT INTO ann_ttt (savestate, pvalue) VALUES (%s, %s)',
                        (self.statesBoard[numTurns], new_pvalue))
                afterstate_pvalue = new_pvalue
                numTurns -= 1


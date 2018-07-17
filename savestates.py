from database import CursorFromConnectionFromPool
from cpu_ai import dupeBoard

"""
Byte learns every time the game is played. At the start of its turns, Byte retrieves recorded game states for its 
possible moves and picks the one with the highest P-value (probability of winning). Byte records the game state of each 
turn and adjusts the recorded P-value of each game state at the end of a game based on the outcome. Byte is able to 
learn from players and other computer AI.
"""

class SaveStates:
    def __init__(self, first):
        self.statesBoard = []
        self.currentBoard = [' '] * 9
        self.table = 'ann_ttt'  # Name of db
        self.alpha = 0.1  # learning rate

        # Track who played first
        if first == 'Player One':
            self.player1 = 'A'
            self.player2 = 'B'
        elif first == 'Player Two':
            self.player1 = 'B'
            self.player2 = 'A'

    def __repr__(self):
        return "<Current Turn Image: {}\n" \
               "Save States: {}".format(self.currentBoard, self.statesBoard)


    def addState(self, whoseTurn, moveKey):
        if whoseTurn == 'Player One':
            agent = self.player1
        else:
            agent = self.player2
        self.currentBoard[moveKey - 1] = agent
        image = dupeBoard(self.currentBoard)
        self.statesBoard.append(image)


    def retrieveState(self, gameState):
        # Returns data from database as list
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM {} WHERE savestate=%s'.format(self.table), (gameState,))  # Cursor stores data
            retrievedData = cursor.fetchone()  # fetchone is first row
            # id: retrievedData[0], savestate: retrievedData[1], pvalue: retrievedData[2]
            if retrievedData:
                return [retrievedData[0], retrievedData[1], retrievedData[2]]


    def recordState(self, winnerCounter):
        loserCounter = winnerCounter - 1

        # Reward winning state by assigning 1 to its P-value
        retrieveWinState = self.retrieveState(self.statesBoard[winnerCounter])
        if not retrieveWinState:
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'INSERT INTO {} (savestate, pvalue) VALUES (%s, %s)'.format(self.table),
                    (self.statesBoard[winnerCounter], 1))
        else:
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'UPDATE {} SET pvalue=%s WHERE savestate=%s'.format(self.table),
                    (1, self.statesBoard[winnerCounter]))
        afterstate_pvalue = 1
        winnerCounter = winnerCounter - 2

        # Reward states leading to winning state with small increase to P-value
        while winnerCounter >= 0:
            retrieved = self.retrieveState(self.statesBoard[winnerCounter])
            if retrieved:
                recorded_pvalue = retrieved[2]
                new_pvalue = recorded_pvalue + self.alpha * (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'UPDATE {} SET pvalue=%s WHERE savestate=%s'.format(self.table),
                        (new_pvalue, self.statesBoard[winnerCounter]))
                afterstate_pvalue = new_pvalue
                winnerCounter -= 2
            else:
                recorded_pvalue = 0.5
                new_pvalue = recorded_pvalue + self.alpha * (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'INSERT INTO {} (savestate, pvalue) VALUES (%s, %s)'.format(self.table),
                        (self.statesBoard[winnerCounter], new_pvalue))
                afterstate_pvalue = new_pvalue
                winnerCounter -= 2

        # Punish losing state by assigning 0 to its P-value
        retrieveLossState = self.retrieveState(self.statesBoard[loserCounter])
        if not retrieveLossState:
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'INSERT INTO {} (savestate, pvalue) VALUES (%s, %s)'.format(self.table),
                    (self.statesBoard[loserCounter], 0))
        else:
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'UPDATE {} SET pvalue=%s WHERE savestate=%s'.format(self.table),
                    (0, self.statesBoard[loserCounter]))
        afterstate_pvalue = 0
        loserCounter = loserCounter - 2

        # Punish states leading to losing state with small decrease to P-value
        while loserCounter >= 0:
            retrieved = self.retrieveState(self.statesBoard[loserCounter])
            if retrieved:
                recorded_pvalue = retrieved[2]
                new_pvalue = recorded_pvalue + self.alpha * (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'UPDATE {} SET pvalue=%s WHERE savestate=%s'.format(self.table),
                        (new_pvalue, self.statesBoard[loserCounter]))
                afterstate_pvalue = new_pvalue
                loserCounter -= 2
            else:
                recorded_pvalue = 0.5
                new_pvalue = recorded_pvalue + self.alpha * (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'INSERT INTO {} (savestate, pvalue) VALUES (%s, %s)'.format(self.table),
                        (self.statesBoard[loserCounter], new_pvalue))
                afterstate_pvalue = new_pvalue
                loserCounter -= 2

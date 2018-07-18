from database import CursorFromConnectionFromPool
from game_utils import dupeBoard


class SaveStates:

    """
    Record the state of each turn in a database at the end of each game.
    Adjust the P-value of each state based on the outcome.
    """
    def __init__(self, first):
        self.statesBoard = []
        self.currentBoard = [' '] * 9
        self.table = 'ann_ttt'  # Name of database
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
            cursor.execute('SELECT * FROM {} WHERE savestate=%s'
                           .format(self.table), (gameState,))
            retrievedData = cursor.fetchone()  # fetchone is first row

            """
            retrievedData[0]: id
            retrievedData[1]: save state (specialized board list)
            retrievedData[2]: p-value of save state
            """
            if retrievedData:
                return [retrievedData[0], retrievedData[1], retrievedData[2]]

    def recordState(self, winnerCounter):
        # input number of total turns when a win occurs
        loserCounter = winnerCounter - 1

        retrieveWinState = self.retrieveState(self.statesBoard[winnerCounter])
        retrieveLossState = self.retrieveState(self.statesBoard[loserCounter])

        self.recordHelper(retrieveWinState, 1, winnerCounter)
        self.recordHelper(retrieveLossState, 0, loserCounter)

    def recordHelper(self, retrievedState, pValue, counter):
        """
        Iterates through each save state and records to database

        :param retrievedState: should be a a retrieved save state from database
        :param pValue: 0 for loser, 1 for winner
        :param counter:
            Winner Counter = # of total turns that passed
            Loser Counter = Winner Counter - 1
        :return: None
        """

        if not retrievedState:
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'INSERT INTO {} (savestate, pvalue) VALUES (%s, %s)'
                    .format(self.table),
                    (self.statesBoard[counter], pValue))
        else:
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute(
                    'UPDATE {} SET pvalue=%s WHERE savestate=%s'
                    .format(self.table),
                    (pValue, self.statesBoard[counter]))
        afterstate_pvalue = pValue
        counter = counter - 2

        # Reward states leading to winning state with small increase to P-value
        # Punish states leading to losing state with small decrease to P-value
        while counter >= 0:
            retrieved = self.retrieveState(self.statesBoard[counter])
            if retrieved:
                recorded_pvalue = retrieved[2]
                new_pvalue = recorded_pvalue + self.alpha * \
                    (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'UPDATE {} SET pvalue=%s WHERE savestate=%s'
                        .format(self.table),
                        (new_pvalue, self.statesBoard[counter]))
                afterstate_pvalue = new_pvalue
                counter -= 2
            else:
                recorded_pvalue = 0.5
                new_pvalue = recorded_pvalue + self.alpha * \
                    (afterstate_pvalue - recorded_pvalue)
                with CursorFromConnectionFromPool() as cursor:
                    cursor.execute(
                        'INSERT INTO {} (savestate, pvalue) VALUES (%s, %s)'
                        .format(self.table),
                        (self.statesBoard[counter], new_pvalue))
                afterstate_pvalue = new_pvalue
                counter -= 2

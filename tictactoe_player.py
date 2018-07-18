class Player:

    # class for creating players, self.letter must be set before playing
    def __init__(self, letter=None, controller='human'):
        self.letter = letter
        self.controller = controller
        self.wins = 0

    def setLetter(self, letter=None):
        if not letter:
            while not (letter == 'X' or letter == 'O'):
                print('Select X or O: ')
                letter = input().upper()

        if letter == 'X':
            self.letter = 'X'
        else:
            self.letter = 'O'

    def setController(self):
        print('Play vs. human, Bit, or Byte? (Bit = Scripted AI; '
              'Byte = Machine Learning AI (unbeatable)')
        selection = input().lower()

        if selection == 'bit':
            self.controller = 'bit'
        elif selection == 'byte':
            self.controller = 'byte'
        else:
            self.controller = 'human'

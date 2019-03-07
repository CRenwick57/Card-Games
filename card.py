class Card(object):

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        if self.suit in ['S','C']:
            self.colour = 'B'
        else:
            self.colour = 'R'

    def __str__(self):
        suitWords = {'S':'Spades','H':'Hearts','D':'Diamonds','C':'Clubs'}
        numWords = {
                1:'Ace',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'6',
                7:'7',
                8:'8',
                9:'9',
                10:'10',
                11:'Jack',
                12:'Queen',
                13:'King'
            }
        return numWords[self.number]+' of '+suitWords[self.suit]

    def shortPrint(self):
        return str(self.number)+self.suit

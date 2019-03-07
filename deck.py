from card import Card
from random import shuffle

class Deck(object):

    def __init__(self):
        self.deck = []
        for suit in ['S','H','D','C']:
            for number in range(1,14):
                self.deck.append(Card(number,suit))
        shuffle(self.deck)

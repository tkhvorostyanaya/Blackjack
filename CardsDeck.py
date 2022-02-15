import random
import CardClass


class Deck(object):
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [CardClass.Card(r, s) for r in ranks for s in suits]
        random.shuffle(self.cards)

    def getCard(self):
        return self.cards.pop()

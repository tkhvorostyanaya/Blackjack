class Card(object):
    def __init__(self, cardpoint, cardsuit):
        self.cardpoint = cardpoint
        self.cardsuit = cardsuit

    def getCardValue(self):
        if self.cardpoint in "TJQK":
            return 10
        else:
            return " A23456789".index(self.cardpoint)

    def getCardRank(self):
        return self.cardpoint

    def __str__(self):
        return str(self.cardpoint) + str(self.cardsuit)

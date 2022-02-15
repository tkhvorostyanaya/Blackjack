from abc import ABC, abstractmethod


class AbstractPlayer(ABC):

    cards = []

    @abstractmethod
    def __init__(self):
        pass

    def newGame(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getCardsValue(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.getCardValue()
            if card.getCardRank() == "A":
                aces += 1

        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "\n" + self.username + "\n"
        for card in self.cards:
            text += str(card) + " "
        text += "\n" + "Cards value: " + str(self.getCardsValue()) + "\n"
        return text


class Player(AbstractPlayer):
    def __init__(self, username):
        self.username = username
        self.countOfLoses = 0
        self.gamesPlayed = 0

    def showStat(self):
        return "\n" + self.username + " games played : " + str(self.gamesPlayed) + "\n" + "win : " + \
               str(self.gamesPlayed - self.countOfLoses) + "\n" + "lose : " + str(self.countOfLoses)


class Dealer(AbstractPlayer):
    def __init__(self):
        self.username = "CasinoDealer"

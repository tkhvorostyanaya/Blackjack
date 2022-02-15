import CardsDeck
import PlayerClass

player = PlayerClass.Player("Player1")
dealer = PlayerClass.Dealer()

while True:

    deck = CardsDeck.Deck()

    player.newGame()
    dealer.newGame()

    player.addCard(deck.getCard())
    player.addCard(deck.getCard())
    dealer.addCard(deck.getCard())

    print(player)
    print(dealer)

    gameIsInProcess = True

    print(player.username)

    while player.getCardsValue() < 21:
        userInput = input("Take another card? (Y/N) ")
        if userInput == "Y" or userInput == "y":
            newCard = deck.getCard()
            player.addCard(newCard)
            print(newCard)
            print("Score = " + str(player.getCardsValue()))

            if player.getCardsValue() > 21:
                print(player.username + " lose")
                player.countOfLoses += 1
                gameIsInProcess = False
        else:
            break

    if gameIsInProcess:

        print("")
        print(dealer.username)
        while dealer.getCardsValue() < 17:
            newCard = deck.getCard()
            dealer.addCard(newCard)
            print(newCard)
            print("Score = " + str(dealer.getCardsValue()))

            if dealer.getCardsValue() > 21:
                print(dealer.username + " lose")
                gameIsInProcess = False

    if gameIsInProcess:
        if player.getCardsValue() == dealer.getCardsValue():
            print("Tie. no one win or lose")
        elif player.getCardsValue() > dealer.getCardsValue():
            print(dealer.username + " lose")
        else:
            print(player.username + " lose")
            player.countOfLoses += 1

    player.gamesPlayed += 1
    print(player.showStat())

    userInput = input("\n" + "Play again? (Y/N) ")
    if userInput == "Y" or userInput == "y":
        continue
    else:
        break

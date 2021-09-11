import random

class Deck:
    def __init__(self):
        self.deck = []
        self.faces = {
            'A' : 1,
            'K' : 10,
            'Q' : 10,
            'J' : 10,
            '10': 10,
            '9' : 9,
            '8' : 8,
            '7' : 7,
            '6' : 6,
            '5' : 5,
            '4' : 4,
            '3' : 3,
            '2' : 2,
        }
        self.suits = ['SPADES','HEART','CLUBS','DIAMOND']

    def createDeck(self):
        for face in self.faces:
            for suit in self.suits:
                self.deck.append((suit,face))
            random.shuffle(self.deck) # shuffle the deck

class Game():
    def __init__(self):
        self.d = Deck()

    def getCard(self, deck):
        card = deck.pop()
        return card

    def getValue(self, card):
        cardValue = self.d.faces.get(card)
        return cardValue
    
    def hit(self, player,deck,cardList):
        card = self.getCard(deck)
        if player == 'dealer':
            print("The dealer got a card")
        else:
            print(f"{player} got the card: {card}")
        cardList[player].append(card)
        value = self.getValue(card[1]) # Because the card is in tuple form and I only want the face, which is in index 1
        return value #prints card and return card value

    def checkWinner (self,scoreSheet): #scoreSheet has to be a dict
        if len(scoreSheet) == 1:
            return f'the winner is {scoreSheet}'
        values = scoreSheet.values()
        for x in list(values):
            if x == 0:
                return False
        for x in scoreSheet:
            if max(list(values)) == min(list(values)):
                return "This round is a tie"
            if max(list(values)) == scoreSheet.get(x):
                return (f'{x} is the winner')
    
    def checkBust (self,scoreSheet, player): #returns a list name of busted player's name
        if scoreSheet.get(player) > 21:
            print(f'{player} is busted')
            return player
        return False

    def createPlayersScoreSheet(self):
        scoreSheet = {
            'dealer' : 0,
        }
        while True:
            ans = input("More players? (y/n)")
            if ans.lower() == 'n':
                break
            elif ans.lower() == 'y':
                name = input("Player name: ")
                scoreSheet[name] = 0
            else:
                print('Invalid Input')
        return scoreSheet
    
    def deletBustedPlayers(self, scoreSheet,bustedPlayer):#Receives a dict and a list, then delets every value of list in dict
        del scoreSheet[bustedPlayer]
        return scoreSheet
    
    def dealerHit(self, scoreSheet):
        if scoreSheet.get('dealer') == 0:
            return 'h'
        if scoreSheet.get('dealer') <= 11:
            return 'h'
        return 's'

    def showResult(self, scoreSheet, winner,cardList):
        for x in cardList:
            print(f'{x} got the cards: {cardList.get(x)}')
            print(f'{x} scored: {scoreSheet.get(x)}')
        print("----------------------")
        print(f"{winner}!")
        print("GAMEOVER")
    
    def createCardDict(self,scoreSheet):
        cardList = {}
        for x in scoreSheet:
            cardList[x] = []
        return cardList

    def mainGame (self):
        self.d.createDeck()
        scoreSheet = self.createPlayersScoreSheet()
        playerCardList = self.createCardDict(scoreSheet)
        while True:
            for player in scoreSheet:
                if scoreSheet.get(player) == 0:
                    while True:
                        if player == 'dealer':
                            ans = self.dealerHit(scoreSheet)
                        else:
                            ans = input(f"{player}'s turn hit or stand? (h/s): ")
                        if ans.lower() == 'h':
                            playerScore = self.hit(player,self.d.deck,playerCardList)
                            scoreSheet[player] += playerScore
                            if self.checkBust(scoreSheet,player):
                                self.deletBustedPlayers(scoreSheet, player)
                                break
                        if ans.lower() == 's':
                            if scoreSheet.get(player) == 0:
                                self.deletBustedPlayers(scoreSheet, player)
                            break
                    if player not in scoreSheet: #If someone is busted, breaks for loop and loop back to the while loop at the top
                        break
            winner = self.checkWinner(scoreSheet)
            if winner:
                self.showResult(scoreSheet, winner, playerCardList)
                return



if __name__ == '__main__':
    g = Game()
    g.mainGame()
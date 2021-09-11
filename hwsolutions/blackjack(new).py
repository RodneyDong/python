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
    
    def hit(self, player):
        self.d.createDeck()
        card = self.getCard(self.d.deck)
        print(f"{player} got the card: {card}")
        value = self.getValue(card[1]) # Because the card is in tuple form and I only want the face, which is in index 1
        return value #prints card and return card value

    def checkWinner (self,scoreSheet): #scoreSheet has to be a dict
        if len(scoreSheet) == 1:
            print(f'the winner is {scoreSheet}')
        values = scoreSheet.values()
        for x in list(values):
            if x == 0:
                return False
        for x in scoreSheet:
            if max(list(values)) == min(list(values)):
                return "This round is a tie"
            if max(list(values)) == scoreSheet.get(x):
                return (f'{x} is the winner')
    
    def checkBust (self,scoreSheet): #returns a list name of busted player's name
        bustedNameList = []
        values = scoreSheet.values()
        for x in scoreSheet:
            if scoreSheet.get(x) > 21:
                print(f'{x} is busted')
                bustedNameList.append(x)
        if bustedNameList == []: # If no busted players, return nothing
            bustedNameList = False
        return bustedNameList

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
    
    def deletBustedPlayers(self, scoreSheet,bustedNameList):#Receives a dict and a list, then delets every value of list in dict
        for x in bustedNameList:
            if x in scoreSheet:
                del scoreSheet[x]
        return scoreSheet
    
    def dealerHit(self, scoreSheet):
        if scoreSheet.get('dealer') == 0:
            return 'h'
        if scoreSheet.get('dealer') <= 11:
            return 'h'
        return 's'

    def mainGame (self):
        scoreSheet = self.createPlayersScoreSheet()
        while len(scoreSheet) > 0:
            for player in scoreSheet:
                roundCount = 0
                while True:
                    ans = input(f"{player}'s turn hit or stand? (h/s): ")
                    if ans.lower() == 'h':
                        roundCount += 1
                        playerScore = self.hit(player)
                        scoreSheet[player] += playerScore
                        if roundCount > 1:
                            bustedPlayerList = self.checkBust(scoreSheet)
                            if bustedPlayerList:
                                self.deletBustedPlayers(scoreSheet, bustedPlayerList)
                                break
                    if ans.lower() == 's':
                        break
                if bustedPlayerList:
                    break
            winner = self.checkWinner(scoreSheet)
            if winner:
                print(scoreSheet)
                print(winner)
                print("GAMEOVER")
                return



if __name__ == '__main__':
    g = Game()
    g.mainGame()
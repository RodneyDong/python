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

class Game(Deck):
    def __init__(self):
        self.d = Deck()
        self.scoreSheet = {}
        self.playerCardList = {}

    def getCard(self, deck):
        card = deck.pop()
        return card

    def getValue(self, card):
        cardValue = self.d.faces.get(card)
        return cardValue
    
    def hit(self, player):
        card = self.getCard(self.d.deck)
        if player == 'dealer':
            print("The dealer got a card")
        else:
            print(f"{player} got the card: {card}")
        self.playerCardList[player].append(card)
        value = self.getValue(card[1]) # Because the card is in tuple form and I only want the face, which is in index 1
        return value #prints card and return card value

    def checkWinner (self): #scoreSheet has to be a dict
        if len(self.scoreSheet) == 1:
            return f'the winner is {self.scoreSheet}'
        values = self.scoreSheet.values()
        for x in list(values):
            if x == 0:
                return False
        for x in self.scoreSheet:
            if max(list(values)) == min(list(values)):
                return "This round is a tie"
            if max(list(values)) == self.scoreSheet.get(x):
                return (f'{x} is the winner')
    
    def checkBust (self, player): #returns a list name of busted player's name
        if self.scoreSheet.get(player) > 21:
            print(f'{player} is busted')
            return player
        return False

    def createPlayersScoreSheet(self):
        self.scoreSheet['dealer'] = 0
        while True:
            ans = input("More players? (y/n)")
            if ans.lower() == 'n':
                break
            elif ans.lower() == 'y':
                name = input("Player name: ")
                self.scoreSheet[name] = 0
            else:
                print('Invalid Input')
    
    def deletBustedPlayers(self, bustedPlayer):#Receives a dict and a list, then delets every value of list in dict
        del self.scoreSheet[bustedPlayer]
        del self.playerCardList[bustedPlayer]
        return self.scoreSheet
    
    def dealerHit(self):
        if self.scoreSheet.get('dealer') == 0:
            return 'h'
        if self.scoreSheet.get('dealer') <= 11:
            return 'h'
        return 's'

    def showResult(self, winner):
        for x in self.playerCardList:
            print(f'{x} got the cards: {self.playerCardList.get(x)}')
            print(f'{x} scored: {self.scoreSheet.get(x)}')
        print("----------------------")
        print(f"{winner}!")
        print("GAMEOVER")
    
    def createCardDict(self):
        for x in self.scoreSheet:
            self.playerCardList[x] = []
    
    def setup(self):
        self.d.createDeck()
        self.createPlayersScoreSheet()
        self.createCardDict()
    
    def game(self, player):
        if self.scoreSheet.get(player) == 0:
            while True:
                if player == 'dealer':
                    ans = self.dealerHit()
                else:
                    ans = input(f"{player}'s turn hit or stand? (h/s): ")
                    self.game(ans)
                if ans.lower() == 'h':
                    playerScore = self.hit(player)
                    self.scoreSheet[player] += playerScore
                    if self.checkBust(player):
                        self.deletBustedPlayers(player)
                        break
                if ans.lower() == 's':
                    if self.scoreSheet.get(player) == 0:
                        self.deletBustedPlayers(player)
                    break

    def mainGame (self):
        self.setup()
        while True:
            for player in self.scoreSheet:
                self.game(player)
                if player not in self.scoreSheet: #If someone is busted, breaks for loop and loop back to the while loop at the top
                    break
            winner = self.checkWinner()
            if winner:
                self.showResult(winner)
                return



if __name__ == '__main__':
    g = Game()
    g.mainGame()
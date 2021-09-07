"""
Reference website: https://www.dicegamedepot.com/yahtzee-rules/

Object of the Game:
The object of Yahtzee is for each player to roll dice and fill out 
their score card over the course of a series of rounds, trying to 
obtain the best rolls they can in 13 different combinations. 
The player with the highest score at the end of the game wins.
"""
import random

class Dices:
    def __init__(self, n=5): # where n is number of dices
        self.n = n
    
    def roll(self, n):
        dices = []
        for i in range(n):
            dices.append(random.randint(1,6))
        return dices

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dices = Dices()
        self.records = []
    
    def __repr__(self):
        return ": ".join((self.name, str(self.score)))

    def addScore(self):
        self.score += self.getScore()
    
    def roll(self, n=5):
        return self.dices.roll(n)

    def keep(self, keeps):
        for d in keeps:
            self.records.append(int(d))
        return self.roll(self.dices.n - len(self.records))

    def getScore(self):
        value = 0
        for i in range(len(self.records)):
            value += self.records[i]
        return value

    def addRecords(self, more):
        for d in more:
            self.records.append(int(d))

class Game:
    def __init__(self, rounds=1): # open for future change
        self.rounds = rounds
        self.playerList = []

    def addPlayer(self):
        while True:
            answer = input("More players? (y/n) ")
            if answer.lower() == 'n':
                break
            name = input("Please enter player: ")
            self.playerList.append(Player(name))

    def showResult(self):
        print("Ordered by score: ")
        ranks = sorted(self.playerList, key=lambda player: player.score, reverse=True)
        for player in ranks:
            print(player)

    def play(self):
        roundCount = 0
        while roundCount < self.rounds:
            for player in self.playerList:
                newRoll = player.roll()
                print(f"{player.name}: {newRoll}")
                round = 1
                while round<3:
                    answer = input(f"{player.name}, try again? (y/n) ")
                    if answer=='n':
                        break
                    answer = input("select dices to keep: for example> 6, 4: ")
                    keeps = answer.split(",")
                    newRoll = player.keep(keeps)
                    print(f"{player.name}: {newRoll}")                
                    round += 1
                player.addRecords(newRoll)
                player.addScore()
            roundCount += 1
        self.showResult()
        print("Game Over!")


if __name__ == '__main__':
    game = Game()
    game.addPlayer()
    game.play()
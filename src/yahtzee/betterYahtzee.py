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
        self.newDices = []
    
    def __repr__(self):
        return ": ".join((self.name, str(self.score)))

    def addScore(self):
        upperSectionScore = self.upperSection(self.records)
        lowerSectionScore = self.lowerSection(self.records)
        print(f"upper section score = {upperSectionScore}")
        print(f"lower section score = {lowerSectionScore}")
        ans = input("upper section (u) or lower section (l): ")
        if ans.lower() == 'u':
            self.score += upperSectionScore
        if ans.lower() == 'l':
            self.score += lowerSectionScore
        self.score += self.getScore()
    
    def roll(self, n=5):
        return self.dices.roll(n)

    def keep(self, keeps, keepDices):
        newValues = []
        for x in keeps:
            if x in keepDices:
                newValues.append(int(x))
        return newValues + self.roll(len(newValues)-len(keepDices))

    def getScore(self):
        value = 0
        for i in range(len(self.records)):
            value += self.records[i]
        return value

    def addRecords(self, more):
        for d in more:
            self.records.append(int(d))

    def upperSection(self,data):
        return sum(data)

    def lowerSection(self,data):
        if self.yahtzee(data):
            return 50
        if self.largeStraight(data):
            return 40
        if self.smallStraight(data):
            return 30
        if self.fullHouse(data):
            return 25
        return self.upperSection(data)

    def kind(self,data): # return the number of same kind values
        max = 0
        for i in range(len(data)):
            c = data.count(data[i])
            if c > max: max = c
        return max

    def fullHouse(self, data):
        return self.kind(data) == 3 and len(set(data)) == 2

    def smallStraight(self,data):
        s = set(data)
        list1=[{1,2,3,4},{2,3,4,5},{3,4,5,6},{1,3,4,5,6},{1,2,3,4,6}]
        return s in list1

    def largeStraight(self,data):
        s1,s2 = {1,2,3,4,5},{2,3,4,5,6}
        return set(data) in [s1,s2]

    def yahtzee(self,data):
        return len(set(data))==1



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
                    newRoll = player.keep(keeps, newRoll)
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
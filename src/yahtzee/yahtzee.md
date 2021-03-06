<h1>Yahtzee Game</h1>

[Yahtzee website](https://www.dicegamedepot.com/yahtzee-rules/)

## Object
The object of Yahtzee is for each player to roll dice and fill out their score card over the course of a series of rounds, trying to obtain the best rolls they can in 13 different combinations. The player with the highest score at the end of the game wins.

## Number of Players
2 or more

## How to PlayYahtzee
* Choose a starting player by player order
* player will take turns one at a time
* The game consists of thirteen rounds
* who has the greatest score wins.

```mermaid
graph TB
A(roll 5 dices)
B([loop for 2])
C{Try again?}
D[choose dices to keep<br>roll others]
E{Try Twice?}
F[score and end]

A-->B-->C
C--True-->D-->E
E--False-->B
E--True-->F
```
## class design
```mermaid
classDiagram

class Dice{
    number
    roll()
}
class Player{
    name:string
    roll()
    addScore()
    keep()
    getScore()
    addRecords()
}
class Game{
    playerList:list
    dices:Dice
    score()
}

Game *-- Player
Player *-- Dice
```

```mermaid
graph TB

A[lowerSection]
B{Yahtzee?}
C{Large Straight}
D{Small Straight}
E{Full House}
F{4 of a Kind}
G{3 of a Kind}
ADDUP[sum of all dices]
A -->B
B--False-->C
C--False-->D
D--False-->E
E--False-->F
F--False-->G
B--True-->50point
C--True-->40point
D--True-->30point
E--True-->25point
F--True-->ADDUP
G--True-->ADDUP

```
# Game of 21 or Black Jack
# Purpose: to set up a game that a player can play with the computer
# Author: Rodney Dong
# Date: April 16, 2021
# My planning:
# I will make two functions for the dealer and the player
# I will first write the program and then organize some codes into functions
print('''
    Welcome to the Game of 21
    —————————————————————————
    Rules:
    • Each player starts with two cards
    • The player asks for another card by saying ‘hit’.
    • If the player’s card total goes over 21, the game is over. The player ‘busts’.
    • The player stops asking for cards by saying ‘stand’.
    • The dealer (computer) will hit until its cards total 16 or better.
    • If the dealer ‘busts’ by going over 21 the player wins automatically.
    ''')
from colorama import Fore, Back, Style
import pcinput
import random
# Memory Requirement
spade = '\u2660'
club = '\u2663'
heart = '\u2665'
diamond = '\u2666'
suits = (Fore.BLACK + spade, Fore.RED + heart, Fore.BLACK + club, Fore.RED + diamond)
faces = ('A','K','Q','J','T','9','8','7','6','5','4','3','2')
deck = []
# input requirement (Everything input into the program)
for suit in suits:
    for face in faces:
        deck.append(Fore.BLACK + "[" + face + suit + Fore.BLACK + "]")

line = 0
for card in deck:
    print(card, end = " ")
    line += 1
    if line % 13 == 0:
        print()
print("----------------------------------------------------------------")
# process requirement (functions are all the process)
def pScore (cardOne, cardTwo):
    valueOne = cardOne [6]
    valueTwo = cardTwo [6]
    if valueOne.isnumeric():
        valueOne = int(valueOne)
    elif 'A'== valueOne:
        print("Your card values are: ",valueOne)
        print("Your card values are: ",valueTwo)
        restart = True
        valueOne = int(pcinput.getInteger("Do you want your Ace to be 1 or 11?"))
        while restart == True:
            if valueOne == 1:
                break
            if valueOne == 11:
                break
            if (valueOne != 1) and (valueOne != 11):
                print("The number for Ace needs to be 1 or 11")
                valueOne = int(pcinput.getInteger("Do you want your Ace to be 1 or 11?"))
                restart == True
    else:
        valueOne = 10
    
    if valueTwo.isnumeric():
        valueTwo = int(valueTwo)
    elif 'A'== valueTwo:
        print("Your card values are: ",valueOne)
        print("Your card values are: ",valueTwo)
        restart = True
        valueTwo = int(pcinput.getInteger("Do you want your Ace to be 1 or 11?"))
        while restart == True:
            if valueTwo == 1:
                break
            if valueTwo == 11:
                break
            if (valueTwo != 1) and (valueTwo != 11):
                print("The number for Ace needs to be 1 or 11")
                valueTwo = int(pcinput.getInteger("Do you want your Ace to be 1 or 11?"))
                restart = True
    else:
        valueTwo = 10
    return valueOne + valueTwo

def dScore (cardOne, cardTwo, dealersScore):
    valueOne = cardOne [6]
    valueTwo = cardTwo [6]
    if valueOne.isnumeric():
        valueOne = int(valueOne)
    elif 'A'== valueOne:
        if dealersScore > 10:
            valueOne = 1
        if dealersScore <= 10:
            valueOne = 11   
    else:
        valueOne = 10
    
    if valueTwo.isnumeric():
        valueTwo = int(valueTwo)
    elif 'A'== valueTwo:
        if dealersScore > 10:
            valueTwo = 1
        if dealersScore <= 10:
            valueTwo = 11  
    else:
        valueTwo = 10
    return valueOne + valueTwo
def playerHit (card):
    value = card [6]
    if value.isnumeric():
        value = int(value)
    elif 'A'== value:
        print("Your hit card is: ",value)
        restart = True
        value = int(pcinput.getInteger("Do you want your Ace to be 1 or 11?"))
        while restart == True:
            if value == 1:
                break
            if value == 11:
                break
            if value != 1 and value != 11:
                print("The number for Ace needs to be 1 or 11")
                value = int(pcinput.getInteger("Do you want your Ace to be 1 or 11?"))
                restart = True
    else:
        value = 10
    return value
def dealerHit (card, dealersScore):
    value = card [6]
    if value.isnumeric():
        value = int(value)
    elif 'A'== value:
        if dealersScore > 10:
            value = 1
        if dealersScore <= 10:
            value = 11
    else:
        value = 10
    return value
random.shuffle(deck)
game = True
playerCard1 = deck.pop()
playerCard2 = deck.pop()
dealerCard1 = deck.pop()
dealerCard2 = deck.pop()
dealerScore = dScore(dealerCard1, dealerCard2, 0)
playerScore = pScore(playerCard1, playerCard2)
# Output requirement (Everything output to the user like the print() function)
print ("You got the cards {} {} your (player) score is {}".format(playerCard1, playerCard2, playerScore))
print("The dealer(computer) has got its cards")
while game == True:
    answer = input("(h)it or (s)tand? ")
    while True:
        if answer.lower() == 'h':
            playerHitCard = deck.pop()
            playerHitValue = playerHit(playerHitCard)
            playerScore += playerHitValue
            print("Your hit card is", playerHitCard, "Your total score is", playerScore)
            break
        if answer.lower() == 's':
            break
        if answer.lower() != 'h' or answer.lower() != 's':
            print("Error: please enter (h)it or (s)tand")
            answer = input("(h)it or (s)tand? ")
        playerScore = playerScore
    if playerScore > 21:
        print("Oops, you have lost the game, because your score went over 21")
        break
    while True:
        if dealerScore < 16:
            print("The dealer chose hit")
            dealerHitCard = deck.pop()
            dealerHitValue = dealerHit(dealerHitCard, dealerScore)
            dealerScore += dealerHitValue
            print("The dealer got the cards: ", dealerCard1, dealerCard2, dealerHitCard)
            print("The dealer's total score is : ", dealerScore)
            break
        if dealerScore > 16:
            print("The dealer chose stand")
            break
        dealerScore = dealerScore
    if dealerScore > 21:
        print("You have won the game, the dealer score went over 21")
        break
    if (dealerScore > 16) and (answer.lower() == 's'):
        print("The dealer scored: ", dealerScore, "in total")
        print("You have scored: ", playerScore, 'in total')
        if dealerScore > playerScore:
            print("Oops, you have lost, the dealer have won you by", dealerScore - playerScore)
        if playerScore > dealerScore:
            print("Congragultions, you have won, you have won the dealer by", playerScore - dealerScore)
        if playerScore == dealerScore:
            print("This round is a tie")
        break
    game = True

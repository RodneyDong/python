import unittest
from src.yahtzee.betterYahtzee import *

class TestYahtzee(unittest.TestCase):
    def test_keep(self):
        player = Player("John")
        d1 = [2,3,4,2,5]
        keeps = ['5', '4'] # keep 2 dices
        newRoll=player.keep(keeps, d1)
        self.assertTrue(4 in newRoll)
        self.assertTrue(5 in newRoll)

        d1 = [4,5,6,6,6]
        keeps = ['4','5','6','6','6'] # keep all dices
        newRoll = player.keep(keeps, d1)
        self.assertEqual(d1, newRoll)

        d1 = [1,2,1,2,3]
        keeps = []
        newRoll = player.keep(keeps, d1)
        self.assertNotEqual(d1, newRoll)
        self.assertEqual(5, len(newRoll))

    def test_addScore(self):
        player = Player("John")
        d1 = [2,4,5,5,5]
        player.setRecords(d1)
        player.addScore(unit=True, ans='l')
        self.assertEquals(21, player.getScore())

        player.score = 0
        d1 = [2,2,5,5,5] # full house
        player.setRecords(d1)
        player.addScore(unit=True, ans='l')
        self.assertEquals(25, player.getScore())

        player.score = 0
        d1 = [2,2,5,5,5] # full house
        player.setRecords(d1)
        player.addScore(unit=True, ans='u')
        self.assertEquals(19, player.getScore())

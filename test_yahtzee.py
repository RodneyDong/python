import unittest
from betterYahtzee import *


class TestYahtzee(unittest.TestCase): # must inherits from unittest.TestCase
    def test_getScore(self):
        p = Player("Rodney")
        d1 = [1,2,3,4,5] #40
        d2 = [1,2,3,4,1] #30
        p.records = d1 
        self.assertEqual(15,p.getScore())
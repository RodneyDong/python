import unittest
from src.yahtzee.score import *

class TestScore(unittest.TestCase):
    def test_upperSection(self):
        data = [2,3,4,2,5]
        self.assertEqual(16,upperSection(data))
    
    def test_kind(self):
        data = [1,1,1,1,1]
        self.assertEqual(5,kind(data))
    
    def test_fullHouse(self):
        data = [2,2,3,3,3]
        self.assertTrue(fullHouse(data))        
        data = [2,2,3,3,1]
        self.assertFalse(fullHouse(data))
        data = [2,2,3,3,3]
        self.assertTrue(fullHouse(data))

    def test_smallStraight(self):
        data = [1,2,3,4,5]
        self.assertFalse(smallStraight(data)) 
        data = [1,2,3,4,2]
        self.assertTrue(smallStraight(data))       
        data = [1,3,4,2,1]
        self.assertTrue(smallStraight(data))
    
    def test_largeStraight(self):
        data = [1,2,3,4,5]
        self.assertTrue(largeStraight(data))  
        data = [2,3,4,5,6]
        self.assertTrue(largeStraight(data))
        data = [1,2,3,4,1]
        self.assertFalse(largeStraight(data))
    
    def test_yahtzee(self):
        data = [1,1,1,1,1]
        self.assertTrue(yahtzee(data))
        data = [1,1,1,1,2]
        self.assertFalse(yahtzee(data))
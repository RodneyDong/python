import unittest
from src.circle import circleArea
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(pi,circleArea(1))
        self.assertEqual(0,circleArea(0))
        self.assertEqual(16.619025137490002,circleArea(2.3))
    
    def test_negativeRadius(self):
        self.assertRaises(ValueError,circleArea,-2.0)
    
    def test_invalidDataType(self):
        self.assertRaises(TypeError,circleArea,-2.0+3j)
        self.assertRaises(TypeError,circleArea,'hello')
        self.assertRaises(TypeError,circleArea,True)
        


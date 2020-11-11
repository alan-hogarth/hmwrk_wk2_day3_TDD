import unittest
from src.TDD import *

class Test(unittest.TestCase):

    # def test_compare_3_1_returns_3_is_greater_than_1(self):
    #     self.assertEqual("3 is greater than 1", compare(3, 1))
    
    def test_compare_3_3_returns_3_is_equal_to_3(self):
        self.assertEqual('3 is equal to 3', compare(3, 3))

        
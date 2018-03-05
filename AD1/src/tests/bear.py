'''
Created on Mar 5, 2018

@author: Yuri Rodrigues
'''
import unittest
from simulation.animals import Bear

class BearTest(unittest.TestCase):


    def setUp(self):
        self.age = 3
        self.ageNotIncr = 10
        
        self.bear = Bear(self.age, "F")

    def tearDown(self):
        pass

    def testMaxAge(self):
        self.assertEqual(self.bear.maxAge(), 10)
    
    def testGetAge(self):
        self.assertEqual(self.bear.getAge(), self.age)
        
    def testIncrAge(self):
        self.assertTrue(self.bear.incrAge())
        
    def testRepr(self):
        self.assertEqual(repr(self.bear), "BF3")
    
    def testNotIncrAge(self):
        self.bear.age = self.ageNotIncr
        self.assertFalse(self.bear.incrAge())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
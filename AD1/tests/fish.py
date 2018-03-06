'''
Created on Mar 5, 2018

@author: Yuri Rodrigues
'''

import unittest
from animals import Fish


class FishTest(unittest.TestCase):
    def setUp(self):
        self.age = 2
        self.ageNotIncr = 4
        
        self.fish = Fish(self.age, "M")

    def tearDown(self):
        pass
    
    def testGetAge(self):
        self.assertEqual(self.fish.getAge(), self.age)
        
    def testIncrAge(self):
        self.assertTrue(self.fish.incrAge())
        
    def testRepr(self):
        self.assertEqual(repr(self.fish), "FM2")
    
    def testNotIncrAge(self):
        self.fish.age = self.ageNotIncr
        self.assertFalse(self.fish.incrAge())
    
    def testRandomCreationAge(self):
        fish = Fish()
        self.assertIn(fish.getAge(), range(5))
    
    def testRandomCreationGender(self):
        fish = Fish()
        self.assertIn(fish.gender, ["M", "F"])

if __name__ == "__main__":
    unittest.main()
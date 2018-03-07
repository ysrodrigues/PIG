'''
Created on Mar 6, 2018

@author: Yuri Rodrigues
'''

import unittest
from environment import River
import animals

class RiverTest(unittest.TestCase):
    def setUp(self):
        self.length = 4
        
        self.river = River(self.length)

    def tearDown(self):
        pass
    
    def testAddRandom(self):
        fish = animals.Fish()
        self.river.cells = [animals.Bear(), animals.Bear(), None, animals.Fish()]
        self.river.addRandom(fish)
        self.assertIsInstance(self.river.cells[2], animals.Fish)
    
    def testNumEmpty(self):
        self.river.cells = [None, animals.Bear(), None, animals.Fish()]
        self.assertEqual(self.river.numEmpty(), 2)
        
        self.river.cells = [None, None, None, None]
        self.assertEqual(self.river.numEmpty(), 4)
        
        self.river.cells = [animals.Bear(), animals.Bear(), animals.Fish(), animals.Fish()]
        self.assertEqual(self.river.numEmpty(), 0)
    
    def testRepr(self):
        self.river.cells = [None, animals.Bear(0, "M"), None, animals.Fish(3, "F")]
        self.assertEqual(repr(self.river), "——— BM0 ——— FF3")
        

if __name__ == "__main__":
    unittest.main()
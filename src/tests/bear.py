'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''
import unittest
import simulation.animals as animal

class BearTest(unittest.TestCase):

    def setUp(self):
        self.bear = animal.Bear()


    def tearDown(self):
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
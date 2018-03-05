'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

from .animal import Animal

class Bear(Animal):
    '''
    classdocs
    '''
    
    def __init__(self, age = None, gender = None):
        '''
        Constructor
        '''
        super().__init__(age, gender)

    def maxAge(self):
        return 10
    
    def getStrength(self):
        if(self.getAge() == 9):
            return 0
        elif(self.getAge() == 0 or self.getAge() == 8):
            return 1
        elif(self.getAge() == 1 or self.getAge() == 7):
            return 2
        elif(self.getAge() == 2 or self.getAge() == 6):
            return 3
        elif(self.getAge() == 3 or self.getAge() == 5):
            return 4
        elif(self.getAge() == 4):
            return 5

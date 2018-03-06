'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

import random
from .animal import Animal

class Bear(Animal):
    '''
    Data modeling for bears
    
    @type MAX_AGE: int
    @param MAX_AGE: Integer for max age of bears
    '''
    
    __MAX_AGE = 9
    
    def __init__(self, age = None, gender = None):
        '''
        Constructor
        
        @type age: int
        @param age: Number between 0 and 9
        '''
        
        if age is None:
            age = random.randint(0, 9)
        
        if gender is None:
            gender = random.choice(["M", "F"])
        
        super().__init__(age, gender)
        
    def maxAge(self):
        return (self.age >= self.__MAX_AGE)
            
    def getStrength(self):
        '''
        Gets the power of bear according to its age
        
        @type strength: int
        @param strength: Number between 0 and 5
        @rtype int
        @return power of bear according to its age
        '''
        
        if(self.getAge() == 9):
            strength = 0
        elif(self.getAge() == 0 or self.getAge() == 8):
            strength = 1
        elif(self.getAge() == 1 or self.getAge() == 7):
            strength = 2
        elif(self.getAge() == 2 or self.getAge() == 6):
            strength = 3
        elif(self.getAge() == 3 or self.getAge() == 5):
            strength = 4
        elif(self.getAge() == 4):
            strength = 5
        
        return strength

'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

import random
from .animal import Animal

class Fish(Animal):
    '''
    Data modeling for fishes
    
    @type MAX_AGE: int
    @param MAX_AGE: Integer for maximum age of fishes
    '''
    
    __MAX_AGE = 4
    
    def __init__(self, age = None, gender = None):
        '''
        Constructor
        
        @type age: int
        @param age: Number between 0 and 4
        '''
        
        if age is None:
            age = random.randint(0, 4)
        
        if gender is None:
            gender = random.choice(["M", "F"])
        
        super().__init__(age, gender)
        
        
    def maxAge(self):
        return (self.age >= self.__MAX_AGE)

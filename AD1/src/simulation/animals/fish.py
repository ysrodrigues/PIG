'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''
from .animal import Animal

class Fish(Animal):
    '''
    classdocs
    '''
    
    def maxAge(self):
        return 4

    def __init__(self, age = None, gender = None):
        '''
        Constructor
        '''
        super().__init__(age, gender)
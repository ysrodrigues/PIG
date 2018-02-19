'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

class Animal(object):
    '''
    classdocs
    '''


    def __init__(self, age = None, gender = None):
        '''
        Constructor
        '''
        self.age = age
        self.gender = gender
        
    def __repr__(self, *args, **kwargs):
        return object.__repr__(self, *args, **kwargs)
        
    def getAge(self):
        return self.age
    
    def maxAge(self):
        return False
    
    def incrAge(self):
        if(self.age < self.maxAge()):
            self.age += 1
            return True
        else: return False
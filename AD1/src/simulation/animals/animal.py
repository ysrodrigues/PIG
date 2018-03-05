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
            
    def getAge(self):
        return self.age
        
    def incrAge(self):
        if(self.age < self.maxAge()):
            self.age += 1
            return True
        else: return False
    
    def maxAge(self):
        pass
    
    def __repr__(self):
        return self.__class__.__name__[:1] + self.gender + str(self.age)
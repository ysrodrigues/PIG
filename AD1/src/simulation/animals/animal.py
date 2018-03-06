'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

class Animal(object):
    '''
    Data modeling for general animals
    
    @type age: int
    @param age: Age of animal
    @type gender: str
    @param gender: F for female and M for Male       
    '''
    
    def __init__(self, age = None, gender = None):
        '''
        Create an animal of the specified age and gender.
        If no age and gender are passed, then create an animal
        of a random age and gender.
        '''
        
        self.age = age
        self.gender = gender
            
    def getAge(self):
        '''
        Get the age of animal.
        
        @rtype: int
        @return: returns a integer representation for the animal's age
        '''
        
        return self.age
        
    def incrAge(self):
        '''
        If the current age of the animal is less than the maximum
        for the species, increments the age of the animal by one
        and returns true. 
        Otherwise, it leaves the age as is and returns false.
        
        @rtype: bool
        @return: True if increments the age, otherwise False 
        '''
        
        if not (self.maxAge()):
            self.age += 1
            return True
        
        return False
    
    def maxAge(self):
        '''
        Returns true if the current age of the animal has reached
        the limit for the species.
        Otherwise, it returns false.
        
        @rtype bool
        @return True if the max age has reached, otherwise False
        '''
        pass
    
    def __repr__(self):
        '''
        Creates a string representation of a animal, with first letter
        of animal's type, its gender and its age         
        
        @rtype str
        @return First letter of class name + gender + age of the animal
        '''
        return self.__class__.__name__[:1] + self.gender + str(self.age)
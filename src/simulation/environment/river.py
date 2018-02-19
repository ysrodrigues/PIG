'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

class River(object):
    '''
    classdocs
    '''


    def __init__(self, params, seed = None):
        '''
        Constructor
        '''
    
    def __repr__(self, *args, **kwargs):
        return object.__repr__(self, *args, **kwargs)
    
    def addRandom(self, animal):
        '''
        Add an animal of age 0 of randomly chosen
        gender and of the same type as animal to a
        cell chosen uniformly at random from among
        the currently empty cells
        
        @type animal: Animal
        @param animal: Animal to include on river      
        @rtype: bool
        @return: True if add successfully the animal on the river, otherwise False
        '''
        
        if(self.numEmpty() > 0):
            return True
        
        return False
    
    def getLength(self):
        return self.length
    
    def numEmpty(self):
        return
    
    def setSeed(self, seed):
        self.seed = seed
    
    def updateCell(self, i):
        return
    
    def updateRive(self):
        return
    
    def write(self, outputFileName):
        return
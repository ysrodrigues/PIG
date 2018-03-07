'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

import random

class River(object):
    '''
     Data modeling for river
     
     @type length: int
     @param length: Length of the River
     @type seed: int
     @param seed: RNG used in updating the river
     @type cells: Array<Animals> 
     @param cells: Position of animals in the river
    '''

    def __init__(self, args, seed = None):
        '''
        Constructor
        
        @type args: str
        @param args: input file name. 
        @type args: int
        @param args: length of the river
        @type seed: int
        @param seed: rng seed to update river
        '''
        
        self.cells = []
        
        if seed is not None:
            self.setSeed(seed)
        
        if(isinstance(args, str)):
            try:
                file = open(args, "r")
                file.close()
            except IOError as err:
                print(err)
                
        elif(isinstance(args, int)):    
            self.length = args
    
    def __repr__(self):
        return repr(self.cells)[1:-1].replace(",", "").replace("None", "———")
    
    def addRandom(self, animal):
        '''
        Add an animal of age 0 of randomly chosen gender and of the same type 
        as animal to a cell chosen uniformly at random from among the currently 
        empty cells.
        
        @type animal: Animal
        @param animal: Animal to include on river      
        @rtype: bool
        @return: True if add successfully the animal on the river, otherwise False
        '''
        
        if(self.numEmpty() > 0):
            cell = random.choice([index for index in range(self.length) if self.cells[index] is None])
            self.cells[cell] = animal
            return True
        
        return False
    
    def getLength(self):
        '''
        Returns the length of the River
         
        @rtype: int
        @return: length of the River
        '''
        
        return self.length
    
    def numEmpty(self):
        '''
        Returns the number of empty (null) cells in the river.
        
        @rtype: int
        @return: empty cells in the river
        '''
        res = 0
        
        for cell in self.cells:
            if cell is None:
                res += 1
        
        return res
    
    def setSeed(self, seed):
        self.seed = seed
    
    def updateCell(self, i):
        return
    
    def updateRiver(self):
        return
    
    def write(self, outputFileName):
        try:
            file = open(outputFileName, "a+")
            file.write(self.cells)
            file.close()
        except IOError as err:
            print(err)
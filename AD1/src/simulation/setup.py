'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
'''

import environment

class RiverSimulation(object):
    '''
    classdocs
    '''
    
    __RANDOM = 1
    __FILE = 2
    __EXIT = 3

    def __init__(self):
        '''
        Constructor
        '''
        self.running = 0
        self.trial = 1
        
        self.resetCicles()
    
    def input(self):
        print("keys: 1 (random river) 2 (file input) 3 (exit)")
        while (self.running != self.__EXIT):
            self.running = int(input("Trial " + str(self.trial) + ": "))
            
            self.trial += 1
            
            if(self.running == 1):
                self.randomRiver()
                
            if(self.running == 2):
                self.fileInput()
    
    def randomRiver(self):
        print("Random River")
        cicles = 0
        
        length = int(input("Enter river length: "))
        
        while(cicles <= 0):
            cicles = int(input("Enter the number of cycles: "))
        
        river = environment.River(length)
        print("Initial river:")
        print(river)
        
        while(self.cicle <= cicles):
            river.updateRiver()
            print("After cycle " + str(self.cicle) + ":")
            print(river)
            self.cicle += 1
        
        river.updateRiver()
        print("Final river:")
        print(river)
        
        self.resetCicles()
    
    def fileInput(self):
        print("File Input")
    
    
    def resetCicles(self):
        self.cicle = 1
    
    def run(self):
        print("River Ecosystem Simulator")
        self.input()        
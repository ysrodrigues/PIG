#!/usr/bin/env python

'''
Created on Feb 11, 2018

@author: Yuri Rodrigues
@encoding: UTF-8
'''

import os
import simulation

def main():
    '''
    This is the main function to running 
    a test simulation from Bears and Fish 
    
    @type biosystem: Ecosystem
    @param biosystem: The ecosystem simulation
    @rtype: number
    @return: Exit code that means no error occurred.
    '''
    
    biosystem = simulation.Ecosystem()
    biosystem.run()
    
    return os.EX_OK

if __name__ == '__main__':
    import sys
    sys.exit(main())
"""
Author Name: Bailey Jannuzzi
Module: environment.py
Description:
"""

from spider import Spider
from bird import Bird
from typing import Tuple

class Environment():
    '''
    Contains game environment's background color, calls 3 different Spider classes, and calls a Bird class.. 
    Contains methods:
        update(): Updates environment features.
        render(): 
    '''
    #Constructor
    def __init__(self):
        self._check_interval = 0.5 #Check every 0.5 seconds
        self._last_check = pygame.time.get_ticks()
    #End of constructor
    
    #Methods
    def update(self):
        '''
        '''
        pass

"""
Author Name: Bailey Jannuzzi
Module: bird.py
Description: Describes the Concrete Bird child class. Inherits from Organism parent class.
"""

from organism import Organism
from typing import Tuple

class Bird(Organism):
    '''
    Concrete class, takes parameters for a bird's position, shape, and color. 
    Contains methods:
        move(): Concrete method that describes how a bird will move, based on user-input from touchpad/mouse.
        eat_spider(): Calls the spider.die() method when bird position is within a defined 
                      range of a spider, and user 'clicks' touchpad/mouse.
    '''
    #Constructor
    def __init__(self, position: Tuple[int, int], shape: str, color: Tuple[int, int, int]):
        super().__init__(self, position, shape, color)
    #End of constructor
    
    #Methods
    def move(self):
        '''
        '''
        pass
    
    def eat_spider(self):
        '''
        '''
        pass
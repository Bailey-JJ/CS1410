"""
Author Name: Bailey Jannuzzi
Module: spider.py
Description: Describes the Concrete Spider child class. Inherits from Organism parent class.
"""

from organism import Organism
from typing import Tuple

class Spider(Organism):
    '''
    Concrete class, takes parameters for a spider's position, shape, color, reaction speed, and movement speed. 
    Contains class attributes:
        starting_pop: int; Pre-defined number of spiders at start.
        current_pop: int; Updates based on the number of not eaten spiders, and 'reproduces' accordingly.
    Contains methods:
        move(): Concrete method that describes how a spider will move.
        reproduce(): Updates the current_pop based on the number of spiders not eaten.
        pop(): Getter and Setter for the spider population.
        evade(): Describes movement based on reaction speed; based on user touchpad input, spiders will move away from bird.
        die(): When bird 'eats' a spider, the spider will be removed from display.
    '''
    
    self._starting_pop = 5
    self._current_pop = 
    
    #Constructor
    def __init__(self, position: Tuple[int, int], shape: str, color: Tuple[int, int, int], reaction_speed: int, speed: int):
        super().__init__(self, position, shape, color)
        self._reaction_speed = reaction_speed
        self._speed = speed
    #End of constructor
    
    #Methods
    def move(self):
        '''
        '''
        pass
    
    def reproduce(self):
        '''
        '''
        pass
    
    def pop(self):
        '''
        '''
        pass
    
    def evade(self):
        '''
        '''
        pass
    
    def die(self):
        '''
        '''
        pass
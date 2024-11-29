"""
Author Name: Bailey Jannuzzi
Module: spider.py
Description: Describes the Concrete Spider child class. Inherits from Organism parent class.
"""

from organism import Organism
from typing import Tuple
import pygame

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
    
    starting_pop = 5
    current_pop = 0
    
    #Constructor
    def __init__(self, position: Tuple[int, int], color: pygame.Surface, reaction_speed: int, speed: int):
        super().__init__(position)
        self._reaction_speed = reaction_speed
        self._color = color
        self._speed = speed
        Spider.current_pop += 1
    #End of constructor
    
    #Methods
    def move(self):
        '''
        '''
        newx = self._position[0] + self._speed[0]
        newy = self._position[1] + self._speed[1]
        
        if newx < 50 or newx > 600 - self.color.get_width():
            self._speed = (-self._speed[0], self._speed[1])  
        else:
            self._position = (newx, self._position[1])

        if newy < 250 or newy > 550 - self.color.get_height():
            self._speed = (self._speed[0], -self._speed[1])  
        else:
            self._position = (self._position[0], newy)
        
    
    def alive(self, surface):
        surface.blit(self._color, self._position)
        
        
    def reproduce(self):
        '''
        '''
        Spider.current_pop += 1
    
    def pop(self):
        '''
        '''
        return Spider.current_pop
    
    def evade(self, bird_position):
        '''
        '''
        pass
    
    def die(self):
        '''
        '''
        Spider.current_pop -= 1
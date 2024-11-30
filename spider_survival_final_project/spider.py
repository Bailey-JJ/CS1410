"""
Author Name: Bailey Jannuzzi
Module: spider.py
Description: Describes the Concrete Spider child class. Inherits from Organism parent class.
"""

from organism import Organism
from typing import Tuple
import pygame
import random

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
        self._direction = (random.choice([-1, 1]), random.choice([-1, 1]))
        Spider.current_pop += 1
    #End of constructor
    
    #Methods
    def move(self):
        '''
        '''
        dx, dy = self._direction
        x = self._position[0] + dx * self._speed
        y = self._position[1] + dy * self._speed
        
        if x < 50 or x > 550:
            dx *= -1

        if y < 250 or y > 550:
            dy *= -1
            
        self._direction = (dx, dy)
        self._position = (x, y)
        
    
    def alive(self, surface):
        surface.blit(self._color, self._position)
        
        
    def reproduce(self):
        '''
        '''
        Spider.current_pop += 1
    
    def get_position(self):
        '''
        '''
        width = self._color.get_width()
        height = self._color.get_height()
        
        x = self._position[0] + width // 2
        y = self._position[1] + height // 2

        return x, y
    
    def evade(self, bird_position):
        '''
        '''
        pass
    
    def die(self):
        '''
        '''
        Spider.current_pop -= 1
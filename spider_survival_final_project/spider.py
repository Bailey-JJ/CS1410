"""
Author Name: Bailey Jannuzzi
Module: spider.py
Description: Describes the Concrete Spider child class. Inherits from Organism parent class.
"""

from organism import Organism
from typing import Tuple
import pygame
import random
import math

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
    
    #Constructor
    def __init__(self, position: Tuple[int, int], shape: pygame.Surface, color: str, speed: int):
        super().__init__(position, shape)
        self._reaction_speed = speed * 2
        self._color = color
        self._speed = speed
        self._direction = (random.choice([-1, 1]), random.choice([-1, 1]))
    #End of constructor
    
    #Methods
    def move(self, bird_position):
        '''
        '''
        spider_x, spider_y = self._position
        
        if bird_position:
            bird_x, bird_y = bird_position
            # Calculate distance to the bird
            distance_to_bird = math.sqrt((spider_x - bird_x)**2 + (spider_y - bird_y)**2)
    
            if distance_to_bird <= 15:
                # Evade logic: move away from the bird
                dx = spider_x - bird_x
                dy = spider_y - bird_y
    
                # Normalize direction vector
                if distance_to_bird > 0:  # Avoid division by zero
                    dx /= distance_to_bird
                    dy /= distance_to_bird
    
                # Adjust position based on reaction speed
                newx = spider_x + dx * self._reaction_speed
                newy = spider_y + dy * self._reaction_speed
            else:
                # Normal movement logic if bird is not close
                dx, dy = self._direction
                newx = spider_x + dx * self._speed
                newy = spider_y + dy * self._speed  
    
        if newx < 50:
            newx = 550
        elif newx > 550:
            newx = 50
    
        if newy < 250:
            newy = 645
        elif newy > 645:
            newy = 250
    
        # Update position and rect
        self._position = (newx, newy)
        
        
    
    def alive(self, surface):
        surface.blit(self._shape, self._position)
        
        
    def get_position(self):
        '''
        '''
        width = self._shape.get_width()
        height = self._shape.get_height()
        
        x = self._position[0] + width // 2
        y = self._position[1] + height // 2

        return x, y
    
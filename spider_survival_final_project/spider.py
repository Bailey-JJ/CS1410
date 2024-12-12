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
    Concrete class, takes parameters for a spider's position, shape, color, and movement speed.
    Contains methods:
        move()
        alive()
        get_position()
    '''
    #Constructor
    def __init__(self, position: Tuple[int, int], shape: pygame.Surface, color: str, speed = None):
        super().__init__(position, shape)
        self._color = color
        self._speed = speed
        self._reaction_speed = self._speed * 1.5
        self._direction = (random.choice([-1, 1]), random.choice([-1, 1]))
    #End of constructor
    
    #Methods
    def move(self, bird_position):
        '''
        Concrete method that describes how a spider will move, based randomly decided, with the ability to "evade" the bird using touchpad input.
        '''
        spider_x, spider_y = self._position
        
        if bird_position:
            bird_x, bird_y = bird_position
            distance_to_bird = math.sqrt((spider_x - bird_x)**2 + (spider_y - bird_y)**2)
    
            if distance_to_bird <= 70:
                dx = spider_x - bird_x
                dy = spider_y - bird_y
    
                if distance_to_bird > 0:
                    dx /= distance_to_bird
                    dy /= distance_to_bird
    
                newx = spider_x + dx * self._reaction_speed
                newy = spider_y + dy * self._reaction_speed
            else:
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
    
        self._position = (newx, newy)
        
    
    def alive(self, surface):
        '''
        Displays spider onto game screen.
        '''
        surface.blit(self._shape, self._position)
        
        
    def get_position(self):
        '''
        Concrete method that finds the center coordinates of a spider image, and returns those coordinates.
        '''
        width = self._shape.get_width()
        height = self._shape.get_height()
        
        x = self._position[0] + width // 2
        y = self._position[1] + height // 2

        return x, y
    
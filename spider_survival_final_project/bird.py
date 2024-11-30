"""
Author Name: Bailey Jannuzzi
Module: bird.py
Description: Describes the Concrete Bird child class. Inherits from Organism parent class.
"""

from organism import Organism
from typing import Tuple
import pygame

class Bird(Organism):
    '''
    Concrete class, takes parameters for a bird's position, shape, and color. 
    Contains methods:
        move(): Concrete method that describes how a bird will move, based on user-input from touchpad/mouse.
        eat_spider(): Calls the spider.die() method when bird position is within a defined 
                      range of a spider, and user 'clicks' touchpad/mouse.
    '''
    #Constructor
    def __init__(self, position = (60, 200), shape = pygame.image.load("transparent_bird_image.png")):
        super().__init__(position)
        self._shape = shape
    #End of constructor
    
    #Methods
    def move(self, screen):
        '''
        '''
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        bird_x = mouse_x - self._shape.get_width() // 2
        bird_y = mouse_y - self._shape.get_height() // 2
        
        self._position = (bird_x, bird_y)
        
        screen.blit(self._shape, self._position)


    def get_position(self):
        '''
        '''
        width = self._shape.get_width()
        height = self._shape.get_height()
        
        x = self._position[0] + width // 2
        y = self._position[1] + height // 2

        return x, y
    

        
        
        
        
        
        
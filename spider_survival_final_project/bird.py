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
    Concrete class, takes parameters for a bird's position and shape. 
    Contains methods:
        move()
        get_position()
    '''
    #Constructor
    def __init__(self, position = None, shape = pygame.image.load("transparent_bird_image.png")):
        super().__init__(position, shape)
    #End of constructor
    
    #Methods
    def move(self, screen, mouse_position: Tuple[int, int]):
        '''
        Concrete method that describes how a bird will move, based on user-input from touchpad/mouse.
        Also displays bird image.
        '''
        mouse_x, mouse_y = mouse_position
        
        bird_x = mouse_x - self.shape.get_width() // 2
        bird_y = mouse_y - self.shape.get_height() // 2
        
        self._position = (bird_x, bird_y)
        
        screen.blit(self.shape, self._position)
    

        
        
        
        
        
        
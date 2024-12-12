"""
Author Name: Bailey Jannuzzi
Module: organism.py
Description: Describes the Abstract Organism parent class
"""

from abc import ABC, abstractmethod
from typing import Tuple

class Organism(ABC):
    '''
    Abstract class. Contains an organism's position, shape, and color. 
    Contains methods:
        move()
        shape()
        get_position()
    '''
    #Constructor
    def __init__(self, position: Tuple[int, int], shape):
        self._position = position
        self._shape = shape
    #End of constructor
    
    #Methods
    @abstractmethod
    def move(self):
        '''
        '''
        pass
    
    @property 
    def shape(self):
        return self._shape
    
    def get_position(self):
        '''
        Method that finds the center coordinates of an image, and returns those coordinates.
        '''
        width = self._shape.get_width()
        height = self._shape.get_height()
        
        x = self._position[0] + width // 2
        y = self._position[1] + height // 2

        return x, y

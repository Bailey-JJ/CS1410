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
    
    def get_position(self):
        '''
        '''
        pass

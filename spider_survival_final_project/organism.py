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
        move(): Abstract method that describes how an organism will move; either pre-determined or 
                by user control.
        display(): Sets an organism as a visible object to user.
    '''
    #Constructor
    def __init__(self, position: Tuple[int, int], shape: str, color: Tuple[int, int, int]):
        self._position = position
        self._shape = shape
        self._color = color
    #End of constructor
    
    #Methods
    @abstractmethod
    def move(self):
        '''
        '''
        pass
    
    def display(self):
        '''
        '''
        pass

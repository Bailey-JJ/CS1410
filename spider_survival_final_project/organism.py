"""
Author Name: Bailey Jannuzzi
Module: organism.py
Description: Describes the Abstract Organism parent class
"""

from abc import ABC, abstractmethod
from typing import Tuple
import pygame

class Organism(ABC):
    '''
    Abstract class. Contains an organism's position, shape, and color. 
    Contains methods:
        move(): Abstract method that describes how an organism will move; either pre-determined or 
                by user control.
        display(): Sets an organism as a visible object to user.
    '''
    #Constructor
    def __init__(self, position: Tuple[int, int]):
        self._position = position
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

"""
Author Name: Bailey Jannuzzi
Module: game_ui.py
Description: 
"""

import pygame
from environment import Environment
from typing import Tuple

class GameUI():
    '''
    Tracks the number of spiders eaten, the timer countdown, the final spider populations for each color,
    and calls the Environment Class. 
    Contains methods:
        update_time(): Updates the countdown timer and display it for the user.
        update_ui(): Updates environment of the game.
    '''
    #Constructor
    def __init__(self):
        self._environment = environment
        self._timer_limit = 60
        self._start_time = pygame.time.get_ticks()

    #End of constructor
    
    #Methods
    def update_time(self):
        '''
        '''
        pass
    
    def update_ui(self):
        '''
        '''
        pass

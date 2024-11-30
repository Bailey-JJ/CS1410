"""
Author Name: Bailey Jannuzzi
Module: environment.py
Description:
"""
import pygame
import random
from spider import Spider
from bird import Bird
from typing import Tuple
import math

class Environment():
    '''
    Contains game environment's background color, calls 3 different Spider classes, and calls a Bird class.. 
    Contains methods:
        update(): Updates environment features.
        render(): 
    '''
    #Constructor
    def __init__(self):
        self._check_interval = 0.5 #Check every 0.5 seconds
        self._last_check = pygame.time.get_ticks()
        self._spiders = []
        #self._bird = Bird()
        #self._population_counts = {}
        #self.initialize_population_counts()
    #End of constructor
    
    #Methods
    def initialize_population_counts(self):
        green = pygame.image.load("clear_green_spider_resized.png")
        red = pygame.image.load("clear_red_spider_resized.png")
        blue = pygame.image.load("clear_blue_spider_resized.png")
        

        # Create spiders for each color
        for _ in range(15):
            self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), red, 2, 1))
            self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), green, 2, 2))
            self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), blue, 2, 0.5))
 

    def remove_spiders(self, bird):
        '''
        Checks if the bird object is overlapping with the spider object, and returns a boolean.
        '''
        bird_rect = bird.get_position()
        
        for spider in self._spiders[:]:  
            spider_rect = spider.get_position()
            
            if abs(bird_rect[0] - spider_rect[0]) < 15 and abs(bird_rect[1] - spider_rect[1]) < 15:
                self._spiders.remove(spider)
        

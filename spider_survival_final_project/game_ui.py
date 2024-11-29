"""
Author Name: Bailey Jannuzzi
Module: game_ui.py
Description: 

    Possible changes: Create functions to create objects, to avoid repeating code? Need to use if statements and loops in code.
"""

import pygame
from environment import Environment
from spider import Spider
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
        #self._environment = environment
        self._timer_limit = 60
        self._start_time = pygame.time.get_ticks()

        
    #End of constructor
    
    #Methods
    def update_time(self):
        '''
        '''
        pass
    
    def setup_display(self):
        '''
        '''
        #Setting up the display objects
        pygame.display.set_caption("Spider Survival Game")
        
        screen = pygame.display.set_mode((900, 800))
        game_screen = pygame.Surface((550, 475))
        population_display = pygame.Surface((50, 50))
        
        return screen, game_screen, population_display
    
        
    def draw_ui(self, screen, game_screen):
        
        font = pygame.font.SysFont('consolas', 32)
        font2 = pygame.font.SysFont('consolas', 20)
        #font3 = pygame.font.SysFont('consolas', 10)
        
        screen.fill((255, 255, 255))  # Fill with white
        game_screen.fill((155, 191, 128)) #Fills with green
        
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(48, 248, 554, 479), 2)
        pygame.draw.circle(screen, (155, 191, 128), (70, 200), 25, 25)
        pygame.draw.circle(screen, (0, 0, 0), (70, 200), 25, 2)
        
        pygame.draw.circle(screen, (255, 105, 105), (140, 200), 25, 25)
        pygame.draw.circle(screen, (0, 0, 0), (140, 200), 25, 2)
        
        pygame.draw.circle(screen, (10, 168, 167), (210, 200), 25, 25)
        pygame.draw.circle(screen, (0, 0, 0), (210, 200), 25, 2)

        #Choosing Background Color
        pygame.draw.rect(screen, (155, 191, 128), pygame.Rect(30, 110, 220, 50), 25, 10, 10, 10, 10, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 110, 220, 50), 2, 10, 10, 10, 10, 10)
        
        #Spider Population Square
        pygame.draw.rect(screen, (155, 191, 128), pygame.Rect(625, 75, 250, 50), 25, 10, 10, 10, 10, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(625, 75, 250, 50), 2, 10, 10, 10, 10, 10)


        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(625, 140, 250, 200), 2) 
        
        #Spider Speed? Optional?
        pygame.draw.rect(screen, (155, 191, 128), pygame.Rect(625, 360, 250, 50), 25, 10, 10, 10, 10, 10) 
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(625, 360, 250, 50), 2, 10, 10, 10, 10, 10)

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(625, 425, 250, 200), 2)
            
        
        #Start Game Button
        pygame.draw.rect(screen, (10, 168, 167), pygame.Rect(625, 660, 250, 50), 25, 10, 10, 10, 10, 10) 
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(625, 660, 250, 50), 2, 10, 10, 10, 10, 10)
        
        
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Spider Survival', True, (0, 0, 0), (155, 191, 128))
        pop_text = font2.render('Spider Population', True, (0, 0, 0), (155, 191, 128))
        speed_text = font2.render('Spider Speed', True, (0, 0, 0), (155, 191, 128))
        bck_text = font2.render('Background Color', True, (0, 0, 0), (155, 191, 128))
    
    
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        pop_textRect = text.get_rect()
        speed_textRect = text.get_rect()
        bck_textRect = text.get_rect()
         
        # set the center of the rectangular object.
        textRect.center = (450, 40)
        pop_textRect.center = (790, 108)
        speed_textRect.center = (815, 392)
        bck_textRect.center = (190, 142)
        
        #speed_textRect.center = (750, 685)  #use for blue button
        
        
        screen.blit(game_screen, (50, 250))
        
        screen.blit(text, textRect)
        screen.blit(pop_text, pop_textRect)
        screen.blit(speed_text, speed_textRect)
        screen.blit(bck_text, bck_textRect)

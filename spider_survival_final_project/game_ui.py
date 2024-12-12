"""
Author Name: Bailey Jannuzzi
Module: game_ui.py
Description: 
"""

import pygame

class GameUI():
    '''
    Draws the basic layout pieces of the game.
    Contains methods:
        draw_ui()
    '''
    pygame.init()
    font = pygame.font.SysFont('consolas', 32)
    font2 = pygame.font.SysFont('consolas', 20)
    font3 = pygame.font.SysFont('consolas', 15)

    
    #Methods
    def draw_ui(self, screen, game_screen):
        '''
        Sets up the screen with the basic non-interactable elements.
        '''
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(48, 248, 554, 439), 2)


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
        
        
        #Game Title Display
        text = GameUI.font.render('Spider Survival', True, (0, 0, 0), (155, 191, 128))
        pop_text = GameUI.font2.render('Spider Population', True, (0, 0, 0), (155, 191, 128))
        speed_text = GameUI.font2.render('Spider Speed', True, (0, 0, 0), (155, 191, 128))
        bck_text = GameUI.font2.render('Background Color', True, (0, 0, 0), (155, 191, 128))
    
    
        textRect = text.get_rect()
        pop_textRect = text.get_rect()
        speed_textRect = text.get_rect()
        bck_textRect = text.get_rect()
         
        
        textRect.center = (450, 40)
        pop_textRect.center = (790, 108)
        speed_textRect.center = (815, 392)
        bck_textRect.center = (190, 142)
        
        
        screen.blit(game_screen, (50, 250))
        screen.blit(text, textRect)
        screen.blit(pop_text, pop_textRect)
        screen.blit(speed_text, speed_textRect)
        screen.blit(bck_text, bck_textRect)

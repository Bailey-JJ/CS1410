"""
Author Name: Bailey Jannuzzi
Module: button.py
Description: Describes the Button class. Provides methods to let users click the screen and change game structure.
"""

from typing import Tuple
import pygame


class Button():
    '''
    '''
    
    def __init__(self, shape: str, color, circle_position: Tuple[int, int] = (0, 0), rect_position: Tuple[int, int, int, int] = (0, 0, 0, 0), radius = 0):
        self._shape = shape
        self._color = color
        self._radius = radius
        self._center = circle_position
        self._position = rect_position
        self._rect_fill = int(rect_position[3] / 2)
        self._rect = pygame.Rect(rect_position)
        
        
    def change_background_color(self, game_screen):
        game_screen.fill(self._color)
        
        
    def stop_start_game(self, game_is):
        if game_is == "running":
            return "paused"
        elif game_is != "running":
            return "running"
        return game_is
    
    
    def draw_square_button(self, screen, text, text_cord: Tuple[int, int]):
        font2 = pygame.font.SysFont('consolas', 20)
        
        pygame.draw.rect(screen, self._color, self._rect, self._rect_fill, 10, 10, 10, 10, 10) 
        pygame.draw.rect(screen, (0, 0, 0), self._rect, 2, 10, 10, 10, 10, 10)
        
        stop_game = font2.render(f"{text}", True, (0, 0, 0))
        stopRect = stop_game.get_rect()
        stopRect.center = (text_cord)
        
        screen.blit(stop_game, stopRect.center)
    
    
    def draw_circle_buttons(self, screen):
        pygame.draw.circle(screen, self._color, self._center, self._radius, self._radius)
        pygame.draw.circle(screen, (0, 0, 0), self._center, self._radius, 2)
    
    
    def check_click(self, mouse_position):
        
        if self._shape == 'rect':
            x, y, width, height = self._position
            if x <= mouse_position[0] <= x + width and y <= mouse_position[1] <= y + height:
                return True
        
        elif self._shape == 'circle':
            dist_squared = (mouse_position[0] - self._center[0])**2 + (mouse_position[1] - self._center[1])**2
            
            if dist_squared <= self._radius**2:
                return True
            
        return False
        
    
    def handle_event(self, event, game_screen, game_is):
        '''
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and self.check_click(event.pos):
            if self._shape == 'circle':
                self.change_background_color(game_screen)
            elif self._shape == 'rect':
                if game_is == "running":
                    return "paused"
                elif game_is == "paused":
                    return "running"
            elif self._shape == 'end' and self._rect.collidepoint(event.pos):
                if game_is == "stopped":
                    return "start over"
        return game_is
    
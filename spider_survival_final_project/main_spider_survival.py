"""
Author Name: Bailey Jannuzzi
Module: main_spider_survival.py
Description: Initializes Game UI and Environment, updates game, and then terminates game.

    Possible changes: Create functions to create objects, to avoid repeating code? Need to use if statements and loops in code
"""
import pygame
import random
from environment import Environment
from game_ui import GameUI
from spider import Spider
from bird import Bird

def main():
    pygame.init()
    
    bird = Bird()
    
    gameui = GameUI()
    
    screen, game_screen, population_display = gameui.setup_display()
    
    
    environment = Environment()
    environment.initialize_population_counts()
    
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        # Event handling, gets all events from the event queue
        clock.tick(50)
        
        for event in pygame.event.get():
            # Close the window when the user clicks the close button
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                environment.remove_spiders(bird)

        gameui.draw_ui(screen, game_screen)
            
        bird.move(screen)
        
        for spider in environment._spiders:
            spider.move()
            spider.alive(screen)

        
        
        pygame.display.flip()
            
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
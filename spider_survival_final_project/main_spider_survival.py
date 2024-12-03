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
from button import Button

def game_loop():
    '''
    Contains all game logic, so that main() can run the game on loop.
    '''
    
    bird = Bird()
    gameui = GameUI()
    environment = Environment()
    
    pygame.display.set_caption("Spider Survival Game")
    screen = pygame.display.set_mode((900, 700))
    game_screen = pygame.Surface((550, 435))
    game_screen.fill((155, 191, 128)) 
    environment.initialize_population_counts()

    
    clock = pygame.time.Clock()
    timer = 5
    paused_start = None
    paused_time = 0
    start_time = pygame.time.get_ticks()
    last_repop_time = pygame.time.get_ticks()
    repop_every = 5000
    
    
    buttons = [
        Button('circle', (155, 191, 128), (70, 200), radius = 25),
        Button('circle', (223, 71, 61), (140, 200), radius = 25),
        Button('circle', (10, 158, 157), (210, 200), radius = 25),
        Button('rect', (10, 158, 157), rect_position = (625, 640, 250, 50)),
        Button('end', (10, 158, 157), rect_position = (320, 480, 250, 50))
        ]
    
    

    # Main loop
    game_is = "running"
    running = True
    while running:
        # Event handling, gets all events from the event queue
        elapsed_seconds = (pygame.time.get_ticks() - (start_time + paused_time)) // 1000
        time_left = max(timer - elapsed_seconds, 0)
                
                
        for event in pygame.event.get():
            # Close the window when the user clicks the close button
            
            if game_is == "start over":
                return "start over"
            
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                environment.remove_spiders(bird)
                
                for button in buttons:
                    if button._shape == 'circle':
                        button.handle_event(event, game_screen, game_is)
                    elif button._shape == 'rect':
                        game_is = button.handle_event(event, screen, game_is)


        if game_is == "stopped":
            environment.display_game_over(screen)
            buttons[4].draw_square_button(screen, "Start Over", (390, 495))
            
            

        if game_is == "paused":
            bird_position = pygame.mouse.get_pos()
            gameui.draw_ui(screen, game_screen)
            
            if paused_start is None:  
                paused_start = pygame.time.get_ticks()
                
            for button in buttons:
                if button._shape == 'circle':
                    button.draw_circle_buttons(screen)
                elif button._shape == 'rect':
                    button.draw_square_button(screen, 'Play Game', (700, 655))
                    
                        
        if game_is == "running":
            if paused_start is not None:  
                paused_time += pygame.time.get_ticks() - paused_start
                paused_start = None
            
            bird_position = pygame.mouse.get_pos() 
            current_time = pygame.time.get_ticks()
            
            if current_time - last_repop_time >= repop_every and len(environment._spiders) < 30:
                environment.repopulate()
                last_repop_time = current_time
            
            gameui.draw_ui(screen, game_screen)
            environment.display_current_stats(screen)
            bird.move(screen, bird_position)
            
                
            for spider in environment._spiders:
                spider.move(bird_position)
                spider.alive(screen)
            timer_text = gameui.font3.render(f"Time Remaining: {time_left}s", True, (0, 0, 0))
            screen.blit(timer_text, (450, 230)) 
            
                            
            for button in buttons[:4]:
                if button._shape == 'circle':
                    button.draw_circle_buttons(screen)
                else:
                    button.draw_square_button(screen, 'Pause Game', (700, 655))
                  

        if time_left == 0 and game_is == "running":
            game_is = "stopped"
                
        pygame.display.flip()
        clock.tick(60)
    
    # Quit Pygame
    pygame.quit()
    return "quit"

def main():
    pygame.init()

    while True:
        start_game = game_loop()
        if start_game == "quit":
            break
        elif start_game == "start over":
            continue
    pygame.quit()

if __name__ == "__main__":
    main()
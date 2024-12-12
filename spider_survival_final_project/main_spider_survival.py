"""
Author Name: Bailey Jannuzzi
Module: main_spider_survival.py
Description: Initializes Game UI and Environment, updates game, and then terminates game.
"""
import pygame
from typing import Tuple
from environment import Environment
from game_ui import GameUI
from bird import Bird
from button import Button


def game_start(screen, gameui, environment, game_screen, buttons, game_is, running):
    begin_font = pygame.font.SysFont('consolas', 20)
    gameui.draw_ui(screen, game_screen)
    environment.display_current_stats(screen)
    
    while True:
        gameui.draw_ui(screen, game_screen)
        draw_buttons(buttons[:3], screen)
        
        instructions_text = begin_font.render("Select a background color then,", True, (0, 0, 0))
        instructions_text2 = begin_font.render("press SPACE to start", True, (0, 0, 0))
        instructions_rect = instructions_text.get_rect(center=(325, 425))
        instructions_rect2 = instructions_text2.get_rect(center=(325, 450))
        screen.blit(instructions_text, instructions_rect)
        screen.blit(instructions_text2, instructions_rect2)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.shape == 'circle':
                        button.handle_event(event, game_screen, game_is)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "running", True
    return game_is, True


def initialize():
    '''
    Initializes the game environment upon start/restart of the game.
    '''
    bird = Bird()
    gameui = GameUI()
    environment = Environment()
    
    pygame.display.set_caption("Spider Survival Game")
    screen = pygame.display.set_mode((900, 700))
    screen.fill((255, 255, 255))
    pygame.display.update()
    game_screen = pygame.Surface((550, 435))
    game_screen.fill((155, 191, 128)) 
    environment.initialize_population_counts()
    
    
    buttons = [
        Button('circle', (155, 191, 128), (70, 200), radius = 25),
        Button('circle', (223, 71, 61), (140, 200), radius = 25),
        Button('circle', (10, 158, 157), (210, 200), radius = 25),
        Button('rect', (10, 158, 157), rect_position = (625, 540, 250, 50)),
        Button('end', (10, 158, 157), rect_position = (320, 480, 250, 50))
        ]
    
    clock = pygame.time.Clock()
    timer = 1
    paused_start = None
    paused_time = 0
    repop_every = 5000
    
    
    return bird, gameui, environment, screen, game_screen, buttons, clock, timer, paused_start, paused_time, repop_every


def draw_buttons(button_list, screen, text: str = None, coord: Tuple[int, int] = None):
    '''
    Draws buttons, based on their type.
    '''
    for button in button_list:
        if button.shape == 'circle':
            button.draw_circle_buttons(screen)
        elif button.shape == 'rect':
            button.draw_square_button(screen, text, coord)


def game_loop():
    '''
    Contains all game logic, so that main() can run the game on loop.
    ''' 

    bird, gameui, environment, screen, game_screen, buttons, clock, timer, paused_start, paused_time, repop_every = initialize()

    game_is = "not started"
    running = False
    
    # Main loop
    game_is, running = game_start(screen, gameui, environment, game_screen, buttons, game_is, running)
    
    start_time = pygame.time.get_ticks()
    last_repop_time = pygame.time.get_ticks()
    
    while running:
        elapsed_seconds = (pygame.time.get_ticks() - (start_time + paused_time)) // 1000
        time_left = max(timer - elapsed_seconds, 0)
                
        for event in pygame.event.get():
                            
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                environment.remove_spiders(bird)
                
                for button in buttons:
                    if button.shape == 'end' and game_is == "stopped":
                        game_is = button.handle_event(event, game_screen, game_is)
                    elif button.shape == 'circle':
                        button.handle_event(event, game_screen, game_is)
                    elif button.shape == 'rect':
                        game_is = button.handle_event(event, screen, game_is)
                
        #Actual playing game
        if game_is == "running":
                    
            bird_position = pygame.mouse.get_pos()

            current_time = pygame.time.get_ticks()
            
            if current_time - last_repop_time >= repop_every and len(environment.spiders) < 30:
                environment.repopulate()
                last_repop_time = current_time
                
            if paused_start is not None:  
                paused_time += pygame.time.get_ticks() - paused_start
                paused_start = None
            
            
            gameui.draw_ui(screen, game_screen)
            environment.display_current_stats(screen)
            bird.move(screen, bird_position)
            
                
            for spider in environment.spiders:
                spider.move(bird_position)
                spider.alive(screen)
            timer_text = gameui.font3.render(f"Time Remaining: {time_left}s", True, (0, 0, 0))
            screen.blit(timer_text, (450, 230)) 
            
            draw_buttons(buttons[:4], screen, 'Pause Game', (700, 555))
            
            
        #Pausing the game
        if game_is == "paused":
            bird_position = pygame.mouse.get_pos()
            gameui.draw_ui(screen, game_screen)
            
            if paused_start is None:  
                paused_start = pygame.time.get_ticks()
                
            draw_buttons(buttons, screen, 'Play Game', (700, 555))
          
            
        #Game Over screen    
        if time_left == 0 and game_is == "running":
            game_is = "stopped"
            
        if game_is == "stopped":
            environment.display_game_over(screen)
            buttons[4].draw_square_button(screen, "Start Over", (390, 495))
            
        if game_is == "start over":
            screen.fill((255, 255, 255))
            pygame.display.update()
            bird, gameui, environment, screen, game_screen, buttons, clock, timer, paused_start, paused_time, repop_every = initialize()
            
            game_is, running = game_start(screen, gameui, environment, game_screen, buttons, game_is, running)
            
            start_time = pygame.time.get_ticks()
            last_repop_time = pygame.time.get_ticks()
            
            
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
    #start_game()
    main()
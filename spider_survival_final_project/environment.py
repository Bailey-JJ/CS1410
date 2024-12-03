"""
Author Name: Bailey Jannuzzi
Module: environment.py
Description:
"""
import pygame
import random
from spider import Spider

class Environment():
    '''
    Contains game environment's background color, calls 3 different Spider classes, and calls a Bird class.. 
    Contains methods:
        update(): Updates environment features.
        render(): 
    '''
    
    #Constructor
    def __init__(self):
        self._check_interval = 5 
        self._last_check = pygame.time.get_ticks()
        self._spiders = []
        self._dead_spiders = []
        self.dead_spiders_count = {'red': 0,
                             'green': 0,
                             'blue': 0,}
        self.population_counts = {'red': 0,
                                  'green': 0,
                                  'blue': 0,}
        
    
    #End of constructor
    
    #Methods
    def initialize_population_counts(self):
        green = pygame.image.load("clear_green_spider_resized.png")
        red = pygame.image.load("clear_red_spider_resized.png")
        blue = pygame.image.load("clear_blue_spider_resized.png")
        

        # Create spiders for each color
        for _ in range(5):
            self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), red, 'red', 1))
            self.population_counts['red'] += 1
            self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), green, 'green', 1.5))
            self.population_counts['green'] += 1
            self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), blue, 'blue', 0.5))
            self.population_counts['blue'] += 1
 

    def remove_spiders(self, bird):
        '''
        Checks if the bird object is overlapping with the spider object, and returns a boolean.
        '''
        bird_rect = bird.get_position()
        
        for spider in self._spiders[:]:  
            spider_rect = spider.get_position()
            
            if abs(bird_rect[0] - spider_rect[0]) < 20 and abs(bird_rect[1] - spider_rect[1]) < 20:
                if spider._color == 'red':
                    self.population_counts['red'] -= 1
                    self.dead_spiders_count['red'] += 1
                    print('removed red')
                elif spider._color == 'green':
                    self.population_counts['green'] -= 1
                    self.dead_spiders_count['green'] += 1
                    print('removed green')
                elif spider._color == 'blue':
                    self.population_counts['blue'] -= 1
                    self.dead_spiders_count['blue'] += 1
                    print('removed blue')
                    
                self._dead_spiders.append(spider)
                self._spiders.remove(spider)
                
                
    def repopulate(self):
        '''
        Takes the number of spiders per color. Divides them by 2, and create 1 new spider per "pair" of spiders.
        '''
        green = pygame.image.load("clear_green_spider_resized.png")
        red = pygame.image.load("clear_red_spider_resized.png")
        blue = pygame.image.load("clear_blue_spider_resized.png")
        
        for color, count in self.population_counts.items():
            if count > 0:
                new_spiders = 1 * (count // 2)
                for _ in range(new_spiders):
                    if color == 'red':
                        self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), red, 'red', 1))
                        self.population_counts['red'] += 1
                    elif color == 'green':
                        self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), green, 'green', 2))
                        self.population_counts['green'] += 1
                    else:
                        self._spiders.append(Spider((random.randint(80, 570), random.randint(280, 695)), blue, 'blue', 0.5))
                        self.population_counts['blue'] += 1
            else:
                return ''


    def display_game_over(self, screen):
        font = pygame.font.SysFont('consolas', 32)
        font2 = pygame.font.SysFont('consolas', 20)
        font3 = pygame.font.SysFont('consolas', 15)
        
        total_dead = len(self._dead_spiders)
        red_dead = self.dead_spiders_count['red']
        blue_dead = self.dead_spiders_count['blue']
        green_dead = self.dead_spiders_count['green']
        
        
        #Creating Game Over Square
        end_game = font.render("Game Over", True, (0, 0, 0))
        endRect = end_game.get_rect()
        endRect.center = (375, 240)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(225, 230, 450, 350), 175, 10, 10, 10, 10, 10)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(225, 230, 450, 350), 2, 10, 10, 10, 10, 10)
        screen.blit(end_game, endRect.center)

        #Displaying Game Stats overtop Game Over Square
        stats_text = font2.render(f"Total Spiders Eaten: {total_dead}", True, (0, 0, 0))
        screen.blit(stats_text, (320, 330)) 
        stats_text2 = font2.render(f"  Red Spiders Eaten: {red_dead}", True, (0, 0, 0))
        screen.blit(stats_text2, (320, 360)) 
        stats_text3 = font2.render(f"  Green Spiders Eaten: {green_dead}", True, (0, 0, 0))
        screen.blit(stats_text3, (320, 390)) 
        stats_text4 = font2.render(f"  Blue Spiders Eaten: {blue_dead}", True, (0, 0, 0))
        screen.blit(stats_text4, (320, 420)) 
        
    
    def display_current_stats(self, screen):
        font = pygame.font.SysFont('consolas', 32)
        font2 = pygame.font.SysFont('consolas', 20)
        font3 = pygame.font.SysFont('consolas', 15)
        
        red_alive = self.population_counts['red']
        blue_alive = self.population_counts['blue']
        green_alive = self.population_counts['green']
        
        pop_text = font2.render(f"Red Spiders: {red_alive}", True, (0, 0, 0))
        screen.blit(pop_text, (630, 180)) 
        pop_text2 = font2.render(f"Green Spiders: {green_alive}", True, (0, 0, 0))
        screen.blit(pop_text2, (630, 230)) 
        pop_text3 = font2.render(f"Blue Spiders: {blue_alive}", True, (0, 0, 0))
        screen.blit(pop_text3, (630, 280)) 
        
        
        
        
        
        

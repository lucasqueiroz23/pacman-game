import pygame, sys
from settings import *


pygame.init()
vector = pygame.math.Vector2

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'

    def run_game(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()

        pygame.quit()
        sys.exit()

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def intro_update(self):
        pass

    def intro_draw(self):
        self.screen.fill((255, 255, 255))
        pygame.display.update()

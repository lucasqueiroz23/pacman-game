import pygame, sys
from settings import *


pygame.init()
vector = pygame.math.Vector2

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

    def run_game(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def draw_text(self, string, screen, text_position, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(string, False, colour)
        text_size = text.get_size()
        text_position[0] = text_position[0] - text_size[0]/2
        text_position[1] = text_position[1] - text_size[1]/2
        screen.blit(text, text_position)

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(COLOR_BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [SCREEN_WIDHT//2, SCREEN_HEIGHT//2], START_TEXT_SIZE, COLOR_ORANGE, START_FONT)
        pygame.display.update()
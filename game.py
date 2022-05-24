import pygame, sys
from settings import *
from player import *


pygame.init()
vector = pygame.math.Vector2

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'menu'
        self.cell_width = MAZE_WIDHT//28
        self.cell_height = MAZE_HEIGHT//30
        self.player = Player(self, PLAYER_START_POSITION)

        self.load()

    def run_game(self):
        while self.running:
            if self.state == 'menu':
                self.menu_events()
                self.menu_update()
                self.menu_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False

            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def draw_text(self, string, screen, text_position, size, colour, font_name,isCentered = False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(string, False, colour)
        text_size = text.get_size()
        if isCentered:
            text_position[0] = text_position[0] - text_size[0]/2
            text_position[1] = text_position[1] - text_size[1]/2

        screen.blit(text, text_position)

    def load(self):
        self.maze = pygame.image.load('images/maze.png')
        self.maze = pygame.transform.scale(self.maze, (MAZE_WIDHT, MAZE_HEIGHT))

    def draw_grid(self):
        for x in range(SCREEN_WIDHT//self.cell_width):
            pygame.draw.line(self.maze, COLOR_ORANGE, (x*self.cell_width, 0), (x*self.cell_width, SCREEN_HEIGHT))
        for x in range(SCREEN_HEIGHT//self.cell_height):
            pygame.draw.line(self.maze, COLOR_ORANGE, (0, x*self.cell_height), (SCREEN_WIDHT, x*self.cell_height))

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def menu_update(self):
        pass

    def menu_draw(self):
        self.screen.fill(COLOR_BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [SCREEN_WIDHT//2, SCREEN_HEIGHT//2], MENU_TEXT_SIZE+5, COLOR_ORANGE, MENU_FONT, True)
        self.draw_text('ONE PLAYER ONLY', self.screen, [SCREEN_WIDHT//2, SCREEN_HEIGHT//2 + 50], MENU_TEXT_SIZE, COLOR_BLUE, MENU_FONT,True)
        self.draw_text('HIGH SCORE: 0', self.screen, (29,0), 18, COLOR_WHITE, MENU_FONT)
        pygame.display.update()

######### jogo #########

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
    
    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.fill(COLOR_BLACK)
        self.screen.blit(self.maze, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        self.draw_grid()
        self.draw_text('HIGH SCORE: 0', self.screen, (29,0), 18, COLOR_WHITE, MENU_FONT)
        self.draw_text('SCORE: 0', self.screen, (SCREEN_WIDHT//2 + 29,0), 18, COLOR_WHITE, MENU_FONT)
        self.player.draw()
        pygame.display.update()

    
import pygame
from pygame.math import Vector2 as vec 

from settings import *

class Player:
    def __init__(self, game, position):
        self.game = game
        self.grid_position = position
        self.x_position = self.grid_position.x*self.game.cell_width+TOP_BOTTOM_BUFFER//2+self.game.cell_width//2
        self.y_position = self.grid_position.y*self.game.cell_height+TOP_BOTTOM_BUFFER//2+self.game.cell_height//2
        self.pix_position = vec(self.x_position, self.y_position)
        # print(self.grid_position, self.pix_position)

    def update(self):
        ...
    
    def draw(self):
        pygame.draw.circle(self.game.screen, COLOR_PLAYER, (int(self.pix_position.x), 
        int(self.pix_position.y)), self.game.cell_width//2 - 2)
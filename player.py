import pygame
from pygame.math import Vector2 as vec 

from settings import *

class Player:
    def __init__(self, game, position):
        self.game = game
        self.grid_position = position
        self.pix_position = self.get_pix_position()
        self.direction = vec(1,0)

    def update(self):
        self.pix_position += self.direction
        self.grid_position[0] = (self.pix_position[0] - TOP_BOTTOM_BUFFER + self.game.cell_width//2)//self.game.cell_width+1 
        self.grid_position[1] = (self.pix_position[1] - TOP_BOTTOM_BUFFER + self.game.cell_height//2)//self.game.cell_height+1 

    def draw(self):
        pygame.draw.circle(self.game.screen, COLOR_PLAYER, (int(self.pix_position.x), 
        int(self.pix_position.y)), self.game.cell_width//2 - 2)
        pygame.draw.rect(self.game.screen, COLOR_RED , (self.grid_position[0]*self.game.cell_width + TOP_BOTTOM_BUFFER//2,
         self.grid_position[1]*self.game.cell_height + TOP_BOTTOM_BUFFER//2, self.game.cell_width, self.game.cell_height), 1)


    def move(self,direction):
        self.direction = direction

    def get_pix_position(self):
        self.x_position = self.grid_position.x*self.game.cell_width+TOP_BOTTOM_BUFFER//2+self.game.cell_width//2
        self.y_position = self.grid_position.y*self.game.cell_height+TOP_BOTTOM_BUFFER//2+self.game.cell_height//2
        self.pix_position = vec(self.x_position, self.y_position)
        return self.pix_position
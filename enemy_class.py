import pygame
from settings import *

vec = pygame.math.Vector2

class Enemy:
    def __init__(self,app,pos,number):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()       # get each enemy position
        self.radius = self.app.cell_width//2  # set enemy size
        self.number = number
        self.colour = self.set_colour()




    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour, (int(self.pix_pos.x)
                                                          , int(self.pix_pos.y)), self.radius)

    def get_pix_pos(self):
        return vec((self.grid_pos.x * self.app.cell_width)+ (self.app.cell_width + TP_BUFFER)//2,
                   (self.grid_pos.y * self.app.cell_height) + (self.app.cell_height + TP_BUFFER)//2)
        #print(self.grid_pos, self.pix_pos) #    def update(self):

    def set_colour(self):
        if self.number == 0:
            return (43,70,200)
        if self.number == 1:
            return (200, 200, 30)
        if self.number == 2:
            return (190, 30, 30)
        if self.number == 3:
            return (200, 150, 30)
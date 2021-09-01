import pygame
from settings import *
vec = pygame.math.Vector2

class Player():
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos                       # the position based on the grid count
        self.pix_pos = self.get_pix_pos()         # use grid position, to gerate the current player position
        self.playerImg = pygame.image.load('sources/player.png')
        self.dirction = vec(1,0)
        self.stored_dirction = None
        print('dirction', self.dirction)


    def update(self):
        print('dirction', self.dirction)

        self.pix_pos += self.dirction # final step to move the player

        #
        # limit player movement within grid by using stored dirction vairbale
        #
        if self.time_to_move():                         #if the pix position is on right place to change dirction
            if self.stored_dirction != None:            # if the new direction is given by press the arrow key.
                self.dirction = self.stored_dirction    # new direction is equle to given direction

        # give pix position to a grid position
        self.grid_pos[0] = (self.pix_pos[0] - TP_BUFFER + self.app.cell_width//2)//self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TP_BUFFER + self.app.cell_height//2)//self.app.cell_height + 1

    def draw(self):
        pygame.draw.circle(self.app.screen, YELLOW, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)
        # draw the player based on the pix position

        ### draw the grid in red rect
        pygame.draw.rect(self.app.screen, RED,
                         (self.grid_pos[0]*self.app.cell_width + TP_BUFFER//2,
                          self.grid_pos[1]* self.app.cell_height + TP_BUFFER//2,
                          self.app.cell_width, self.app.cell_height), 1)

    def move(self, dirction):
        self.stored_dirction = dirction

    def get_pix_pos(self):
        return vec((self.grid_pos.x * self.app.cell_width)+ (self.app.cell_width + TP_BUFFER)//2,
                   (self.grid_pos.y * self.app.cell_height) + (self.app.cell_height + TP_BUFFER)//2)
        #print(self.grid_pos, self.pix_pos) #

    def time_to_move(self):
        if int(self.pix_pos.x + TP_BUFFER//2) % self.app.cell_width == 0:
            if self.dirction == vec(1,0) or self.dirction == vec(-1, 0):
                return True
        if int(self.pix_pos.y + TP_BUFFER//2) % self.app.cell_height == 0:
            if self.dirction == vec(0,1) or self.dirction == vec(0, -1):
                return True
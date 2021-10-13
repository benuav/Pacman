import pygame
from settings import *
vec = pygame.math.Vector2

class Player():
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos                       # the position based on the grid count
        self.pix_pos = self.get_pix_pos()         # use grid position, to gerate the current player position
        self.playerImg = pygame.image.load('sources/player.png')
        self.direction = vec(1,0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2 # speed is used to time the direction

    def update(self):

        if self.able_to_move:                # if the the forward direction is not wall, return True
            self.pix_pos += self.direction*self.speed   # final step to move the player

        #######################################################################
        # limit player movement within grid by using stored direction variable #
        #######################################################################
        if self.time_to_move():                           #if the pix position is on right place to change dirction
            if self.stored_direction != None:             # if the new direction is given by press the arrow key.
                self.direction = self.stored_direction    # new direction is equal to given direction

            self.able_to_move = self.can_move()           # change able to move state by can_move

        # give pix position to a grid position
        self.grid_pos[0] = (self.pix_pos[0] - TP_BUFFER + self.app.cell_width//2)//self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TP_BUFFER + self.app.cell_height//2)//self.app.cell_height + 1

        if self.on_coin():                           # if player meet coin, remove the coin
            self.eat_coin()


    def draw(self):        # draw the player based on the pix position
        pygame.draw.circle(self.app.screen, YELLOW, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2-2)

        #############################################################################
        ###                          draw the grid in red rect                      #
        #pygame.draw.rect(self.app.screen, RED,                                     #
        #                 (self.grid_pos[0]*self.app.cell_width + TP_BUFFER//2,     #
        #                  self.grid_pos[1]* self.app.cell_height + TP_BUFFER//2,   #
        #                  self.app.cell_width, self.app.cell_height), 1)           #
        #############################################################################

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x + TP_BUFFER // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + TP_BUFFER // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        else:
            return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1


    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos.x * self.app.cell_width)+ (self.app.cell_width + TP_BUFFER)//2,
                   (self.grid_pos.y * self.app.cell_height) + (self.app.cell_height + TP_BUFFER)//2)
        #print(self.grid_pos, self.pix_pos) #

    def time_to_move(self):
        if int(self.pix_pos.x + TP_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1,0) or self.direction == vec(-1, 0):
                return True
        if int(self.pix_pos.y + TP_BUFFER//2) % self.app.cell_height == 0:
            if self.direction == vec(0,1) or self.direction == vec(0, -1):
                return True

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos + self.direction) == wall: # the forward next step is equal to wall
                return False
        return True                                         # when the wall is not on the direction


    ''' time to move: when the new direction is gevin, can move function will return True, 
    then the able to move will change to True.'''
    #
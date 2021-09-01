import pygame, sys, copy
from settings import *
from player_class import *
#from enemy_class import *

pygame.init()             # initialize the pygame
vec = pygame.math.Vector2 # for velosity(speed), acceliration, position (x,y)



class App():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # set screen size
        self.clock = pygame.time.Clock()   # set the time
        self.running = True
        self.state = 'intro'               # set the init state as intro
        #self.background = pygame.image.load('sources/maze_2.png')
        self.cell_width = MAZE_WIDTH //28
        self.cell_height = MAZE_HEIGHT //30
        self.player = Player(self, PLAYER_START_POS)
        self.loadImage()


    def run(self):
        while self.running:
            if self.state == 'intro':      # display when state = intro
                self.intro_events()
                self.intro_update()
                self.intro_draw()   # draw things
            elif self.state == 'playing':
                self.playing_events()
                self.playing_draw()
                self.playing_update()
            else:
                self.running = False
            self.clock.tick(fps)           # control the loop speed

        pygame.quit()
        sys.exit()

##############################  help state   #######################################

    def draw_text(self, words, screen, size,colour,font_name,pos):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        pos[0] = (pos[0] - text_size[0]) // 2    # get floor recult of have text size
        pos[1] = (pos[1] - text_size[1]) // 2
        screen.blit(text, pos)                   # draw the thing

    def loadImage(self):
        self.background = pygame.image.load('sources/maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH,MAZE_HEIGHT)) # call the background, resize it


    def draw_grid(self):
        #self.load() # pass background to function
        for x in range (WIDTH//self.cell_width):
            pygame.draw.line(self.background, GRAY, (x * self.cell_width, 0), (x* self.cell_width, HEIGHT))
            # draw line on screen, not maze image
        for x in range (HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GRAY, (0, x * self.cell_height), (WIDTH, x * self.cell_height))


##############################  intro state   #######################################

    def intro_events(self):                 # function: quit program
        for event in pygame.event.get():    # access the list of event from pygame
            if event.type == pygame.QUIT:   # when press exit on the window
                self.running = False        # brake the while loop
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def intro_update(self):
        pass

    def intro_draw(self): # draw text at intro page
        self.screen.fill(BLACK)
        self.draw_text('START GAME - 448,596', self.screen, START_TEXT_SIZE, BLUE, START_FONT, [WIDTH,HEIGHT])
        self.draw_text('Sha Bai - 448,496', self.screen, START_TEXT_SIZE, RED, START_FONT, [WIDTH,HEIGHT+100])
        self.draw_text('Zhuoheng Li - 448,496', self.screen, START_TEXT_SIZE, RED, START_FONT, [WIDTH,HEIGHT+150])

        self.draw_text('HIGHEST SCORE - 0,0', self.screen, START_TEXT_SIZE, WHITE, START_FONT, [250,30])


        pygame.display.update()             # update the screen

##############################  playing state   #######################################

    def playing_events(self):                 # function: quit program
        for event in pygame.event.get():    # access the list of event from pygame
            if event.type == pygame.QUIT:   # when press exit on the window
                self.running = False        # brake the while loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                    print('move left')
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                    print('move right')
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0,1))
                if event.key == pygame.K_SPACE:
                    self.player.move(vec(0,0))




    def playing_update(self):

        self.player.update()

    def playing_draw(self):            # draw text at intro page
        self.screen.fill(BLACK)        # fill screen with black first, remove intro image
       # self.loadImage()                  # load resized image
        self.draw_grid()

        self.screen.blit(self.background,(TP_BUFFER//2, TP_BUFFER//2))



        self.draw_text( 'CURRENT SCORE: 0', self.screen, START_TEXT_SIZE, WHITE, START_FONT, [150,25])
        self.draw_text( 'HIGHEST SCORE: 0', self.screen, START_TEXT_SIZE, WHITE, START_FONT, [WIDTH,25])

        self.player.draw()

        pygame.display.update()        # update the screen


##############################  intro state   #######################################




from pygame.math import Vector2 as vec

#screen settings
WIDTH, HEIGHT = 610, 670
TP_BUFFER = 50

MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TP_BUFFER, HEIGHT - TP_BUFFER
LOGO_WIDTH, LOGO_HEIGHT = int(WIDTH * 0.8), int(HEIGHT * 0.2)
fps = 60

ROWS = 30
COLS = 28

#colour settings
BLUE = (30,130,160)
YELLOW = (170,130,60)
GRAY = (110,110,110)
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)

#font settings
YEAR_TEXT_SIZE = 24
NAME_TEXT_SIZE = 16
START_TEXT_SIZE = 30
SCORE_TEXT_SIZE = 16
START_FONT = 'arial black'

#player
#PLAYER_START_POS = 0


# bot settings

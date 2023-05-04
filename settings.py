# Code created by Landon Zafiropoulo
WIDTH = 500
HEIGHT = 500
# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 30
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
# Moving Platform
PLATFORM_LIST = [(10, HEIGHT - 40, WIDTH, 40, (200,200,200), "base"),
                 (1, HEIGHT - 20, WIDTH, 20, (250,250,200), "base"),
                 (5, HEIGHT - 10, WIDTH, 30, (300,200,200), "base"),]
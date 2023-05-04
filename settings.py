# FIle create by Landon Zafiropoulo

########## screen dimensions #############
WIDTH = 800
HEIGHT = 600

############# game settings ##############
FPS = 30
RUNNING = True
SCORE = 0
PAUSED = False

############ player attributes ###########
PLAYER_ACC  = 2
PLAYER_FRICTION = -0.12
MOB_FRICTION = -0.7
MOB_ACC= 0.7
PLAYER_GRAV = 1
PLAYER_JUMP = 20
################ colors ##################
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
PURPLE = (160,32,240)
########## Starting platforms ############
PLATFORM_LIST = [(30, 40, 170, 50, (255,50,50), "normal"),
                 (220, 40, 170, 50, (255,50,50), "normal"),
                 (410, 40, 170, 50, (255,50,50), "normal"),
                 (600, 40, 170, 50, (255,50,50), "normal"),
                 (30, 110, 170, 50, (50,50,255), "normal"),
                 (220, 110, 170, 50, (50,50,255), "normal"),
                 (410, 110, 170, 50, (50,50,255), "normal"),
                 (600, 110, 170, 50, (50,50,255), "normal"),
                 (30, 180, 170, 50, (160,32,240), "normal"),
                 (220, 180, 170, 50, (160,32,240), "normal"),
                 (410, 180, 170, 50, (160,32,240), "normal"),
                 (600, 180, 170, 50, (160,32,240), "normal"),
                 (30, 250, 170, 50, (20,20,20), "normal"),
                 (220, 250, 170, 50, (20,20,20), "normal"),
                 (410, 250, 170, 50, (20,20,20), "normal"),
                 (600, 250, 170, 50, (20,20,20), "normal"),]

# x, y, width, height

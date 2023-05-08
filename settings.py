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
PLAYER_JUMP = 30
################ colors ##################
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
PURPLE = (160,32,240)
########## Starting platforms ############
PLATFORM_LIST = [(30, 40, 170, 50, (255,50,50), "disappearing"),
                 (220, 40, 170, 50, (255,50,50), "disappearing"),
                 (410, 40, 170, 50, (255,50,50), "disappearing"),
                 (600, 40, 170, 50, (255,50,50), "disappearing"),
                 (30, 110, 170, 50, (50,50,255), "disappearing"),
                 (220, 110, 170, 50, (50,50,255), "disappearing"),
                 (410, 110, 170, 50, (50,50,255), "disappearing"),
                 (600, 110, 170, 50, (50,50,255), "disappearing"),
                 (30, 180, 170, 50, (160,32,240), "disappearing"),
                 (220, 180, 170, 50, (160,32,240), "disappearing"),
                 (410, 180, 170, 50, (160,32,240), "disappearing"),
                 (600, 180, 170, 50, (160,32,240), "disappearing"),
                 (30, 250, 170, 50, (20,20,20), "disappearing"),
                 (220, 250, 170, 50, (20,20,20), "disappearing"),
                 (410, 250, 170, 50, (20,20,20), "disappearing"),
                 (600, 250, 170, 50, (20,20,20), "disappearing"),
                 (300, 500, 150, 20, (255,255,255), "bouncey"),]

# x, y, width, height

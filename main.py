# Code created by Landon Zafiropoulo

'''
create a breakout gameself
create a restart button

'''
import pygame as pie
import os
from settings import *
from sprites import *



class Game:
    def __init__(self):
        self.screen = pie.display.set_mode((WIDTH, HEIGHT))
        pie.display.set_caption("Breakout")
        self.screen.fill(BLACK)
        self.clock = pie.time.Clock()
        self.running = True
    def new(self):
        self.score = 0
        self.all_sprites = pie.sprite.Group()
        self.platforms = pie.sprite.Group()
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        

g = Game()


while g.running:
    g.new()
pie.quit()

# running = True
# while running:
#     for event in pie.event.get():
#         if event.type == pie.QUIT:
#             running = False

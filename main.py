# Code created by Landon Zafiropoulo

'''
create a breakout game
create a restart button

'''
import pygame as pie
import os
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pie.init()
        pie.mixer.init()
        self.screen = pie.display.set_mode((WIDTH, HEIGHT))
        pie.display.set_caption("breakout")
        self.clock = pie.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        self.all_sprites = pie.sprite.Group()
        self.platforms = pie.sprite.Group()
        self.plat0 = Platform(WIDTH, 50, 0, HEIGHT-50, (100,150,150), "base")
        self.all_sprites.add(self.plat0)


        
g = Game()

while g.running:
    g.new()

pie.quit()
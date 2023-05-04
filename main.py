# Code created by Landon Zafiropoulo

'''
create a breakout game
create a restart button

'''
import pygame as pie
import os
from settings import *
from sprites import *

screen = pie.display.set_mode((WIDTH, HEIGHT))
pie.display.set_caption("Breakout")
screen.fill(BLACK)
clock = pie.time.Clock()

running = True
while running:
    for event in pie.event.get():
        if event.type == pie.QUIT:
            running = False

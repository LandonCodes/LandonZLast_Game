# Code created by Landon Zafiropoulo
import pygame as pie
from pygame.sprite import Sprite
from settings import *
from random import randint
vec = pie.math.Vector2

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pie.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pie.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC
        if keystate[pie.K_a]:
            self.acc.x = -PLAYER_ACC
        # if keystate[pg.K_s]:
        #     self.acc.y = PLAYER_ACC
        if keystate[pie.K_d]:
            self.acc.x = PLAYER_ACC
        def jump(self):
            self.rect.x += 1
            hits = pie.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 1
         # making sure the player hits the platform to jump
            self.vel.y = -PLAYER_JUMP
        def inbounds(self):
            if self.rect.x > WIDTH:
                self.vel.x *= -1
                self.pos.x = 0

            if self.rect.x < 0:
                self.vel.x *= -1
                self.pos.x = WIDTH

            if self.rect.y < 0:
                self.vel.y *= -1

            if self.rect.y > HEIGHT:
                self.vel.y *= -1
    def update(self):
        self.inbounds()

class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pie.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
        
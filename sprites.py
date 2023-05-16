#file created by landon zafiropoulo
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((150,20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT-45)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC

    def inbounds(self):
        pass
    def update(self):
        self.acc = vec(0, 0)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Mob(Sprite):
    def __init__(self, game, width,height,color):
        Sprite.__init__(self)
        self.game = game
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(400, 300)
        self.vel = vec(randint(6,15),randint(6,15))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
        if self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y < 0:
            self.vel.y *= -1
        # if self.rect.y > HEIGHT:
        #     self.vel.y += 1
 
    def update(self):
        self.inbounds()
        hit = pg.sprite.collide_rect(self, self.game.player)
        if hit:
            print("I hit the " + str(self.game.player))
            self.vel.y *= -1
        hit_plat = pg.sprite.spritecollide(self, self.game.platforms, True)
        self.pos += self.vel
        self.rect.center = self.pos
        #when mob hits platform it reverses its y direction
        mhits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if mhits:
            self.vel.y *= -1 

# new platform class
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
    def update(self):
       if self.variant == "moving":
        self.rect.x += 1

  
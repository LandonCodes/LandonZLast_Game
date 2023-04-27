# Code created by Landon Zafiropoulo

'''
create a breakout game
- 3 lives on screen as hearts
- working restart button
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
        pie.display.set_caption("my game")
        self.clock = pie.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        self.all_sprites = pie.sprite.Group()
        self.platforms = pie.sprite.Group()
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (100,150,150), "base")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    # def events(self):
  
    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_text("TEST", 24, WHITE, WIDTH/2, HEIGHT/2)
        self.all_sprites.draw(self.screen)

        pie.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pie.font.match_font('arial')
        font = pie.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pie.mouse.get_pos()
        return (x,y)

g = Game()

while g.running:
    g.new()

pie.quit()
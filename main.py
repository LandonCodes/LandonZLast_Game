# Code created by Landon Zafiropoulo
# Starting from working
'''
create a breakout game
create a restart button


'''

# import libs
import pygame as pg
import os
import sys
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite 
# Name what I worked on a block of code then the screen shot



# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        #sets score to zero when the game starts
        self.score = 0
        print(self.screen)
        self.died = True

    def new(self):
        # starting a new game
        #  self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.floor = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        #for all the platforms in settings put them in the screen
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.ball = Mob(self, 20, 20, (0,255,0))
        self.all_sprites.add(self.ball)
        self.enemies.add(self.ball)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()  

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        self.screen.fill(BLUE)
            # self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a any key to play", 22, WHITE, WIDTH / 2, HEIGHT / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        # self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 30, RED, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Type to Restart", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False
                    
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
g = Game()
g.show_start_screen()
# kick off the game loop
while g.running:
    g.new()
    g.show_go_screen

pg.quit()
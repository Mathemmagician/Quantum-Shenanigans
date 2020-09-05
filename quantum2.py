
'''Hi Baky'''

import pygame as pg
import sys
import os
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_sounds()
        self.load_data()

    def load_sounds(self):
        pg.mixer.init()
        pg.mixer.music.load(os.path.join("static", "electro2.wav"))
        pg.mixer.music.set_volume(0.02)
        pg.mixer.music.play(loops=-1)
        self.split_sound = pg.mixer.Sound(os.path.join("static", "roblox.wav"))

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.players = pg.sprite.Group()
        player = Player(self, 5, GRIDHEIGHT // 2)
        #player = Player(self, 3, GRIDHEIGHT // 2)
        for x in range(10, 13):
            Wall(self, x, 5)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        self.GAMESTEP = pg.USEREVENT + 1
        pg.time.set_timer(self.GAMESTEP, 1000)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.mixer.music.stop()
        pg.mixer.quit()
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        pg.display.flip()

    def events(self):
        # catch all events here
        dx, dy = 0, 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    dx+=-1
                if event.key == pg.K_RIGHT:
                    dx+=1
                if event.key == pg.K_UP:
                    dy+=-1
                if event.key == pg.K_DOWN:
                    dy+=1
            if event.type == self.GAMESTEP:
                for wall in self.walls:
                    wall.move(dx=-1)

        for player in self.players:
            player.move(dx, dy)

        for player in self.players:
            player.collide_with_players()

        #print('sum', sum([player.power for player in self.players]))
        if sum([player.power for player in self.players]) > 1.05:
            print([player.power for player in self.players])
            pg.time.delay(5000)


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

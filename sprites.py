import pygame as pg
from settings import *
import random

class Player(pg.sprite.Sprite):

    idCounter = 0

    def __init__(self, game, x, y, power=1):
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.power = power
        self.update_color()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.id = Player.idCounter
        Player.idCounter += 1

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.collide_with_items()
            
        if not self.collide_with_walls(dx, dy):
            self.x = min(max(0, self.x), GRIDWIDTH-1)
            self.y = min(max(0, self.y), GRIDHEIGHT-1)
        else:
            Player(self.game, self.x, self.y-1, self.power/2)
            Player(self.game, self.x, self.y+1, self.power/2)
            self.game.split_sound.play()
            self.kill()


    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x and wall.y == self.y:
                return True
        return False

    def collide_with_players(self):
        for player in self.game.players:
            if player == self:
                continue
            if self.x == player.x and self.y == player.y and self.id < player.id:
                self.update_power(delta = player.power)
                player.kill()

    def collide_with_items(self):
        for item in self.game.items:
            if self.x == item.x and self.y == item.y:
                self.update_power(delta = item.boost)
                item.kill()
                self.game.coid_sound.play()
                Item(self.game)

    def update_power(self, coeff=1, delta=0):
        self.power = coeff * self.power + delta
        self.update_color()

    def update_color(self):
        self.image.fill(np.clip(YELLOW * self.power + BGCOLOR * (1-self.power), 0, 255))

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def move(self, dx=0):
        self.x += dx
        if self.x < 0:
            self.kill()
            Wall(self.game, GRIDWIDTH-1, random.randint(0, GRIDHEIGHT-1))

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Item(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.boost = random.uniform(0, 1)
        self.image.fill(BLUE * self.boost + RED * (1 - self.boost))
        self.rect = self.image.get_rect()
        self.x = GRIDWIDTH
        self.y = random.randint(0, GRIDHEIGHT-1)
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self, dx=0):
        self.x += dx
        if self.x < 0:
            self.kill()
            Item(self.game)
            Item(self.game)

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


















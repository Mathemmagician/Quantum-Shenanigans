
import pygame
import random

from pygame.locals import (
	KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT,
	K_ESCAPE, QUIT,
)


class Player(pygame.sprite.Sprite):
	def __init__(self, s, m = 0):
		super(Player, self).__init__()
		self.s, self.m = s, m

		self.surf = pygame.Surface((s, s))
		self.surf.fill((255, 0, 0))
		self.rect = self.surf.get_rect()
		self.rect.move_ip(s, s*(SCREEN_HEIGHT//(2*s)))

	def update(self):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -self.s)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, self.s)

		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT

	def quantum_split(self):
		pass

	def move(self, dx = 0, dy = 0):
		self.rect.move_ip(dx*self.s, dy*self.s)

		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT


class Cell(pygame.sprite.Sprite):
	def __init__(self, s, m, x=0, y=0):
		super(Cell, self).__init__()
		self.s, self.m, self.x, self.y = s, m, x, y

		self.surf = pygame.Surface((s - 2 * m, s - 2 * m))
		self.surf.fill((230, 230, 230))
		self.rect = self.surf.get_rect()
		self.rect.move_ip(x*s+m, y*s+m)

	# Move the sprite based on user keypresses
	def update(self):
		pass


pygame.init()
pygame.key.set_repeat(500, 100)

NEXTSTEP = pygame.USEREVENT + 1
pygame.time.set_timer(NEXTSTEP, 10)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
CELL_SIZE, CELL_MARGIN = 40, 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():

	all_sprites = pygame.sprite.Group()
	bg_sprites = pygame.sprite.Group()
	players = pygame.sprite.Group()

	for i in range(SCREEN_WIDTH // CELL_SIZE):
		for j in range(SCREEN_HEIGHT // CELL_SIZE):
			cell = Cell(CELL_SIZE, CELL_MARGIN, i, j)
			all_sprites.add(cell)
			bg_sprites.add(cell)


	player = Player(CELL_SIZE)
	all_sprites.add(player)
	players.add(player)


	running = True

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_UP:
					for player in players:
						player.move(dy=-1)
				if event.key == K_DOWN:
					for player in players:
						player.move(dy=+1)


		pressed_keys = pygame.key.get_pressed()

		#player.update(pressed_keys)

		screen.fill((0, 0, 0))

		for entity in all_sprites:
			screen.blit(entity.surf, entity.rect)


		pygame.display.flip()


if __name__ == '__main__':
	main()










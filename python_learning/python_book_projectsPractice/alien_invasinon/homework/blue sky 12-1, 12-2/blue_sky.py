import sys
import pygame

from bully_minion import BullyMinion

def wiondow():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Blue sky")

	rbg_color = (70, 130, 180)

	bully = BullyMinion(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(rbg_color)
		bully.blitme()

		pygame.display.flip()

wiondow()
# Упражнение 12-1 и 12-2.

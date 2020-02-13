import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Pygame")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					print(event.key)
				elif event.key == pygame.K_RIGHT:
					print(event.key)
		pygame.display.flip()
run_game()
# Упражнение 12-4.

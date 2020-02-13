import pygame
import sys

from dvd_image import DVD
from settings import Settings

pygame.init()
settings = Settings()
win = pygame.display.set_mode((settings.win_width, settings.win_height))
pygame.display.set_caption('DVD')

dvd = DVD(win, settings)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    dvd.dvd_direction()
    dvd.update()

    win.fill(settings.win_color)
    dvd.blit()
    pygame.display.update()

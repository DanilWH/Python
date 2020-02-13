import pygame
import sys

import functions as f
from settings import Settings
from character import Character

pygame.init()
settings = Settings() # Создание экземпляра настроек прилодения.
screen = pygame.display.set_mode((settings.screen_weidth,
    settings.screen_height))
pygame.display.set_caption('EasyGame')

clock = pygame.time.Clock()
character = Character(settings, screen) # Создание экземпляра персонажа.
bullets = []

while True:
    clock.tick(30)
    f.check_event(character, bullets, screen, settings) # Отслеживание клавиатуры.

    character.update() # Обновление позиции персонажа.
    f.update_bullet(bullets)
    f.update_game(character, screen, settings, bullets)

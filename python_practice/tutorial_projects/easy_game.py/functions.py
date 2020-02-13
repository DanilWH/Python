import pygame
import sys

from bullet import Bullet

def check_event(character, bullets, screen, settings):
    """Проверка нажатий клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_f:
                create_bullet(bullets, screen, settings, character)
            elif event.key == pygame.K_LEFT:
                character.move_left = True
                character.direction = -1
            elif event.key == pygame.K_RIGHT:
                character.move_right = True
                character.direction = 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.move_left = False
            elif event.key == pygame.K_RIGHT:
                character.move_right = False

    keys = pygame.key.get_pressed()
    if not character.isJump:
        if keys[pygame.K_SPACE]:
            character.isJump = True

def create_bullet(bullets, screen, settings, character):
    if len(bullets) < 5:
        bullet = Bullet(screen, settings, character)
        bullets.append(bullet)

def update_game(character, screen, settings, bullets):
    """Перерисовка экрана и всех поверхностей."""

    image = pygame.image.load('sprites/bg.jpg')
    screen.blit(image, (0, 0))
    for bullet in bullets:
        bullet.draw()
    character.blitme() # Перерисовка персонажа в текущей поцизии.
    pygame.display.update() # Обновление экрана.

def update_bullet(bullets):
    for bullet in bullets:
        bullet.update()
        if bullet.circle.right >= 500 or bullet.circle.right <= 0:
            bullets.remove(bullet)

import sys
import pygame

from bullet import Bullet
def check_keydown_event(event, settings, ship, screen, bullets):
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(bullets, settings, ship, screen)

def fire_bullet(bullets, settings, ship, screen):
	"""Выпускает пулю если максимум ещё не достигнут."""
	# Создание новой пули и включение её в группу bullets
	if len(bullets) < settings.bullet_allowed:
		new_bullet = Bullet(settings, ship, screen)
		bullets.add(new_bullet)

def check_keyup_event(event, ship):
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_event(settings, ship, screen, bullets):
	"""Реагирует на события."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, settings, ship, screen, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship)

def update_screen(settings, ship, screen, bullets):
	screen.fill(settings.rgb_color)
	# Все пули выводятся позади изображения корабля.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	pygame.display.flip()
def update_bullets(bullets):
	"""Обновляет позицию пуль и уничтожает старые."""
	# Обновлении позиции пуль.
	bullets.update()

	# Удаление старых пуль, вышедшых за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.left >= 1200:
			bullets.remove(bullet)
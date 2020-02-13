import pygame
import sys

from bullet import Bullet

def event_tracking(spaceship, g_settings, screen, bullets, play_button, stats,
	target):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			event_tracking_down(event, spaceship, g_settings, screen, bullets,
				stats, target)
		elif event.type == pygame.KEYUP:
			event_tracking_up(event, spaceship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if not stats.game_active:
				check_play_button(play_button, mouse_x, mouse_y, stats,
					spaceship, target, bullets, g_settings)

def reset_game_statistics(stats, bullets, spaceship, target, g_settings):
	"""Сбрасывает статистики игры и запускает её при нажатии кнопки Play."""
	# Сброс скорости настроек.
	g_settings.initialize_game_settings()
	# Сброс игровой статистики.
	stats.reset_stats()

	# Очистка списка пуль.
	bullets.empty()

	# Выравнивание корабля по центру у правого края экрана.
	spaceship.center_spaceship()
	# Выравнивание мишени по центру у правого края экрана.
	target.center_target()

	# При нажатии кнопки Play игра переходит в активное состояние.
	stats.game_active = True

def check_play_button(play_button, mouse_x, mouse_y, stats, spaceship, target,
	bullets, g_settings):
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		# Сброс игровой статистики.
		reset_game_statistics(stats, bullets, spaceship, target, g_settings)

def event_tracking_down(event, spaceship, g_settings, screen, bullets, stats,
	target):
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		reset_game_statistics(stats, bullets, spaceship, target, g_settings)
	elif event.key == pygame.K_UP:
		spaceship.move_up = True
	elif event.key == pygame.K_DOWN:
		spaceship.move_down = True
	elif event.key == pygame.K_SPACE:
		if len(bullets) < g_settings.number_bullets and stats.game_active:
			new_bullet = Bullet(g_settings, spaceship, screen)
			bullets.add(new_bullet)

def event_tracking_up(event, spaceship):
	if event.key == pygame.K_UP:
		spaceship.move_up = False
	elif event.key == pygame.K_DOWN:
		spaceship.move_down = False

def check_update_bullets(g_settings, bullets, target, spaceship, stats):
	# Проверка вышедших пуль за экран и столкновений с мишенью.
	for bullet in bullets.copy():
		if bullet.rect.right <= 0:
			check_bullet_screen(g_settings, bullets, target, spaceship, stats)
			bullets.remove(bullet)

		elif pygame.sprite.spritecollideany(target, bullets):
			g_settings.increase_speed()
			bullets.remove(bullet)

def update_bullets(g_settings, bullets, target, spaceship, stats):
	# Проверка вышедших пуль за экран и столкновений с мишенью.
	check_update_bullets(g_settings, bullets, target, spaceship, stats)
	bullets.update() # Обновление позиции пули.


def update_target(target):
	"""Обновляет позицию экрана и поверяет достижение края экрана."""
	target.update_target()
	target.check_edges()


def check_bullet_screen(g_settings, bullets, target, spaceship, stats):
	"""Проверяет промахи сделанные пользователем."""
	if stats.number_of_misses > 0:
		stats.number_of_misses -= 1
	else:
		stats.game_active = False

def update_screen(screen, g_settings, spaceship, target, bullets, play_button,
	stats):
	"""Отрисовка и обновление экрана."""

	screen.fill(g_settings.rgb_color) # Заполнение экрана цветом.

	# Отрисовка пуль.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	spaceship.blitme() # Отрисовка корабля.
	target.blitme_target() # Отрисовка мишени.

	if not stats.game_active:
		play_button.draw_button()

	pygame.display.flip() # Обновление кадров экрана.
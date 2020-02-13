import pygame

class Bullet():
    def __init__(self, screen, settings, character):
        self.screen = screen
        self.direction = character.direction # Инициализация направления пули.

        self.circle = pygame.Rect(0, 0, settings.radius * 2,
            settings.radius * 2)

        # Назначение координат, где должна появляться пуля.
        # Координата x.
        self.circle.centerx = character.rect.centerx + (
            (character.rect.width / 2) - settings.radius -
            settings.bullet_speed) * self.direction
        # Координата y.
        self.circle.centery = character.rect.centery + 10

        # Хранение координаты x в вещественном формате.
        self.x = float(self.circle.centerx)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed
        self.radius = settings.radius

    def update(self):
        self.x += self.speed * self.direction

        self.circle.centerx = self.x

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
            (self.circle.centerx, self.circle.centery), self.radius)

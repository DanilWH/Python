import pygame
import random

class DVD():
    """Inicialization dvd image."""

    def __init__(self, win, settings):
        self.win = win
        self.win_width = settings.win_width
        self.win_height = settings.win_height

        self.images = [pygame.image.load('images/DVD_v2.png'),
            pygame.image.load('images/DVD_blue.png'),
            pygame.image.load('images/DVD_pink.png'),
            pygame.image.load('images/DVD_green.png'),
            pygame.image.load('images/DVD_red.png'),
            pygame.image.load('images/DVD_turquoise.png'),
            pygame.image.load('images/DVD_yellow.png')]

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.win_rect = self.win.get_rect()

        self.random_coordination_x = random.randint(
            (0 + self.rect.width // 2), (self.win_width - self.rect.width // 2)
        )
        self.random_coordination_y = random.randint(
            (0 + self.rect.height // 2), (self.win_height - self.rect.height // 2)
        )

        self.rect.centerx = self.random_coordination_x
        self.rect.centery = self.random_coordination_y

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        self.random_direction_x = random.randrange(-1, 2, 2)
        self.random_direction_y = random.randrange(-1, 2, 2)

        self.move_x = self.random_direction_x
        self.move_y = self.random_direction_y

        self.speed = settings.speed
        self.color_count = 0

    def update(self):
        self.x += self.speed * self.move_x
        self.y += self.speed * self.move_y

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def dvd_direction(self):

        if self.rect.left <= self.win_rect.left:
            self.move_x = 1
            self.check_color()
        if self.rect.right >= self.win_rect.right:
            self.move_x = -1
            self.check_color()
        if self.rect.top <= self.win_rect.top:
            self.move_y = 1
            self.check_color()
        if self.rect.bottom >= self.win_rect.bottom:
            self.move_y = -1
            self.check_color()

        print(self.color_count)

    def check_color(self):
        if self.color_count >= 6:
            self.color_count = 0
        else:
            self.color_count += 1
        self.image = self.images[self.color_count]

    def blit(self):
        self.win.blit(self.image, self.rect)

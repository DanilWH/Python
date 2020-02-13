import pygame

class Character():
    def __init__(self, settings, screen):
        self.screen = screen

        # Взятие прямоугольника экрана.
        self.screen_rect = self.screen.get_rect()

        # Загрузка стоящего персонажа.
        self.idle = pygame.image.load('sprites/idle.png')
        self.rect = self.idle.get_rect()
        # Загрузка персонажа, идущего влево.
        self.walk_left = [pygame.image.load('sprites/left_1.png'),
            pygame.image.load('sprites/left_2.png'),
            pygame.image.load('sprites/left_3.png'),
            pygame.image.load('sprites/left_4.png'),
            pygame.image.load('sprites/left_5.png'),
            pygame.image.load('sprites/left_6.png')]
        # Загрузка персонажа, идущего вправо.
        self.walk_right = [pygame.image.load('sprites/right_1.png'),
            pygame.image.load('sprites/right_2.png'),
            pygame.image.load('sprites/right_3.png'),
            pygame.image.load('sprites/right_4.png'),
            pygame.image.load('sprites/right_5.png'),
            pygame.image.load('sprites/right_6.png'),]

        # Назначение координат персонажу
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 7

        # Хранение координат в вещественном формате.
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)

        # Назначение скорости и цвета персонажу.
        self.speed = settings.speed
        self.jumpCount = 10
        self.animCount = 0
        self.direction = 1

        # Флаги передвижения.
        self.move_left = False
        self.move_right = False
        self.isJump = False

    def update(self):
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        if self.isJump:
            if self.jumpCount >= -10:
                if self.jumpCount >= 0:
                    self.y -= (self.jumpCount ** 2) / 2
                    self.jumpCount -= 1
                else:
                    self.y -= -(self.jumpCount ** 2) / 2
                    self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

        self.rect.centerx = self.x
        self.rect.bottom = self.y

    def blitme(self):
        if self.animCount >= 30:
            self.animCount = 0

        if self.move_left and not self.move_right:
            self.screen.blit(self.walk_left[self.animCount // 5], self.rect)
            print(self.animCount)
            self.animCount += 1
            print(self.animCount)
        elif self.move_right and not self.move_left:
            self.screen.blit(self.walk_right[self.animCount // 5], self.rect)
            self.animCount += 1
        else:
            self.animCount = 0
            self.screen.blit(self.idle, self.rect)

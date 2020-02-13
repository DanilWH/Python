class Settings():

    def __init__(self):
        """Настройки игры."""
        # Настройки прямоугольника.
        self.speed = 4

        # Настройки экрана:
        self.screen_weidth = 1000
        self.screen_height = 900
        # Цвет фона экрана.
        self.screen_color = (230, 230, 230)

        # Настройки пули.
        self.radius = 3
        self.bullet_color = (240, 240, 240)
        self.bullet_speed = 8

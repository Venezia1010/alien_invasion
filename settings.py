import pygame
# модуль содержит класс с именем Settings для хранения всех настроек

class Settings:
    """Класс для хранения всех настроек игры Alien invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (4, 16, 28)

        # Настройка корабля
        self.bg_image = pygame.image.load('images/space.png')
        self.ship_speed_factor = 1
        self.ship_limit = 3

        # Настройки пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 193, 43)
        self.bullet_allowed = 5
        
        # Настройки пришельцев
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
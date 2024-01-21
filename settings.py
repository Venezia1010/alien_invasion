# модуль содержит класс с именем Settings для хранения всех настроек

class Settings:
    """Класс для хранения всех настроек игры Alien invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (4, 16, 28)
        
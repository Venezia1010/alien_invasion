# модуль содержит класс с именем Settings для хранения всех настроек

class Settings:
    """Класс для хранения всех настроек игры Alien invasion"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
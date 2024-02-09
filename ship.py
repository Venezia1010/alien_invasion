import pygame

class Ship:
    """Класс космический корабыль"""
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальное положение"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника
        # Загрузка изображения
        self.image = pygame.image.load('images/sokol_1.png')
        # После того как изображение будет загружено, метод get_rect() используется
        # для получения атрибута rect поверхности . Один из факторов эффективности
        # Pygame заключается в том, что программист может выполнять операции с игровы-
        # ми элементами как с прямоугольниками даже в том случае, если они имеют другую
        # форму. Операции с прямоугольниками эффективны, потому что прямоугольник —
        # простая геометрическая фигура. Обычно этот подход работает достаточно хорошо
        # и игроки не замечают, что программа не отслеживает точную геометрическую
        # форму каждого игрового элемента.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    

    def update(self):
        """Обновляет положение корабля с учетом флага"""
        if self.moving_right and self.screen_rect.right > self.rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.screen_rect.left < self.rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.screen_rect.top < self.rect.top:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.screen_rect.bottom > self.rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

import pygame

class Ship:
    """Класс космический корабыль"""
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальное положение"""
        self.screen = screen

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
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.movinr_bottom = False
    

    def update(self):
        """Обновляет положение корабля с учетом флага"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_top:
            self.rect.centery -= 1
        if self.movinr_bottom:
            self.rect.centery += 1

    
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)


class Ship_2:
    """Класс добавляет корабль нацентр экрана"""
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/sokol_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
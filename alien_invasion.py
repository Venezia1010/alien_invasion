# Модуль sys нужет чтобы по команде игрока завершить игру
import sys
# Модуль pygame для написания всех аспектов игры
import pygame
# Модуль settings
from settings import Settings

def run_game():
    """Инициализирует pygame, settings и обьект экрана"""
    # Инициализация настроек необходимых для pygame
    pygame.init()
    # Создание отображаемой области (главного окна)
    # Кортеж представляющий разрешение игры
    # Объект screen называется поверхностью (surface). Поверхность в Pygame пред-
    # ставляет часть экрана, на которой отображается игровой элемент. Каждый элемент
    # в игре (например, пришелец или корабль игрока) представлен поверхностью.
    # Поверхность, возвращаемая display.set_mode(), представляет все игровое окно.
    # При активизации игрового цикла анимации эта поверхность автоматически пере-
    # рисовывается при каждом проходе цикла.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Титл окна
    pygame.display.set_caption("Alien Invasion")
    


    # Запуск основного цикла управления игрой
    while True:
        # Отслеживание событий клавиатуры и мыши
        # pygame.event.get() нужен для получения доступа к обнаруженным событиям
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

# Инициализация игры и запуск основного цикла
if __name__ == '__main__':
    run_game()

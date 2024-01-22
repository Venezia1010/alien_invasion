import sys
import pygame


def check_events(ship):
    """Обрабатывает нажатия клавишь и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_top = True
            elif event.key == pygame.K_DOWN:
                ship.movinr_bottom = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_top= False
            elif event.key == pygame.K_DOWN:
                ship.movinr_bottom = False

def update_screen(ai_settings, screen, ship):
    """Отображает изображения на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_top= False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавишь и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Отображает изображения на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)

    # Все пули выводяться позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()


    # screen.blit(ai_settings.bg_image, (0, 0))
    ship.blitme()
    aliens.draw(screen)


def update_bullets(bullets):
    """Обновляет позиции пуль и удаляет старые пули"""
    # Обновление позиции пуль
    bullets.update()

    # Удаление пуль вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    
def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достикнут"""
    # Создание новой пули и включение ее в группу bullets
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев"""
    # Создание пришельца и вычисление кол-ва пришельцев в ряду
    # Интервал между пришельцами равен одному пришельцу
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
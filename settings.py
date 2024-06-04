import pygame


class Settings:
    """游戏基本设置"""
    pygame.font.init()

    #   游戏窗口大小
    screen_width = 1280
    screen_height = 720

    #    游戏背景
    #   bg_image = pygame.image.load("images/bg1.png")
    #   bg_image = pygame.transform.scale(bg_image, [screen_width, screen_height])
    bg_color = 100, 149, 237

    #   飞船设置
    ship_width = 58
    ship_height = 50
    ship_speed_factor = 5

    #   子弹设置
    bullet_color = 139, 69, 19
    bullet_width = 5
    bullet_height = 12
    bullet_speed_factor = 8

    #   敌怪设置
    alien_width = 58
    alien_height = 50
    alien_speed_factor = 1.5
    max_enemies_in_row = 3

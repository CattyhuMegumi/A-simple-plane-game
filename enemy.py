import pygame
from random import random
from random import uniform


class Alien(pygame.sprite.Sprite):
    """敌怪实现"""

    def __init__(self, ai_settings, screen):
        """敌怪初始化"""
        super().__init__()
        #   敌怪设置
        self.width = ai_settings.alien_width
        self.height = ai_settings.alien_height
        self.speed_factor = ai_settings.alien_speed_factor

        #   敌怪图像加载
        self.image = pygame.image.load("images/alien1.png")
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = self.image.get_rect()

        #   随机初始位置
        self.rect.top = 0
        self.rect.centerx = screen.get_rect().width * uniform(0.1, 0.9)  # 禁止在边缘出现

        self.y = float(self.rect.y)

    def update_enemy(self, screen):
        self.y += self.speed_factor * 1
        self.rect.y = int(self.y)
        screen.blit(self.image, self.rect)

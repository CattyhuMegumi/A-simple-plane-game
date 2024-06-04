import pygame


class Bullet(pygame.sprite.Sprite):
    """子弹实现"""
    def __init__(self, ai_settings, ship):
        """子弹初始化"""
        super().__init__()
        #  子弹设置
        self.width = ai_settings.bullet_width
        self.height = ai_settings.bullet_height
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        #   子弹位置初始化
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def update_bullet(self, screen):
        self.y -= self.speed_factor * 1
        self.rect.y = self.y
        pygame.draw.rect(screen, self.color, self.rect)


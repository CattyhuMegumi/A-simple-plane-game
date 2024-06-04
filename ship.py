import pygame


class Ship:
    """飞船类实现"""

    def __init__(self, ai_settings, screen):
        """飞船初始化"""

        #   飞船设置
        self.width = ai_settings.ship_width
        self.height = ai_settings.ship_height
        self.speed_factor = ai_settings.ship_speed_factor

        #   飞船图像加载
        self.image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = self.image.get_rect()

        #    飞船初始位置
        self.rect.centerx = screen.get_width() / 2
        self.rect.bottom = screen.get_rect().bottom - screen.get_height() / 10

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #   飞船移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

        #   飞船开火标志
        self.fire_key = False

    def update_ship(self, screen):
        #   飞船移动
        self.ship_moving(screen)

        #   飞船显示
        screen.blit(self.image, self.rect)

    def ship_moving(self, screen):
        if self.moving_right and self.rect.right < screen.get_rect().right:
            self.x += self.speed_factor * 1
        if self.moving_left and self.rect.x > 0:
            self.x -= self.speed_factor * 1
        if self.moving_forward and self.rect.y > 0:
            self.y -= self.speed_factor * 1
        if self.moving_backward and self.rect.bottom < screen.get_rect().bottom:
            self.y += self.speed_factor * 1

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

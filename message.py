import pygame


def is_click_on_screen(screen) -> bool:
    if pygame.mouse.get_focused():
        return True
    return False


class Message:
    """消息类实现"""

    def __init__(self, msg, font_size=48, color=(0, 0, 0), bg_color=(255, 255, 255)):
        """消息类初始化"""

        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.msg = self.font.render(msg, False, self.color, bg_color)
        self.rect = self.msg.get_rect()

    def draw_msg_on_screen(self, screen, pos: tuple = None):
        """屏幕消息显示，默认居中"""
        if pos is None:
            pos = [screen.get_rect().centerx - self.rect.width / 2, screen.get_rect().centery - self.rect.height / 2]
        self.rect.left, self.rect.top = pos
        screen.blit(self.msg, pos)

    def is_click_on_msg(self) -> bool:
        mouse_posx, mouse_posy = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_posx, mouse_posy):
            return True
        else:
            return False

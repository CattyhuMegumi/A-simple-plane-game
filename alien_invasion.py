import sys

import pygame
import event_check
from settings import Settings
from ship import Ship
from message import Message


class Game:
    """游戏主体"""

    def __init__(self):
        """游戏初始化"""

        self.game_active = True
        #   游戏初始设置
        self.ai_settings = Settings()

        #   游戏界面
        self.game_screen = pygame.display.set_mode([self.ai_settings.screen_width, self.ai_settings.screen_height])
        #   游戏背景图片
        #   bg = self.ai_settings.bg_image
        #   surfaces.append(bg)
        #   game_screen.blit(bg, dest=[0, 0])
        self.game_screen.fill(self.ai_settings.bg_color)

        #   显示游戏界面
        pygame.display.set_caption("Alien Invasion")
        pygame.display.flip()

        #   玩家控制
        self.ship = Ship(self.ai_settings, self.game_screen)

        #   子弹列表
        self.bullets = pygame.sprite.Group()

        #   敌怪列表
        self.enemies = pygame.sprite.Group()
        #   new_alien = Alien(self.ai_settings, self.game_screen)
        #   self.enemies.add(new_alien)

        #   分数
        self.score = 0

        #   定时刷新敌怪
        pygame.time.set_timer(event_check.ENEMY_SPAWN, 3 * 1000)

        #   游戏消息
        #   self.surfaces = []

    def run_game(self):
        """游戏运行"""
        #    pygame初始化
        pygame.init()

        #   游戏时钟
        clock = pygame.time.Clock()

        #   游戏开始
        while self.game_active:
            #   60帧
            clock.tick(60)

            #    检查事件
            event_check.event_check(self)
            self.update_screen()

            #   显示屏幕图像
            pygame.display.update()

        if not self.game_active:
            event_check.event_check(self)

    def update_screen(self):
        """更新屏幕"""
        self.game_screen.fill(self.ai_settings.bg_color)

        #   飞船更新
        self.ship.update_ship(self.game_screen)

        #   子弹更新
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
            else:
                bullet.update_bullet(self.game_screen)

        #   敌怪更新
        for alien in self.enemies.copy():
            alien.update_enemy(self.game_screen)

        #   子弹与敌怪碰撞检测
        self.score += 10 * event_check.bullet_enemy_collision(self.bullets, self.enemies)

        #   分数刷新
        msg_score = Message('Score: ')
        msg_score.draw_msg_on_screen(self.game_screen, [10, 10])
        msg_score_num = Message(str(self.score))
        msg_score_num.draw_msg_on_screen(self.game_screen, [msg_score.rect.right + 10, 10])

        #   游戏结束检测
        if event_check.ship_enemy_collision(self.ship, self.enemies) or event_check.enemy_cross(self.ai_settings, self.enemies):
            if event_check.game_over(self) == 0:
                game.__init__()
                game.run_game()
            else:
                sys.exit()


#   游戏运行
game = Game()
game.run_game()

import sys
import pygame
import bullet
import enemy
import random
from message import Message

ENEMY_SPAWN = pygame.USEREVENT
GAME_OVER = pygame.USEREVENT + 1


# def event_check(ai_settings, screen, ship, bullets, enemies, game_active):
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            sys.exit()
#        elif event.type == pygame.KEYDOWN:
#            event_check_keydown(event, ai_settings, ship, bullets)
#        elif event.type == pygame.KEYUP:
#            event_check_keyup(event, ship)
#        elif event.type == ENEMY_SPAWN:
#            enemy_spawn(ai_settings, screen, enemies)
#        elif event.type == GAME_OVER:
#            game_active = False

def event_check(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_check_keydown(event, game.ai_settings, game.ship, game.bullets)
        elif event.type == pygame.KEYUP:
            event_check_keyup(event, game.ship)
        elif event.type == ENEMY_SPAWN:
            enemy_spawn(game.ai_settings, game.game_screen, game.enemies)
        elif event.type == GAME_OVER:
            game.game_active = False


def event_check_keydown(event, ai_settings, ship, bullets):
    if event.key == pygame.K_w:
        ship.moving_forward = True
    if event.key == pygame.K_s:
        ship.moving_backward = True
    if event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_SPACE:
        new_bullet = bullet.Bullet(ai_settings, ship)
        bullets.add(new_bullet)
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def event_check_keyup(event, ship):
    if event.key == pygame.K_w:
        ship.moving_forward = False
    if event.key == pygame.K_s:
        ship.moving_backward = False
    if event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_d:
        ship.moving_right = False


def enemy_spawn(ai_settings, screen, enemies):
    for i in range(1, random.randint(1, ai_settings.max_enemies_in_row) + 1):
        alien = enemy.Alien(ai_settings, screen)
        enemies.add(alien)


def bullet_enemy_collision(bullets, enemies):
    enemies_number1 = len(enemies)
    pygame.sprite.groupcollide(bullets, enemies, True, True)
    enemies_number2 = len(enemies)
    return enemies_number1 - enemies_number2


def ship_enemy_collision(ship, enemies) -> bool:
    enemy = pygame.sprite.spritecollideany(ship, enemies)
    if enemy is None:
        return False
    else:
        game_over_event = pygame.event.Event(GAME_OVER)
        pygame.event.post(game_over_event)
        return True


def enemy_cross(ai_settings, enemies) -> bool:
    for enemy in enemies.copy():
        if enemy.rect.y > ai_settings.screen_height:
            game_over_event = pygame.event.Event(GAME_OVER)
            pygame.event.post(game_over_event)
            return True
    return False


def game_over(game):
    #   Game Over消息显示
    msg_end = Message('Game Over!', 68)
    msg_end.draw_msg_on_screen(game.game_screen,
                               (game.game_screen.get_rect().centerx -
                                msg_end.rect.width / 2,
                                game.game_screen.get_rect().centery -
                                msg_end.rect.height))

    #   退出和重来选项
    msg_replay = Message('Replay')
    msg_replay.draw_msg_on_screen(game.game_screen,
                                  (game.game_screen.get_rect().centerx -
                                   msg_replay.rect.width - 10,
                                   game.game_screen.get_rect().centery + 10))

    msg_quit = Message('Quit')
    msg_quit.draw_msg_on_screen(game.game_screen,
                                (game.game_screen.get_rect().centerx + 30,
                                 game.game_screen.get_rect().centery + 10))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if msg_replay.is_click_on_msg():
                    return 0
                elif msg_quit.is_click_on_msg():
                    return 1

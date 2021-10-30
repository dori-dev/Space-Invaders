"""Advance Game Space Invaders
"""

# ------------------------------ import ------------------------------
import math
from random import randint, choice
import pygame
from pygame import mixer

# ------------------------------ function ------------------------------

def start_button(screen_var: pygame.display, position: tuple, text: str, color: tuple, size: int):
    """make button in the screen

    Args:
        screen_var (pygame.display): screen name
        position (tuple): x and y of button
        text (str): description of button
        color (tuple): rgb color
        size (int): size of font

    Returns:
        screen.blit: return for make a button
    """
    font = pygame.font.Font('freesansbold.ttf', size)
    text_render = font.render(text, True, color)
    _, _, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen_var, (200, 200, 200), (x, y), (x + w , y), 5)
    pygame.draw.line(screen_var, (200, 200, 200), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen_var, (100, 100, 100), (x, y, w , h))
    return screen_var.blit(text_render, (x, y))


def button(screen_var: pygame.display, position: tuple, text: str, color: tuple):
    """make button in the screen

    Args:
        screen_var (pygame.display): screen name
        position (tuple): x and y of button
        text (str): description of button
        color (tuple): rgb color

    Returns:
        screen.blit: return for make a button
    """
    font = BUTTON_FONT
    text_render = font.render(text, True, color)
    _, _, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen_var, (200, 200, 200), (x, y), (x + w , y), 5)
    pygame.draw.line(screen_var, (200, 200, 200), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen_var, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen_var, (100, 100, 100), (x, y, w , h))
    return screen_var.blit(text_render, (x, y))


def is_collision(x_1: int,
                y_1: int,
                x_2: int,
                y_2: int,
                desired_distance: int) -> bool:
    """calculate collision object 1 and object 2

    Args:
        x_1 (int): x of object 1
        y_1 (int): y of object 1
        x_2 (int): x of object 2
        y_2 (int): y of object 2
        desired_distance (int): good distance

    Returns:
        bool: True or False
    """
    distance = math.sqrt(math.pow(x_1-x_2, 2) + math.pow(y_1-y_2, 2))
    if distance < desired_distance:
        return True
    return False


def player(image: pygame.Surface,
        player_x_size: int,
        player_y_size: int) -> None:
    """make player character in the screen with render picture in x and y size

    Args:
        image (pygame image): image of player character
        player_x_size (int): x size in x axis
        player_y_size (int): y size in y axis
    """
    screen.blit(image, (player_x_size, player_y_size))


def alien(image: pygame.Surface,
        alien_x_size: int,
        alien_y_size: int) -> None:
    """make alien character in the screen with render picture in x and y size

    Args:
        image (pygame.Surface): image of alien character
        alien_x_size (int): x size in x axis
        alien_y_size (int): y size in y axis
    """
    screen.blit(image, (alien_x_size, alien_y_size))


def bullet(image: pygame.Surface,
        bullet_x_size: int,
        bullet_y_size: int) -> None:
    """make bullet character in the screen with render picture in x and y size

    Args:
        image (pygame.Surface): image of bullet character
        bullet_x_size (int): x size in x axis
        bullet_y_size (int): y size in y axis
    """
    screen.blit(image, (bullet_x_size+16, bullet_y_size+10))


def bomb(image: pygame.Surface,
        bomb_x_size: int,
        bomb_y_size: int) -> None:
    """make bomb animation in the screen when bullet collision alien


    Args:
        image (pygame.Surface): image of bomb animation
        bomb_x_size (int): x size in x axis
        bomb_y_size (int): y size in y axis
    """
    screen.blit(image, (bomb_x_size, bomb_y_size))


def show_score() -> None:
    """show score of user in the screen, score means user die how many alien
    """
    font_render = SHOW_FONT.render(
        f'Score: {SCORE_VALUE}', True, (255, 255, 255))
    screen.blit(font_render, (60, 10))


def show_bullet_use() -> None:
    """show bullet use of user, bullet use means user use bullet
    """
    font_render = SHOW_FONT.render(
        f'Fire: {BULLET_USE}', True, (255, 255, 255))
    screen.blit(font_render, (350, 10))


def show_alien_die() -> None:
    """show bullet count of user can use it for fire"""
    font_render = SHOW_FONT.render(
        f'Kill: {ALIEN_DIE}', True, (255, 255, 255))
    screen.blit(font_render, (620, 10))


def show_text(text: str, x: int, y: int) -> None:
    """when the alien collision the player ufo user was game over!
    """
    font_render = GAME_OVER_FONT.render(text, True, (230, 230, 230))
    _, _, w, h = font_render.get_rect()
    pygame.draw.line(screen, (50, 50, 50), (x, y), (x, y))
    pygame.draw.line(screen, (50, 50, 50), (x, y), (x, y))
    pygame.draw.rect(screen, (50, 50, 50), (x, y, w, h-7))
    screen.blit(font_render, (x, y))


# ------------------------------ menu ------------------------------

pygame.init()
screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load('images/bg.jpg')
pygame.display.set_caption('Start of Game')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
mixer.music.load('musics/menu.wav')
mixer.music.set_volume(0.4)
mixer.music.play(-1)
GAME = False
LEARN = False
MENU = True
while MENU:
    screen.blit(bg, (0, 0))
    easy = start_button(screen, (260, 50), 'EASY', (0, 0, 0), 100)
    normal = start_button(screen, (245, 200), 'MEAN', (0, 0, 0), 100)
    hard = start_button(screen, (260, 350), 'HARD', (0, 0, 0), 100)
    learn = start_button(screen, (150, 500), ' How To Play ', (0, 0, 0), 80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MENU = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy.collidepoint(pygame.mouse.get_pos()):
                COUNT_BULLET = 2
                STANDARD = 0.5
                WINS = 0.5
                GOOD_MOBS = 0.5
                BAD_MOBS = 2
                BULLET_SPEED = 2
                UFO_SPEED = 2
                BAD_SCORE = 0.5
                GOOD_SCORE = 2
                MENU = False
                GAME = True
            if normal.collidepoint(pygame.mouse.get_pos()):
                COUNT_BULLET = 1
                STANDARD = 1
                WINS = 1
                GOOD_MOBS = 1
                BAD_MOBS = 1
                BULLET_SPEED = 1
                UFO_SPEED = 1
                BAD_SCORE = 1
                GOOD_SCORE = 1
                MENU = False
                GAME = True
            if hard.collidepoint(pygame.mouse.get_pos()):
                COUNT_BULLET = 0.5
                STANDARD = 1.5
                WINS = 2
                GOOD_MOBS = 2
                BAD_MOBS = 0.5
                BULLET_SPEED = 0.5
                UFO_SPEED = 0.5
                BAD_SCORE = 2
                GOOD_SCORE = 0.5
                MENU = False
                GAME = True
            if learn.collidepoint(pygame.mouse.get_pos()):
                LEARN = True
                COUNT = 0
                if LEARN:
                    screen2 = pygame.display.set_mode((800, 600))
                    bg2 = pygame.image.load('images/learn.png')
                    pygame.display.set_caption('How to Play')
                    icon = pygame.image.load('images/icon.png')
                    pygame.display.set_icon(icon)


                while LEARN:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            LEARN = False
                            MENU = False
                        if COUNT > 1000:
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                if back.collidepoint(pygame.mouse.get_pos()):
                                    LEARN = False
                    screen2.blit(bg2, (0, 0))
                    COUNT += 1
                    if COUNT > 1000:
                        back = start_button(screen2, (30, 270), 'BACK', (0, 0, 0), 65)
                    pygame.display.update()
    pygame.display.update()


while GAME:
    # ------------------------------ main code ------------------------------
    pygame.init()
    bg = pygame.image.load('images/bg.jpg')
    icon = pygame.image.load('images/icon.png')
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(icon)
    mixer.music.load('musics/background.wav')
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)

    # ------------------------------ variable ------------------------------
    exp1_sound = mixer.Sound('musics/exp.wav')
    exp2_sound = mixer.Sound('musics/exp3.wav')
    exp3_sound = mixer.Sound('musics/exp2.wav')
    fire1_sound = mixer.Sound('musics/laser1.wav')
    fire2_sound = mixer.Sound('musics/laser2.wav')
    fire_sound = fire1_sound
    wrong_sound = mixer.Sound('musics/wrong.wav')
    WITCH = 1
    count_back = 0
    alien_y_back = False
    SCORE_VALUE = 0
    BULLET_USE = 0
    BULLET_Y_CHANGE = 2*BULLET_SPEED
    PLAYER_X_SPEED = 0.5*UFO_SPEED
    ALIEN_DIE = 0
    BULLET_UFO = False
    BULLET_IMG_1 = pygame.image.load('images/bullet1.png')
    BULLET_IMG_2 = pygame.image.load('images/bullet2.png')
    BULLET_IMG = BULLET_IMG_1
    UFO1 = pygame.image.load('images/ufo1.png')
    UFO2 = pygame.image.load('images/ufo2.png')
    SHOW_FONT = pygame.font.Font('freesansbold.ttf', 40)
    GAME_OVER_FONT = pygame.font.Font('freesansbold.ttf', 80)
    BUTTON_FONT = pygame.font.Font('freesansbold.ttf', 50)
    ALIEN_COUNT = int(7*BAD_MOBS)
    G_ALIEN_COUNT = int(9*GOOD_MOBS)
    PLAYER_IMG_CHANGE = True
    RUNNING = True
    GAME_OVER_RUNNING = False
    WON_GAME = False
    all_aliens = []
    for a in range(0, 20):
        all_aliens.append((a, pygame.image.load(f'images/alien{a}.png')))
    all_g_aliens = []
    for a in range(1, 9):
        all_g_aliens.append((a, pygame.image.load(f'images/g_alien{a}.png')))
    ALIEN_UFO = {
        10: 15,
        11: 16,
        12: 17,
        13: 18,
        14: 19,
    }
    ALIEN_UFO2 = [15, 16, 17, 18, 19]
    BOMB_ANIMATION = []
    for picture in range(1, 13):
        BOMB_ANIMATION.append(pygame.image.load(f'images/bomb/{picture}.png'))


    # ------------------------------ game objects ------------------------------

    player_img = UFO1
    player_x, player_y, player_x_change = 368, 500, 0

    alien_name = []
    alien_img = []
    alien_y = []
    alien_x = []
    alien_x_change = []


    for a in range(ALIEN_COUNT):
        img = choice(all_aliens[:15])
        alien_name.append(img[0])
        alien_img.append(img[1])
        true_false = [True]
        x_size, y_size = 500, 150
        while any(true_false):
            true_false = []
            x_size = randint(6, 730)
            y_size = randint(30, 250)
            for x_point, y_point in zip(alien_x, alien_y):
                true_false.append(is_collision(x_size, y_size, x_point, y_point, 64))
        alien_x.append(x_size)
        alien_y.append(y_size)
        alien_x_change.append(randint(4, 12)/10)


    g_alien_name = []
    g_alien_img = []
    g_alien_y = []
    g_alien_x = []
    g_alien_x_change = []
    g_alien_y_change = []

    for a in range(G_ALIEN_COUNT):
        img = choice(all_g_aliens)
        g_alien_name.append(img[0])
        g_alien_img.append(img[1])
        true_false = [True]
        x_size, y_size = 500, 150
        while any(true_false):
            true_false = []
            x_size = randint(6, 730)
            y_size = randint(30, 250)
            for x_point, y_point in zip(alien_x, alien_y):
                true_false.append(is_collision(x_size, y_size, x_point, y_point, 64))
        g_alien_x.append(x_size)
        g_alien_y.append(y_size)
        g_alien_x_change.append(randint(4, 12)/10)
        g_alien_y_change.append(1)


    bullet_x, bullet_y, bullet_state = 0, 490, 'ready'
    # bullet_state='ready' bullet not shoot
    # bullet_state='fire' bullet was shoot

    animation, index, round_count, bomb_x, bomb_y = False, 0, 0, 0, 490



    # ------------------------------ run game ------------------------------

    while RUNNING:
        screen.blit(bg, (0, 0))
        player(player_img, player_x, player_y)
        show_score()
        show_bullet_use()
        show_alien_die()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                GAME = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -PLAYER_X_SPEED
                elif event.key == pygame.K_RIGHT:
                    player_x_change = PLAYER_X_SPEED
                elif event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        fire_sound.play()
                        bullet_x = player_x
                        bullet(BULLET_IMG, bullet_x, bullet_y)
                        bullet_state = 'fire'
                        BULLET_USE += 1
                elif event.key == pygame.K_RETURN:
                    if PLAYER_IMG_CHANGE:
                        player_img = UFO2
                        fire_sound = fire2_sound
                        PLAYER_IMG_CHANGE = False
                        PLAYER_X_SPEED = 3
                        BULLET_Y_CHANGE = 6
                        if bullet_state == 'ready':
                            BULLET_IMG = BULLET_IMG_2
                        else:
                            BULLET_UFO = True
                    else:
                        player_img = UFO1
                        fire_sound = fire1_sound
                        PLAYER_IMG_CHANGE = True
                        BULLET_Y_CHANGE = 2*BULLET_SPEED
                        PLAYER_X_SPEED = 0.5*UFO_SPEED
                        if bullet_state == 'ready':
                            BULLET_IMG = BULLET_IMG_1
                        else:
                            BULLET_UFO = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x += player_x_change
        if player_x > 730:
            player_x = 730
        elif player_x < 6:
            player_x = 6

        if bullet_y < -25:
            bullet_y = 480
            bullet_state = 'ready'
            if BULLET_UFO:
                BULLET_UFO = False
                if PLAYER_IMG_CHANGE:
                    BULLET_IMG = BULLET_IMG_1
                else:
                    BULLET_IMG = BULLET_IMG_2

        if bullet_state == 'fire':
            bullet(BULLET_IMG, bullet_x, bullet_y)
            bullet_y -= BULLET_Y_CHANGE
        if BULLET_USE > (100*COUNT_BULLET):
            try:
                if BULLET_USE/SCORE_VALUE > (2.5*STANDARD) or BULLET_USE/SCORE_VALUE < 0:
                    RUNNING = False
                    GAME_OVER_RUNNING = True
            except ZeroDivisionError:
                RUNNING = False
                GAME_OVER_RUNNING = True
        if SCORE_VALUE > (200*WINS):
            if 0 < BULLET_USE/SCORE_VALUE < (2.5*STANDARD):
                RUNNING = False
                WON_GAME = True

        for a in range(ALIEN_COUNT):
            alien_x[a] += alien_x_change[a]

            if alien_x[a] > 730:
                alien_x_change[a] = -randint(4, 12)/10
                alien_y[a] += randint(6, 20)
            if alien_x[a] < 6:
                alien_x_change[a] = randint(4, 12)/10
                alien_y[a] += randint(6, 20)
            alien(alien_img[a], alien_x[a], alien_y[a])

            if is_collision(player_x, player_y, alien_x[a], alien_y[a], 70):
                RUNNING = False
                GAME_OVER_RUNNING = True
                break

            elif is_collision(alien_x[a], alien_y[a], bullet_x, bullet_y, 40):
                bomb_x, bomb_y, round_count, index, animation = bullet_x, bullet_y, 0, 0, True
                if BULLET_UFO:
                    BULLET_UFO = False
                    if PLAYER_IMG_CHANGE:
                        BULLET_IMG = BULLET_IMG_1
                    else:
                        BULLET_IMG = BULLET_IMG_2

                if alien_name[a] in ALIEN_UFO:
                    exp1_sound.play()
                    alien_img[a] = all_aliens[ALIEN_UFO[alien_name[a]]][1]
                    alien_name[a] = ALIEN_UFO[alien_name[a]]
                    bullet_y = 480
                    bullet_state = 'ready'
                    alien_y_back = a

                else:
                    if alien_name[a] in ALIEN_UFO2:
                        exp2_sound.play()
                    else:
                        exp3_sound.play()
                    bullet_y = 480
                    bullet_state = 'ready'
                    if PLAYER_IMG_CHANGE:
                        SCORE_VALUE += (1*GOOD_SCORE)
                    else:
                        SCORE_VALUE += 1
                    ALIEN_DIE += 1
                    img = choice(all_aliens[:15])
                    alien_img[a] = img[1]
                    alien_name[a] = img[0]
                    true_false = [True]
                    x_size, y_size = 150, 250
                    while any(true_false):
                        true_false = []
                        x_size = randint(6, 730)
                        y_size = randint(30, 250)
                        for x_point, y_point in zip(alien_x, alien_y):
                            true_false.append(is_collision(
                                x_size, y_size, x_point, y_point, 64))
                    alien_x[a] = x_size
                    alien_y[a] = y_size

        for a in range(G_ALIEN_COUNT):
            g_alien_x[a] += g_alien_x_change[a]

            if g_alien_y[a] > 420:
                g_alien_y_change[a] = -1
            elif g_alien_y[a] < 180:
                g_alien_y_change[a] = 1
            if g_alien_x[a] > 730:
                g_alien_x_change[a] = -randint(4, 12)/10
                g_alien_y[a] += randint(6, 20) * g_alien_y_change[a]
            elif g_alien_x[a] < 6:
                g_alien_x_change[a] = randint(4, 12)/10
                g_alien_y[a] += randint(6, 20) * g_alien_y_change[a]
            alien(g_alien_img[a], g_alien_x[a], g_alien_y[a])

            if is_collision(g_alien_x[a], g_alien_y[a], bullet_x, bullet_y, 40):
                bomb_x, bomb_y, round_count, index, animation = bullet_x, bullet_y, 0, 0, True
                if BULLET_UFO:
                    BULLET_UFO = False
                    if PLAYER_IMG_CHANGE:
                        BULLET_IMG = BULLET_IMG_1
                    else:
                        BULLET_IMG = BULLET_IMG_2


                exp2_sound.play()
                wrong_sound.play()
                bullet_y = 480
                bullet_state = 'ready'
                if PLAYER_IMG_CHANGE:
                    SCORE_VALUE -= (1*BAD_SCORE)
                else:
                    SCORE_VALUE -= 1
                ALIEN_DIE += 1
                img = choice(all_g_aliens)
                g_alien_img[a] = img[1]
                g_alien_name[a] = img[0]
                true_false = [True]
                x_size, y_size = 150, 250
                while any(true_false):
                    true_false = []
                    x_size = randint(6, 730)
                    y_size = randint(30, 250)
                    for x_point, y_point in zip(alien_x, alien_y):
                        true_false.append(is_collision(
                            x_size, y_size, x_point, y_point, 64))
                g_alien_x[a] = x_size
                g_alien_y[a] = y_size



        if animation:
            if index == 12:
                index, round_count, animation = 0, 0, False
            bomb(BOMB_ANIMATION[index], bomb_x, bomb_y-30)
            if round_count == 15:
                round_count = 0
                index += 1
            round_count += 1

        if alien_y_back:
            alien_y[alien_y_back] = alien_y[alien_y_back] - 2
            count_back += 1
            if count_back == 7:
                count_back = 0
                alien_y_back = False
        pygame.display.update()

    # ------------------------------ game over ------------------------------

    mixer.music.stop()
    if GAME_OVER_RUNNING:
        game_over_sound = mixer.Sound('musics/game_over.wav')
        game_over_sound.set_volume(0.9)
        game_over_sound.play()
    while GAME_OVER_RUNNING:
        quit_b = button(screen, (70, 170), ' Close Game ', (0, 0, 0))
        play_again_b = button(screen, (450, 170), ' Play Again ', (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_OVER_RUNNING = False
                GAME = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_b.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    GAME = False
                if play_again_b.collidepoint(pygame.mouse.get_pos()):
                    GAME_OVER_RUNNING = False
        show_text('YOU LOSE', 195, 340)
        pygame.display.update()

    # ------------------------------ won ------------------------------

    if WON_GAME:
        game_over_sound = mixer.Sound('musics/won.wav')
        game_over_sound.set_volume(0.8)
        game_over_sound.play()

    while WON_GAME:
        quit_b = button(screen, (70, 170), ' Close Game ', (0, 0, 0))
        play_again_b = button(screen, (450, 170), ' Play Again ', (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                WON_GAME = False
                GAME = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_b.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    GAME = False
                if play_again_b.collidepoint(pygame.mouse.get_pos()):
                    WON_GAME = False
        show_text('YOU WON', 200, 340)
        pygame.display.update()

# Jenei Endre - TA2QUN
# Python beadandó - Snake Game

'''
A futtatáshoz szükséges a pygame library telepítése (8.4 MB)!
Terminálba kell a következő parancsot futtatni: pip install pygame

De megtalálható futtatható állományként is a 'TA2QUN_Python_SnakeGame' könyváron belül (TA2QUN_beadando.exe).

A kígyó irányítása a 'WASD' gombokkal történik.
'''

import pygame as pg
from random import randrange

# random pozíció
get_random_position = lambda: [randrange(*range), randrange(*range)]

# ablak
window = 700
tile_size = 35
range = (tile_size // 2, window - tile_size // 2, tile_size)
screen = pg.display.set_mode([window] * 2)
pg.display.set_caption('Jenei Endre (TA2QUN)')

# idő
time, time_step = 0, 110
clock = pg.time.Clock()

# kígyó
snake = pg.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

# alma
food = snake.copy()
food.center = get_random_position()

# pont kiírás
pg.init()
score_value = 0
font = pg.font.SysFont("verdana", 20)


def draw_score():
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 5))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -tile_size)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, tile_size)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-tile_size, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (tile_size, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
    screen.fill('black')
    draw_score()

    # szélek és magábafordulás figyelése
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir, score_value = 1, (0, 0), 0
        segments = [snake.copy()]

    # alma felvétel és pontok
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
        score_value += 1

    # alma kirajzolása
    pg.draw.rect(screen, 'red', food)

    # kígyó kirajzolása
    [pg.draw.rect(screen, 'green', segment) for segment in segments]

    # kígyó mozgatása
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pg.display.flip()
    clock.tick(60)

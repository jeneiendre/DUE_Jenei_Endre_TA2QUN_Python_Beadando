# Jenei Endre - TA2QUN
# Python beadando - Snake Game

"""
A futtatáshoz szükséges a pygame modul telepítése!

A kígyó irányítása a nyilakkal történik.
"""

import pygame
import random
import osztaly
import fuggveny

# Szinek
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Ablak kirajzolasa, cime es icon
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jenei Endre (TA2QUN)')
pygame_icon = pygame.image.load('snake.png')
pygame.display.set_icon(pygame_icon)

# Kigyo peldanyositasa es elhelyezese az ablak kozepen
snake = osztaly.Snake
snake_x = screen_width / 2
snake_y = screen_height / 2
snake.speed = 15
snake.size = 10
snake.length = 1

# Kezdoertekek
apple_x = round(random.randrange(0, screen_width - snake.size) / 10.0) * 10.0
apple_y = round(random.randrange(0, screen_height - snake.size) / 10.0) * 10.0
speed_x = 0
speed_y = 10

game_over = False
starting = True

running = True
clock = pygame.time.Clock()

# A 'running' mindaddig igaz amig a felhasznalo ki nem lep
while running:
    # Jatek loop
    if not game_over:
        # Kezdokepernyo
        if starting:
            screen.fill(green)
            fuggveny.starting_screen(screen, screen_height, black)
        # Innen indul a jatek
        else:
            screen.fill(black)

            # A kigyo fejet mindig elore helyezi
            snake_head = [snake_x, snake_y]
            snake.blocks.append(snake_head)

            # Figyeli a kigyo hosszat
            if len(snake.blocks) > snake.length:
                del snake.blocks[0]

            # Magabafordulas ellenorzese
            for x in snake.blocks[:-1]:
                if x == snake_head:
                    game_over = True

            # A kigyo blokkjainak kirajzolasa minden pontban ami a jatekose
            for block in snake.blocks:
                pygame.draw.rect(screen, green, [block[0], block[1], snake.size, snake.size])
            # Az elso alma kirajzolasa
            pygame.draw.rect(screen, red, [apple_x, apple_y, snake.size, snake.size])

            # Kigyo mozgatasa adott sebesseggel
            snake_x += speed_x
            snake_y += speed_y

            # Alma felvetele, uj pozicioba helyezese es kigyo hosszanak novelese
            if snake_x == apple_x and snake_y == apple_y:
                apple_x = round(random.randrange(0, screen_width - snake.size) / 10.0) * 10.0
                apple_y = round(random.randrange(0, screen_height - snake.size) / 10.0) * 10.0
                snake.length += 1

            # A kigyo figyelese, hogy alul vagy felul kimegy-e az ablakbol
            if (snake_x >= screen_width or snake_x < 0 or
                    # A kigyo figyelese, hogy jobb vagy baloldal kimegy-e az ablakbol
                    snake_y >= screen_height or snake_y < 0):
                game_over = True

    # Game over (pontok es utasitasok kiiratasa)
    else:
        screen.fill(green)
        fuggveny.game_over_screen(screen, snake.length, screen_height, black)

    # Kepernyo frissitese
    pygame.display.flip()
    clock.tick(snake.speed)

    # Esemenyek kezelese
    for event in pygame.event.get():
        # 'KEYDOWN' esemenyek kezelese
        if event.type == pygame.KEYDOWN:
            # Leallitja a jatekot (Q gomb)
            if event.key == pygame.K_q:
                running = False
            # Ujra inditja a jatekot (Space gomb)
            if event.key == pygame.K_SPACE:
                game_over = False
                starting = False
                snake_x = screen_width / 2
                snake_y = screen_height / 2
                snake.blocks = []
                snake.length = 1
            # Mozgas (fel, le, bal, jobb nyilakkal)
            if event.key == pygame.K_UP:
                speed_x = 0
                speed_y = -10
            if event.key == pygame.K_DOWN:
                speed_x = 0
                speed_y = 10
            if event.key == pygame.K_LEFT:
                speed_y = 0
                speed_x = -10
            if event.key == pygame.K_RIGHT:
                speed_y = 0
                speed_x = 10
        # 'QUIT' esemeny kezelese (Ha X-el lep ki a felhasznalo)
        if event.type == pygame.QUIT:
            running = False

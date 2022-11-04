import pygame

pygame.init()
font = pygame.font.SysFont('Arial', 30)


def starting_screen(screen, screen_height, font_color):
    text_start1 = font.render('Az kígyó irányításához használd a nyilakat.', False, font_color)
    screen.blit(text_start1, (10, screen_height / 2 - 100))

    text_start2 = font.render('A játék indításához nyomd meg a \'Space\' gombot.', False, font_color)
    screen.blit(text_start2, (10, screen_height / 2 - 50))


def game_over_screen(screen, length, screen_height, font_color):
    score = font.render('Pontok: ' + str(length), False, font_color)
    screen.blit(score, (10, screen_height / 2 - 100))

    text_q = font.render('A \'Q\' lenyomásával léphetsz ki.', False, font_color)
    screen.blit(text_q, (10, screen_height / 2))

    text_space = font.render('A \'Space\' lenyomásával kezdheted előről.', False, font_color)
    screen.blit(text_space, (10, screen_height / 2 - 50))

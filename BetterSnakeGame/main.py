# Imports
import pygame
import random
import time

# Display Settings
width = 800
rows = 20

SCR = pygame.display.set_mode((width, width))
pygame.display.set_caption("Snake Game")

FPS = 60
VEL = width // rows

# Colors
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
GREY = pygame.Color(128, 128, 128)
BLUE = pygame.Color(0, 0, 255)
DARKBLUE = pygame.Color(0, 0, 128)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
ORANGE = pygame.Color(255, 165, 0)
PINK = pygame.Color(255, 192, 203)
YELLOW = pygame.Color(255, 255, 0)


# Fruit Class


class Fruit:
    step = 44
    x = 0
    y = 0

    def __init__(self, x, y, color):
        self.x = x * self.step
        self.y = y
        self.color = color

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, (self.x, self.y, 10, 10))


class Player:

    def __init__(self, x, y, length):
        self.x = x
        self.y = y

    def draw(self, scr, size):
        pygame.draw.rect(scr, WHITE, (self.x, self.y, size, size))


def draw_grid(width, rows, scr):
    sizeBtw = width // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtw
        y = y + sizeBtw

        pygame.draw.line(scr, GREY, (x, 0), (x, width))
        pygame.draw.line(scr, GREY, (0, y), (width, y))


def main(scr, width):
    run = True

    left = False
    right = False
    up = False
    down = False

    clock = pygame.time.Clock()

    p = Player(400, 400, 0)

    def redraw_window():
        scr.fill(BLACK)
        draw_grid(width, rows, SCR)
        p.draw(SCR, width // rows)
        pygame.display.update()

    while run:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if left:
            p.x -= VEL
        if right:
            p.x += VEL
        if up:
            p.y -= VEL
        if down:
            p.y += VEL

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not right:
            left = True
            right = False
            up = False
            down = False
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not left:
            left = False
            right = True
            up = False
            down = False
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not up:
            left = False
            right = False
            up = False
            down = True
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and not down:
            left = False
            right = False
            up = True
            down = False

        if p.y > width or p.y < -10 or p.x > width or p.x < -10:
            run = False
    pygame.quit()


main(SCR, width)

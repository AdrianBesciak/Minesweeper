# Example file showing a basic pygame "game loop"
import random

import pygame
import resources
from element import Element

field_width = 20
field_height = 20
mines_amount = 10
element_size = 32
border = 16
top_border = 100

# pygame setup
pygame.init()
display_width = element_size * field_width + border * 2
display_height = element_size * field_height + border + top_border
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Minesweeper")

grid = []
mines = []


def generate_minefield():
    for _ in range(mines_amount):
        print('Mine: ', i, j)
        i = random.randrange(0, field_width)
        j = random.randrange(0, field_height)
        grid[i][j].flag = True


def game():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for j in range(field_height):
        line = []
        for i in range(field_width):
            element = Element(i, j, element_size, border, top_border, is_mine=True, screen=screen)
            line.append(element)
            element.draw()
        grid.append(line)

    game_state = "Running"
    while game_state != "Exit":
        # limits FPS to 60
        clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = "Exit"
            elif event.type == pygame.MOUSEBUTTONUP:
                for row in grid:
                    for element in row:
                        if element.rect.collidepoint(event.pos):
                            if event.button == 1:
                                element.click()
                            elif event.button == 3:
                                element.flag_marked()

        # flip() the display to put your work on screen
        pygame.display.flip()


game()
pygame.quit()

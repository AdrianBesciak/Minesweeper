# Example file showing a basic pygame "game loop"

import pygame
import resources
from element import Element
from minefield import Minefield

field_width = 10
field_height = 10
mines_amount = 10


# pygame setup
pygame.init()
display_width = resources.element_size * field_width + resources.border * 2
display_height = resources.element_size * field_height + resources.border + resources.top_border
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Minesweeper")


def game():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    minefield = Minefield(field_width, field_height, mines_amount, screen)

    game_state = "Running"
    while game_state != "Exit":
        # limits FPS to 60
        clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = "Exit"
            elif event.type == pygame.MOUSEBUTTONUP:
                for row in minefield.grid:
                    for element in row:
                        if element.rect.collidepoint(event.pos):
                            if event.button == 1:
                                mines_in_neighbourhood = minefield.count_neighbours(minefield.grid.index(row),
                                                                                    row.index(element))
                                element.click(mines_in_neighbourhood)
                            elif event.button == 3:
                                element.flag_marked()

        # flip() the display to put your work on screen
        pygame.display.flip()


game()
pygame.quit()

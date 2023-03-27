# Example file showing a basic pygame "game loop"

import pygame
import resources
from minefield import Minefield

field_width = 15
field_height = 15
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
                                row_index = minefield.grid.index(row)
                                column_index = row.index(element)
                                mines_in_neighbourhood = minefield.count_neighbours(row_index, column_index)
                                clicked = element.click(mines_in_neighbourhood)
                                if clicked:
                                    minefield.uncover_neighbours(row_index, column_index)   #Todo isn't this a bug if we will click on flag?
                            elif event.button == 3:
                                element.flag_marked()

        # flip() the display to put your work on screen
        pygame.display.flip()


game()
pygame.quit()

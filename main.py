# Example file showing a basic pygame "game loop"

import pygame
import resources
from minefield import Minefield
import game_state
from timer import Timer

field_width = 30
field_height = 16
mines_amount = 10


# pygame setup
pygame.init()
display_width = resources.element_size * field_width + resources.border * 2
display_height = resources.element_size * field_height + resources.border + resources.top_border
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont('Consolas', 30)
game_timer = Timer(screen=screen, font=font)


def game():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    minefield = Minefield(field_width, field_height, mines_amount, screen, font)
    game_timer.print()

    while game_state.state != game_state.GameState.EXIT:
        # limits FPS to 60
        clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.state = game_state.GameState.EXIT
            elif event.type == pygame.USEREVENT:
                game_timer.update()
            elif event.type == pygame.MOUSEBUTTONUP:
                if game_state.state == game_state.GameState.FAILED or game_state.state == game_state.GameState.WON:
                    minefield = Minefield(field_width, field_height, mines_amount, screen, font)
                    game_timer.reset()
                    game_state.state = game_state.GameState.NOT_STARTED
                    continue
                for row in minefield.grid:
                    for element in row:
                        if element.rect.collidepoint(event.pos):
                            row_index = minefield.grid.index(row)
                            column_index = row.index(element)
                            if game_state.state == game_state.GameState.NOT_STARTED:
                                game_state.state = game_state.GameState.IN_PROGRESS
                                minefield.generate_mines(row_index, column_index)
                                game_timer.start()
                            if event.button == 1:
                                mines_in_neighbourhood = minefield.count_mined_neighbours(row_index, column_index)
                                clicked = element.click(mines_in_neighbourhood)
                                if clicked:
                                    minefield.uncover_neighbours(row_index, column_index)   #Todo isn't this a bug if we will click on flag?
                                minefield.is_game_won()
                                if minefield.is_game_won():
                                    game_state.state = game_state.GameState.WON
                                    minefield.uncover_whole_field()
                                    minefield.mines_counter.game_won()
                                    print("Game WON!!!")
                            elif event.button == 3:
                                element.flag_marked()
                            print(minefield.flagged_mines)

        if game_state.state != game_state.GameState.IN_PROGRESS:
            game_timer.stop()

        # flip() the display to put your work on screen
        pygame.display.flip()


game()
pygame.quit()

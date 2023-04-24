# Example file showing a basic pygame "game loop"

import pygame
import resources
from minefield import Minefield
from game_state import GameState
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
    minefield = Minefield(field_width, field_height, mines_amount, screen, font)
    game_timer.print()
    state = GameState(screen)

    while not state.quit():
        # limits FPS to 60
        clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.set_quit()
            elif event.type == pygame.USEREVENT:
                game_timer.update()
            elif event.type == pygame.MOUSEBUTTONUP:
                if state.is_clicked(event.pos) or state.is_finished():
                    minefield = Minefield(field_width, field_height, mines_amount, screen, font)
                    game_timer.reset()
                    state.reset_game()
                    continue
                for row in minefield.grid:
                    for element in row:
                        if element.rect.collidepoint(event.pos):
                            row_index = minefield.grid.index(row)
                            column_index = row.index(element)
                            if state.is_not_started():
                                state.start_game()
                                minefield.generate_mines(row_index, column_index)
                                game_timer.start()
                            if event.button == 1:
                                mines_in_neighbourhood = minefield.count_mined_neighbours(row_index, column_index)
                                clicked = element.click(mines_in_neighbourhood, state)
                                if clicked:
                                    minefield.uncover_neighbours(row_index, column_index, state)   #Todo isn't this a bug if we will click on flag?
                                minefield.is_game_won()
                                if minefield.is_game_won():
                                    state.win_game()
                                    minefield.uncover_whole_field(state)
                                    minefield.mines_counter.game_won()
                                    print("Game WON!!!")
                            elif event.button == 3:
                                element.flag_marked()
                            print(minefield.flagged_mines)

        if not state.is_in_progress():
            game_timer.stop()

        state.draw()

        # flip() the display to put your work on screen
        pygame.display.flip()


game()
pygame.quit()

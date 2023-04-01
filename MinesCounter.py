
import pygame

import resources


class MinesCounter:
    def __init__(self, screen, font):
        self.flagged_mines = 0
        self.field_width = 60
        self.field_height = 30
        self.screen = screen
        self.font = font
        self.print()

    def added_flag(self):
        self.flagged_mines += 1
        self.print()

    def deleted_flag(self):
        self.flagged_mines -= 1
        self.print()

    def print(self):
        text = '{:03d}'.format(self.flagged_mines)
        self.screen.fill((0, 0, 0), (resources.border, resources.border, self.field_width, self.field_height))
        self.screen.blit(self.font.render(text, True, (250, 250, 250)), (resources.border, resources.border))

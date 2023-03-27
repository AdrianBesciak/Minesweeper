import pygame
import resources


class Element:
    def __init__(self, x, y, field_size, border_size, top_border_size, is_mine, screen):
        self.x = x
        self.y = y
        self.clicked = False
        self.mineClicked = False
        self.mineFalse = False
        self.flag = False
        self.rect = pygame.Rect(border_size + self.x * field_size, top_border_size + self.y * field_size, field_size, field_size)
        self.mine = is_mine
        self.screen = screen

    def draw(self, resource=resources.img_element):
        self.screen.blit(resource, self.rect)

    def click(self):
        if not self.flag:
            self.draw(resources.img_empty_field)

    def flag_marked(self):
        self.draw(resources.img_flag)
        self.flag = True

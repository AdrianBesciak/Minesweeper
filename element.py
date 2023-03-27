import pygame
import resources


class Element:
    def __init__(self, x, y, field_size, border_size, top_border_size, screen):
        self.x = x
        self.y = y
        self.clicked = False
        self.mine = False
        self.flag = False
        self.rect = pygame.Rect(border_size + self.x * field_size, top_border_size + self.y * field_size, field_size, field_size)
        self.screen = screen

    def draw(self, resource=resources.img_element):
        self.screen.blit(resource, self.rect)

    def click(self, mined_neighbours):
        if not self.clicked:
            self.clicked = True
            if self.mine:
                self.draw(resources.img_mineClicked)
            else:
                if mined_neighbours == 0:
                    self.draw(resources.img_empty_field)
                elif mined_neighbours == 1:
                    self.draw(resources.img_element1)
                elif mined_neighbours == 2:
                    self.draw(resources.img_element2)
                elif mined_neighbours == 3:
                    self.draw(resources.img_element3)
                elif mined_neighbours == 4:
                    self.draw(resources.img_element4)
                elif mined_neighbours == 5:
                    self.draw(resources.img_element5)
                elif mined_neighbours == 6:
                    self.draw(resources.img_element6)
                elif mined_neighbours == 7:
                    self.draw(resources.img_element7)
                elif mined_neighbours == 8:
                    self.draw(resources.img_element8)
        return self.clicked

    def flag_marked(self):
        if self.clicked and self.flag:
            self.clicked = False
            self.flag = False
            self.draw()
        elif not self.clicked:
            self.draw(resources.img_flag)
            self.flag = True
            self.clicked = True

    def is_mine(self):
        return self.mine

    def is_clicked(self):
        return self.clicked

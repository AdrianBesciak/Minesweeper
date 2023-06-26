import pygame
import resources


class Element:
    def __init__(self, x, y, mines_counter, minefield, field_size, border_size, top_border_size, screen, icons):
        self.x = x
        self.y = y
        self.clicked = False
        self.mine = False
        self.flag = False
        self.icons = icons
        self.rect = pygame.Rect(border_size + self.x * field_size, top_border_size + self.y * field_size, field_size, field_size)
        self.screen = screen
        self.mines_counter = mines_counter
        self.minefield = minefield

    def draw(self, resource):
        self.screen.blit(resource, self.rect)

    def click(self, mined_neighbours, state):
        if not self.clicked:
            self.clicked = True
            self.minefield.uncovered_fields += 1
            if self.mine:
                state.fail_game()
                self.minefield.uncover_whole_field(state)
                self.draw(self.icons.img_mineClicked)
            else:
                if mined_neighbours == 0:
                    self.draw(self.icons.img_empty_field)
                elif mined_neighbours == 1:
                    self.draw(self.icons.img_element1)
                elif mined_neighbours == 2:
                    self.draw(self.icons.img_element2)
                elif mined_neighbours == 3:
                    self.draw(self.icons.img_element3)
                elif mined_neighbours == 4:
                    self.draw(self.icons.img_element4)
                elif mined_neighbours == 5:
                    self.draw(self.icons.img_element5)
                elif mined_neighbours == 6:
                    self.draw(self.icons.img_element6)
                elif mined_neighbours == 7:
                    self.draw(self.icons.img_element7)
                elif mined_neighbours == 8:
                    self.draw(self.icons.img_element8)
        return self.clicked

    def final_click(self, state):
        if self.clicked:
            return
        if state.is_game_won():
            if self.mine:
                self.draw(self.icons.img_flag)
        else:
            if self.mine:
                self.draw(self.icons.img_mine)

    def flag_marked(self):
        if self.clicked and self.flag:
            self.clicked = False
            self.flag = False
            self.draw(self.icons.img_element)
            self.mines_counter.deleted_flag()
            return False

        elif not self.clicked:
            self.draw(self.icons.img_flag)
            self.flag = True
            self.clicked = True
            self.mines_counter.added_flag()
            return True

    def is_mine(self):
        return self.mine

    def is_clicked(self):
        return self.clicked

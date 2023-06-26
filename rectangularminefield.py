from element import Element
import resources
import random
from MinesCounter import MinesCounter
from minefield import Minefield


class RectangularMinefield(Minefield):
    def __init__(self, width, height, mines_amount, screen, font):
        self.width = width
        self.height = height
        super().__init__(mines_amount, screen, font)

    def generate_grid(self, screen):
        for j in range(self.height):
            line = []
            for i in range(self.width):
                element = Element(i, j, self.mines_counter, self, resources.element_size, resources.border, resources.top_border, screen=screen, icons=resources.RectangularResources)
                line.append(element)
                element.draw(resources.RectangularResources.img_element)
            self.grid.append(line)

    def generate_mines(self, excluded_i, excluded_j):
        for _ in range(self.mines_amount):
            i = excluded_i
            j = excluded_j
            while i == excluded_i and j == excluded_j and not self.grid[i][j].mine:
                i = random.randrange(0, self.width)
                j = random.randrange(0, self.height)
            print('Mine: ', i, j)
            self.grid[j][i].mine = True

    def get_neighbours(self, i, j):
        neighbours = []
        if i > 0:
            if j > 0:
                neighbours.append((i - 1, j - 1))
            neighbours.append((i - 1, j))
            if j < self.width - 1:
                neighbours.append((i - 1, j + 1))

        if j > 0:
            neighbours.append((i, j - 1))
        if j < self.width - 1:
            neighbours.append((i, j + 1))

        if i < self.height - 1:
            if j > 0:
                neighbours.append((i + 1, j - 1))
            neighbours.append((i + 1, j))
            if j < self.width - 1:
                neighbours.append((i + 1, j + 1))
        return neighbours

    def is_game_won(self):
        return self.uncovered_fields == self.width * self.height - self.mines_amount

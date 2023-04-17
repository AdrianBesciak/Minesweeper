from element import Element
import resources
import random
from MinesCounter import MinesCounter


class Minefield:
    def __init__(self, width, height, mines_amount, screen, font):
        self.width = width
        self.height = height
        self.mines_counter = MinesCounter(mines_amount, screen, font)
        self.mines_amount = mines_amount
        self.flagged_mines = 0
        self.grid = []
        self.uncovered_fields = 0
        self.generate_grid(screen)

    def generate_grid(self, screen):
        for j in range(self.height):
            line = []
            for i in range(self.width):
                element = Element(i, j, self.mines_counter, self, resources.element_size, resources.border, resources.top_border, screen=screen)
                line.append(element)
                element.draw()
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

    def count_mined_neighbours(self, i, j):
        mined_neighbours = 0
        for row, column in self.get_neighbours(i, j):
            mined_neighbours += self.grid[row][column].is_mine()
        return mined_neighbours

    def uncover_neighbours(self, i_begin, j_begin, state_icon):
        q = [(i_begin, j_begin)]
        while len(q) > 0:
            row, column = q.pop()
            if not self.grid[row][column].is_mine():
                self.grid[row][column].click(self.count_mined_neighbours(row, column), state_icon)
                if self.count_mined_neighbours(row, column) == 0:
                    neighbours = self.get_neighbours(row, column)
                    for i, j in neighbours:
                        if not self.grid[i][j].is_clicked():
                            q.append((i, j))

    def uncover_whole_field(self, state_icon):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].final_click(state_icon)
                self.uncover_neighbours(i, j, state_icon)

    def is_game_won(self):
        return self.uncovered_fields == self.width * self.height - self.mines_amount

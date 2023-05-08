from element import Element
import resources
import random
from MinesCounter import MinesCounter


class Minefield:
    def __init__(self, mines_amount, screen, font):
        self.mines_counter = MinesCounter(mines_amount, screen, font)
        self.mines_amount = mines_amount
        self.flagged_mines = 0
        self.grid = []
        self.uncovered_fields = 0
        self.generate_grid(screen)

    def generate_grid(self, screen):
        raise NotImplementedError

    def generate_mines(self, excluded_i, excluded_j):
        raise NotImplementedError

    def get_neighbours(self, i, j):
        raise NotImplementedError

    def count_mined_neighbours(self, i, j):
        mined_neighbours = 0
        for row, column in self.get_neighbours(i, j):
            mined_neighbours += self.grid[row][column].is_mine()
        return mined_neighbours

    def uncover_neighbours(self, i_begin, j_begin, state):
        q = [(i_begin, j_begin)]
        while len(q) > 0:
            row, column = q.pop()
            if not self.grid[row][column].is_mine():
                self.grid[row][column].click(self.count_mined_neighbours(row, column), state)
                if self.count_mined_neighbours(row, column) == 0:
                    neighbours = self.get_neighbours(row, column)
                    for i, j in neighbours:
                        if not self.grid[i][j].is_clicked():
                            q.append((i, j))

    def uncover_whole_field(self, state):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].final_click(state)
                self.uncover_neighbours(i, j, state)

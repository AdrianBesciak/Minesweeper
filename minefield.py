from element import Element
import resources
import random

class Minefield:
    def __init__(self, width, height, mines_amount, screen):
        self.width = width
        self.height = height
        self.mines_amount = mines_amount
        self.grid = []
        self.mines = []
        self.generate_grid(screen)
        self.generate_mines()   #ToDo - move this line after first click

    def generate_grid(self, screen):
        for j in range(self.height):
            line = []
            for i in range(self.width):
                element = Element(i, j, resources.element_size, resources.border, resources.top_border, screen=screen)
                line.append(element)
                element.draw()
            self.grid.append(line)

    def generate_mines(self):
        for _ in range(self.mines_amount):
            i = random.randrange(0, self.width)
            j = random.randrange(0, self.height)
            print('Mine: ', i, j)
            self.grid[i][j].mine = True

    def count_neighbours(self, i, j):
        mined_neighbours = 0
        if i > 0:
            if j > 0:
                mined_neighbours += self.grid[i-1][j-1].is_mine()
            mined_neighbours += self.grid[i-1][j].is_mine()
            if j < self.width - 1:
                mined_neighbours += self.grid[i-1][j+1].is_mine()

        if j > 0:
            mined_neighbours += self.grid[i][j-1].is_mine()
        if j < self.width - 1:
            mined_neighbours += self.grid[i][j+1].is_mine()

        if i < self.height - 1:
            if j > 0:
                mined_neighbours += self.grid[i+1][j-1].is_mine()
            mined_neighbours += self.grid[i+1][j].is_mine()
            if j < self.width - 1:
                mined_neighbours += self.grid[i+1][j+1].is_mine()
        return mined_neighbours

    def uncover_neighbours(self, i_begin, j_begin):
        q = []
        q.append((i_begin, j_begin))
        while len(q) > 0:
            row, column = q.pop()
            if row < 0 or row >= self.width or column < 0 or column >= self.height:
                continue
            if self.grid[row][column].is_clicked() and (i_begin != row or j_begin != column):
                continue
            if not self.grid[row][column].is_mine():
                self.grid[row][column].click(self.count_neighbours(row, column))
                if self.count_neighbours(row, column) == 0:
                    q.append((row - 1, column - 1))
                    q.append((row - 1, column))
                    q.append((row - 1, column + 1))
                    q.append((row, column - 1))
                    q.append((row, column + 1))
                    q.append((row + 1, column - 1))
                    q.append((row + 1, column))
                    q.append((row + 1, column + 1))

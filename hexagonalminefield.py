from element import Element
import resources
import random
from MinesCounter import MinesCounter
from minefield import Minefield


class HexagonalMinefield(Minefield):
    def __init__(self, radius, mines_amount, screen, font):
        self.radius = radius
        self.a = 32
        super().__init__(mines_amount, screen, font)

    def generate_grid(self, screen):
        for layer in range(self.field_height()):
            line = []
            line_offset = abs(self.radius - layer - 1) / 2
            print('Line width: ', self.layer_width(layer), 'layer: ', layer, 'offset: ', line_offset)
            for j in range(self.layer_width(layer)):
                x = j + line_offset
                y = (layer) / 3 * 2
                element = Element(x, y, self.mines_counter, self, resources.element_size, resources.border, resources.top_border, screen=screen, icons=resources.HexagonalResources)
                line.append(element)
                element.draw(resources.HexagonalResources.img_element)  #ToDo fix drawing elements
            self.grid.append(line)

    def field_height(self):
        return 2 * self.radius - 1

    def layer_width(self, layer):
        if layer < self.radius:
            return self.radius + layer
        return 3 * self.radius - layer - 2

    def generate_mines(self, excluded_layer, excluded_item):
        for _ in range(self.mines_amount):
            layer = excluded_layer
            item = excluded_item
            while layer == excluded_layer and item == excluded_item and not self.grid[layer][item].mine:
                layer = random.randrange(0, self.field_height())
                item = random.randrange(0, self.layer_width(layer))
            print('Mine: ', layer, item)
            self.grid[layer][item].mine = True

    def get_neighbours(self, i, j):
        neighbours = []
        # if i > 0:
        #     if j > 0:
        #         neighbours.append((i - 1, j - 1))
        #     neighbours.append((i - 1, j))
        #     if j < self.width - 1:
        #         neighbours.append((i - 1, j + 1))
        #
        # if j > 0:
        #     neighbours.append((i, j - 1))
        # if j < self.width - 1:
        #     neighbours.append((i, j + 1))
        #
        # if i < self.height - 1:
        #     if j > 0:
        #         neighbours.append((i + 1, j - 1))
        #     neighbours.append((i + 1, j))
        #     if j < self.width - 1:
        #         neighbours.append((i + 1, j + 1))
        return neighbours

    def is_game_won(self):
        return self.uncovered_fields == self.width * self.height - self.mines_amount

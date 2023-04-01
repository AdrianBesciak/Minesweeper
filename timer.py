import pygame

import resources


class Timer:
    def __init__(self, screen, font):
        self.timer = 0
        self.screen = screen
        self.font = font
        self.print()

    def start(self):
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.timer = 0

    def stop(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)

    def update(self):
        self.timer += 1
        self.print()

    def reset(self):
        self.timer = 0
        self.print()

    def print(self):
        text = str(self.timer)
        self.screen.fill((0, 0, 0), (resources.border, resources.border, 60, 30))
        self.screen.blit(self.font.render(text, True, (250, 250, 250)), (resources.border, resources.border))

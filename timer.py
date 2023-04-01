import pygame

import resources


class Timer:
    def __init__(self, screen, font):
        self.timer_width = 60
        self.timer_height = 30
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
        window_size = pygame.display.get_window_size()
        text = '{:03d}'.format(self.timer)
        self.screen.fill((0, 0, 0), (
        window_size[0] - resources.border - self.timer_width, resources.border, self.timer_width, self.timer_height))
        self.screen.blit(self.font.render(text, True, (250, 250, 250)),
                         (window_size[0] - resources.border - self.timer_width, resources.border))

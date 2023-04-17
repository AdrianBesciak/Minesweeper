from enum import Enum
import resources
import pygame


class GameState:
    class States(Enum):
        NOT_STARTED = 1
        IN_PROGRESS = 2
        WON = 3
        FAILED = 4
        EXIT = 5

    def __init__(self, screen):
        self.state = self.States.NOT_STARTED
        self.screen = screen
        width, _ = pygame.display.get_surface().get_size()
        self.rect = pygame.Rect(width // 2 - resources.big_element_size // 2,
                                resources.top_border // 2 - resources.big_element_size // 2, resources.big_element_size,
                                resources.big_element_size)
        self.rect_face = pygame.Rect(width // 2 - resources.face_size // 2,
                                resources.top_border // 2 - resources.face_size // 2, resources.face_size,
                                resources.face_size)

    def set_state(self, new_state):
        self.state = new_state

    def draw(self):
        if self.state == self.States.NOT_STARTED:
            self.screen.blit(resources.img_big_element, self.rect)
            self.screen.blit(resources.img_face_smiling, self.rect_face)
        elif self.state == self.States.IN_PROGRESS:
            self.screen.blit(resources.img_face_considering, self.rect_face)
        elif self.state == self.States.FAILED:
            self.screen.blit(resources.img_face_dead, self.rect_face)
        elif self.state == self.States.WON:
            self.screen.blit(resources.img_face_sunglasses, self.rect_face)

    def is_clicked(self, click_position):
        return self.rect.collidepoint(click_position)

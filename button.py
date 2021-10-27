import pygame
import os

black = (0, 0, 0)


class Button:

    def __init__(self, window, x, y, image):
        self.image = pygame.image.load(os.path.join('assets', image)).convert_alpha()
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        window.blit(self.image, (self.rect.x, self.rect.y))

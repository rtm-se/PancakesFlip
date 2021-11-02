import os

import pygame


class Dot(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'hit_bar.png')).convert()
        self.rect = self.image.get_rect(midtop=(x, y))




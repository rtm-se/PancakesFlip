import pygame
import os

SLIDER_VEL = 3

class SliderBar(pygame.sprite.Sprite):
    def __init__(self, back_bar, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'slider_bar.png'))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.slider_vector = 'right'
        self.back = back_bar

    def move_slider(self):
        if self.slider_vector == 'right':
            self.rect.x += SLIDER_VEL
        elif self.slider_vector == 'left':
            self.rect.x -= SLIDER_VEL

        if self.rect.x + 5 >= self.back.width + self.back.x - 30 and self.slider_vector == "right":
            self.slider_vector = "left"
        elif self.rect.x <= self.back.x + 30 and self.slider_vector == "left":
            self.slider_vector = "right"

    def update(self):
        self.move_slider()

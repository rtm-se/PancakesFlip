import pygame
import os

black = (0, 0, 0)


class Button:

    def __init__(self, window, x, y, image, image2):
        self.image_static = pygame.image.load(os.path.join('assets', image)).convert_alpha()
        self.image_pressed = pygame.image.load(os.path.join('assets', image2)).convert_alpha()
        self.rect = self.image_static.get_rect(topleft = (x,y))
        self.window = window



    def draw_button_static(self):
        self.window.blit(self.image_static, self.rect)

    def draw_button_active(self):
        self.window.blit(self.image_pressed, self.rect)
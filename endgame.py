import pygame
import os
from button import Button

class Endgame:

    def __init__(self, window):
        self.window = window
        self.shadow = pygame.image.load(os.path.join('assets', 'shadow.png')).convert_alpha()
        self.rety_button = Button(self.window, 355, 569, 'button1-static.png', 'button1-HW.png')
        self.meny_button = Button(self.window, 355, 644, 'button2.png', 'button2.png')
        self.list_of_buttons = [self.rety_button, self.meny_button]


    def main_loop(self):
        self.window.blit(self.shadow, (0, 0))

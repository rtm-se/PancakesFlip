import os.path

import pygame
from button import Button

WHITE = (255, 255, 255)


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load(os.path.join("assets", "menu_bg.png"))
        self.window.blit(self.bg, (0, 0))
        self.button1 = Button(self.window, (self.window.get_width() / 100) * 35.9,
                              (self.window.get_height() / 100) * 58.9, "button_1.png")
        self.button2 = Button(self.window, (self.window.get_width() / 100) * 35.9,
                              (self.window.get_height() / 100) * 68.7, "button_2.png")
        self.button3 = Button(self.window, (self.window.get_width() / 100) * 35.9,
                              (self.window.get_height() / 100) * 78.5, "button_3.png")

        # pygame.draw.rect(self.window, WHITE, [self.window.get_width()/2, self.window.get_height()/2, 140, 40])
        pygame.display.update()



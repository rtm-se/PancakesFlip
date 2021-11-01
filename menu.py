import os.path

import pygame
from button import Button

WHITE = (255, 255, 255)


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load(os.path.join("assets", "menu_bg.png"))
        self.button1 = Button(self.window, (self.window.get_width() / 100) * 35.9,
                              (self.window.get_height() / 100) * 58.9, "button1-static.png", "button1-HW.png")
        self.button2 = Button(self.window, (self.window.get_width() / 100) * 35.9,
                              (self.window.get_height() / 100) * 68.7, "button2-static.png", "button2-HW.png")
        self.button3 = Button(self.window, (self.window.get_width() / 100) * 35.9,
                              (self.window.get_height() / 100) * 78.5, "button3-static.png", "button3-HW.png")

        self.list_of_buttons = [self.button1, self.button2, self.button3]








import os
import pygame
# in case of adding button to the credits screen
#from button import Button

class Credits():
    def __init__(self):
        self.image = pygame.image.load(os.path.join('assets', 'credits.png'))

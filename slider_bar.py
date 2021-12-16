import pygame
import os
import time
# SLIDER_VEL = 3

class SliderBar(pygame.sprite.Sprite):
    def __init__(self, back_bar, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'slider_bar.png'))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.slider_vector = 'right'
        self.back = back_bar
        self.time = time.time()
        self.start_music_time = 0
    #todo make a new slider movement system that would sync up to the beat

    def move_slider(self, vel):
        if self.slider_vector == 'right':
            self.rect.x += 2
        elif self.slider_vector == 'left':
            self.rect.x -= 2

        if self.rect.x >= self.back.width + self.back.x and self.slider_vector == "right":
            self.slider_vector = "left"
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
        elif self.rect.x <= self.back.x and self.slider_vector == "left":
            self.slider_vector = "right"
            pygame.mixer.music.stop()
            pygame.mixer.music.play()

    def update(self, vel):
        self.move_slider(vel)
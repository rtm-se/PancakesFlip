import pygame
import os
import time
# SLIDER_VEL = 3

class SliderBar(pygame.sprite.Sprite):
    def __init__(self, back_bar, x, y, slider_function_access):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'slider_bar.png'))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.slider_vector = 'right'
        self.back = back_bar
        self.time = time.time()
        self.start_music_time = 0
        self.slide_access = slider_function_access
    #todo make a new slider movement system that would sync up to the beat

    def move_slider(self, vel):
        mill_seconds = pygame.mixer.music.get_pos()
        print(mill_seconds)
        pos_per_pixel = self.back.width / 4000
        bar_pos = pos_per_pixel * (mill_seconds - self.start_music_time)
        if self.slider_vector == 'right':
            self.rect.x = self.back.x + bar_pos
        elif self.slider_vector == 'left':
            self.rect.x  = self.back.x + self.back.width - pos_per_pixel * (mill_seconds - self.start_music_time)

        if self.rect.x >= self.back.width + self.back.x and self.slider_vector == "right":
            self.slider_vector = "left"
            self.start_music_time += 4000
            self.slide_access.slider_edge_check()

            #pygame.mixer.music.stop()
            #pygame.mixer.music.play()
        elif self.rect.x <= self.back.x and self.slider_vector == "left":
            self.slider_vector = "right"
            self.start_music_time += 4000

            self.slide_access.slider_edge_check()
            #pygame.mixer.music.stop()
            #pygame.mixer.music.play()

    def update(self, vel):
        self.move_slider(vel)
import os.path
import random
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
SLIDER_VEL = 3

#TODO add lives
#TODO add endgame screen

class Slider:

    def __init__(self, win):
        self.bg_picture = pygame.image.load(os.path.join('assets', 'slider_bg.png')).convert()
        self.chief_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_1.png')).convert_alpha(), (371, 390))
        self.chief_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_2.png')).convert_alpha(), (371, 390))
        self.bar_picture = pygame.image.load(os.path.join('assets', 'bar.png')).convert_alpha()
        self.bar_rect = self.bar_picture.get_rect(topleft = (325, 139))

        self.dots_list = []
        self.slider_vector = "right"
        self.slider = self.generate_slider()

    def generate_dot(self):
        pass

        difficulty = 25
        y = self.bar_rect.y + 5
        x = random.randint(self.bar_rect.x, self.bar_rect.x + self.bar_rect.width - difficulty)
        self.dots_list.append(pygame.Rect(x, y, difficulty, self.bar_rect.height-10))


    def generate_slider(self):
        size = 5
        y = self.bar_rect.y
        x = self.bar_rect.x
        return pygame.Rect(x, y, size, self.bar_rect.height)

    def move_slider(self):
        if self.slider_vector == "right":
            self.slider.x += SLIDER_VEL
        elif self.slider_vector == "left":
            self.slider.x -= SLIDER_VEL

        if self.slider.x + 5 >= self.bar_rect.width + self.bar_rect.x and self.slider_vector == "right":
            self.slider_vector = "left"
        elif self.slider.x <= self.bar_rect.x and self.slider_vector == "left":
            self.slider_vector = "right"

    def hit_check(self):
        for dot in self.dots_list:
            if dot.colliderect(self.slider):
                self.dots_list.remove(dot)
                return True
            else:
                pass

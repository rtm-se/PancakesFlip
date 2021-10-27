import random
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
SLIDER_VEL = 3


class Slider:

    def __init__(self, win):
        self.background = pygame.Rect(win.get_width() // 2 - 250, win.get_height() // 2 - 25, 500, 50)
        self.dots_list = []
        self.slider_vector = "right"
        self.slider = self.generate_slider()

    def generate_dot(self):
        difficulty = 25
        y = self.background.y
        x = random.randint(self.background.x, self.background.x + self.background.width - difficulty)
        self.dots_list.append(pygame.Rect(x, y, difficulty, self.background.height))

    def generate_slider(self):
        size = 5
        y = self.background.y
        x = self.background.x
        return pygame.Rect(x, y, size, self.background.height)

    def move_slider(self):
        if self.slider_vector == "right":
            self.slider.x += SLIDER_VEL
        elif self.slider_vector == "left":
            self.slider.x -= SLIDER_VEL

        if self.slider.x + 5 >= self.background.width + self.background.x and self.slider_vector == "right":
            self.slider_vector = "left"
        elif self.slider.x <= self.background.x and self.slider_vector == "left":
            self.slider_vector = "right"

    def hit_check(self):
        for dot in self.dots_list:
            if dot.colliderect(self.slider):
                self.dots_list.remove(dot)
                return True
            else:
                pass

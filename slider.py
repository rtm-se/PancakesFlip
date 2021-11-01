import os.path
import random
import pygame
from random import randint
from dot import Dot
from slider_bar import SliderBar
from chief import Chief
from button import Button

BLACK = (0, 0, 0)
RED = (255, 0, 0)

PAN_COLOR = '#FFAD7E'



class Slider:

    def __init__(self, win):
        self.lives = 3
        self.score = 0
        self.window = win
        self.mode = 'game'

        self.bg_picture = pygame.image.load(os.path.join('assets', 'slider_bg.png')).convert()
        self.bar_picture = pygame.image.load(os.path.join('assets', 'bar.png')).convert_alpha()
        self.bar_rect = self.bar_picture.get_rect(topleft=(332, 139))

        self.font = pygame.font.SysFont('Roboto', 40)
        self.lives_text = self.font.render(f'{self.lives}', 1, BLACK)

        self.list_of_buttons = []

        self.chief = pygame.sprite.Group()
        self.chief.add(Chief())

        self.dot_group = pygame.sprite.Group()

        self.slider_bar = pygame.sprite.GroupSingle()
        self.slider_bar.add(SliderBar(self.bar_rect, self.bar_rect.x + 50, self.bar_rect.y))

    '''
    def generate_dot(self):
        difficulty = 25
        y = self.bar_rect.y + 5
        x = random.randint(self.bar_rect.x, self.bar_rect.x + self.bar_rect.width - difficulty)
        self.dots_list.append(pygame.Rect(10, 10, 10, 10))
    '''

    def generate_slider(self):
        size = 5
        y = self.bar_rect.y
        x = self.bar_rect.x
        return pygame.Rect(x, y, size, self.bar_rect.height)

    def hit_check(self):
        if pygame.sprite.spritecollide(self.slider_bar.sprite, self.dot_group, True):
            self.score += 1
        else:
            self.lives -= 1
            self.update_lives_text()
            if self.lives <= 0:
                self.mode = 'retry_screen'


    def make_screenshot(self):
        self.window.blit(self.bg_picture, (0, 0))
        score_text = self.font.render('0', 1, BLACK)
        self.window.blit(self.lives_text, (154, 63))
        self.window.blit(self.bar_picture, self.bar_rect)
        self.window.blit(score_text, (929, 63))
        self.chief.draw(self.window)
        self.dot_group.draw(self.window)
        self.slider_bar.draw(self.window)

        rect = self.window.get_rect()
        sub = self.window.subsurface(rect)
        self.sub = sub.copy()





    '''
    def hit_check_3(self):
        for dot in self.dots_list:
            if dot.colliderect(self.slider):
                self.dots_list.remove(dot)
                return True
            else:
                self.lives -= 1
                self.update_lives_text()
                return []

    def hit_check_2(self):
        for dot in self.dots_list:
            if dot.colliderect(self.slider):
                self.dots_list.remove(dot)
                return True
            else:
                self.lives -= 1
                self.update_lives_text()
    '''
    def update_lives_text(self):
        self.lives_text = self.font.render(f'{self.lives}', 1, BLACK)

    def main_loop(self):
        if self.mode == 'game':
            self.window.blit(self.bg_picture, (0, 0))
            score_text = self.font.render(f'{self.score}', 1, BLACK)
            self.window.blit(self.lives_text, (154, 63))

            self.window.blit(self.bar_picture, self.bar_rect)
            self.window.blit(score_text, (929, 63))
            self.chief.update()
            self.chief.draw(self.window)

            if len(self.dot_group) <= 0:
                for _ in range(3):
                    self.dot_group.add(Dot(randint(self.bar_rect.x + 50, self.bar_rect.x + self.bar_rect.width - 50), self.bar_rect.y+6))

            self.dot_group.draw(self.window)
            self.slider_bar.draw(self.window)
            self.slider_bar.update()
            return True

        elif self.mode == 'retry_screen':
            self.make_screenshot()
            return False





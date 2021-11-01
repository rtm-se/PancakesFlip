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
        self.score = 0
        self.font_score_text = pygame.font.SysFont('Roboto', 28)
        self.font_score_number = pygame.font.SysFont('Roboto', 68)

        self.text1 = self.font_score_text.render('Your final score:', 1, 'white')
        self.text1_rect = self.text1.get_rect(center=(1024/2, 222 + self.text1.get_height()/2))
        self.text2 = self.font_score_text.render('Try again?', 1, 'white')
        self.text2_rect = self.text2.get_rect(center=(1024/2, 502 + self.text2.get_height()/2))

        self.score_text = self.font_score_number.render(f'{self.score}', 1, 'white')
        self.score_text_rect = self.score_text.get_rect(center=(1024/2, 283 + self.score_text.get_height()/2))





    def update_score(self, score):
        self.score = score
        self.score_text = self.font_score_number.render(f'{self.score}', 1, 'white')
        self.score_text_rect = self.score_text.get_rect(center=(1024/2, 283 + self.score_text.get_height()/2))

    def main_loop(self):
        self.window.blit(self.shadow, (0, 0))
        self.window.blit(self.text1, self.text1_rect)
        self.window.blit(self.text2, self.text2_rect)
        self.window.blit(self.score_text, self.score_text_rect)


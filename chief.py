import pygame
import os

class Chief(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.chief_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_1.png')).convert_alpha(), (371, 390))
        self.chief_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_2.png')).convert_alpha(), (371, 390))

        self.chief_frame_counter = 0

        self.image = self.chief_1
        self.rect = self.image.get_rect(topleft=(338, 216))

    def idle_anim(self):
        self.chief_frame_counter += 1
        if self.chief_frame_counter % 30 == 0:
            self.chief_frame_counter = 0
            if self.image == self.chief_1:
                self.image = self.chief_2
            else:
                self.image = self.chief_1

    def update(self):
        self.idle_anim()



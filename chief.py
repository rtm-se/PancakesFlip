import pygame
import os

class Chief(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.flip_anim_counter = 0
        self.chief_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_1.png')).convert_alpha(), (371, 390))
        self.chief_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_2.png')).convert_alpha(), (371, 390))
        self.chief_flip = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'dood_flip.png')).convert_alpha(), (371, 390))
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

    def update(self, state):
        if state == 'idle':
            self.idle_anim()
        elif state == 'idle' and self.flip_anim_counter > 0:
            self.image = self.chief_flip
            self.flip_anim_counter -= 1
        if state == 'flip' and self.flip_anim_counter == 0:
            self.flip_anim_counter = 60
        else:
            self.idle_anim()

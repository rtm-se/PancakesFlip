import sys
import pygame
from menu import Menu
from slider import Slider
from credits import Credits
WIDTH = 1024
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
PAN_COLOR = '#FFAD7E'


class MainWindow:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("sliders demo")
        pygame.font.init()
        self.font = pygame.font.SysFont('Roboto', 40)
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.window)
        self.slider = Slider(self.window)
        self.score = 0
        self.dude_counter = 0
        self.chief = self.slider.chief_1
        self.credits = Credits()
    def draw_func(self):
        self.window.blit(self.slider.bg_picture, (0, 0))
        score_text = self.font.render(f'{self.score}', 1, BLACK)

        self.dude_counter += 1

        if self.dude_counter % 30 == 0:
            if self.chief == self.slider.chief_1:
                self.chief = self.slider.chief_2
            else:
                self.chief = self.slider.chief_1
        self.window.blit(self.chief, (391, 216))

        self.window.blit(self.slider.bar_picture, self.slider.bar_rect)
        self.window.blit(score_text, (929, 63))
        if len(self.slider.dots_list) <= 0:
            for _ in range(3):
                self.slider.generate_dot()

        for dot in self.slider.dots_list:
            pygame.draw.rect(self.window, PAN_COLOR, dot)
        self.slider.move_slider()
        pygame.draw.rect(self.window, 'GREEN', self.slider.slider)

    def main_logic(self):
        run = True
        state = "main_menu"
        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if state == "main_menu":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if self.menu.button1.rect.collidepoint(mouse_pos):
                            print('slider')
                            state = "slider"
                        elif self.menu.button3.rect.collidepoint(mouse_pos):
                            print('credits')
                            state = 'credits'
                if state == "credits" and event.type == pygame.KEYDOWN:
                    state = 'main_menu'
                if state == "slider" and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.slider.hit_check():
                        self.score += 1
                    else:
                        self.score -= 1

            if state == "slider":
                self.draw_func()
            if state == "credits":
                self.window.blit(self.credits.image, (0 ,0))
            if state == "main_menu":

                self.window.blit(self.menu.bg, (0, 0))
                for button in self.menu.list_of_buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.draw_button_active()
                    else:
                        button.draw_button_static()
            pygame.display.update()


if __name__ == "__main__":
    MW = MainWindow()
    MW.main_logic()

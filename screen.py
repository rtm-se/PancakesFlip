import sys
import pygame
from menu import Menu
from slider import Slider

WIDTH = 1024
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class MainWindow:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("sliders demo")
        pygame.font.init()
        self.font = pygame.font.SysFont('timesnewroman', 40)
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.window)
        self.slider = Slider(self.window)
        self.score = 0

    def draw_func(self):
        self.window.fill(WHITE)
        score_text = self.font.render(f'Score: {self.score}', 1, GREEN)
        pygame.draw.rect(self.window, BLACK, self.slider.background)
        self.window.blit(score_text, (self.window.get_width() // 2 - score_text.get_width() // 2, 20))
        if len(self.slider.dots_list) <= 0:
            for _ in range(3):
                self.slider.generate_dot()

        for dot in self.slider.dots_list:
            pygame.draw.rect(self.window, RED, dot)
        self.slider.move_slider()
        pygame.draw.rect(self.window, GREEN, self.slider.slider)

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
                            print('button was pressed at {0}'.format(mouse_pos))
                            state = "slider"
                if state == "slider" and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.slider.hit_check():
                        self.score += 1
                    else:
                        self.score -= 1

            if state == "slider":
                self.draw_func()

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

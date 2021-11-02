import sys
import pygame
from menu import Menu
from slider import Slider
from credits import Credits
from endgame import Endgame

WIDTH = 1024
HEIGHT = 768
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
        pygame.mixer.init()
        self.font = pygame.font.SysFont('Roboto', 40)

        self.clock = pygame.time.Clock()

        self.slider = Slider(self.window)
        self.menu = Menu(self.window)
        self.credits = Credits()
        self.endgame = Endgame(self.window)
        self.game_state = "slider"

    def reset_game(self):
        self.slider.lives = 3
        self.slider.score = 0
        self.slider.mode = 'game'
        self.slider.dot_group.empty()
        self.slider.slider_bar.sprite.rect.x = self.slider.bar_rect.x

    def main_logic(self):
        run = True
        state = "main_menu"
        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if state == "credits" and event.type == pygame.KEYDOWN:
                    state = 'main_menu'

                if state == "main_menu":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if self.menu.button1.rect.collidepoint(mouse_pos):
                            print('slider')
                            self.slider.bgm.play(loops=-1)
                            self.reset_game()
                            state = "slider"
                        elif self.menu.button3.rect.collidepoint(mouse_pos):
                            print('credits')
                            state = 'credits'

                if state == "endgame":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if self.endgame.meny_button.rect.collidepoint(mouse_pos):
                            print('main_menu')
                            self.slider.bgm.stop()
                            state = "main_menu"
                        elif self.endgame.rety_button.rect.collidepoint(mouse_pos):
                            print('slider')
                            self.reset_game()
                            self.slider.bgm.play(loops=-1)
                            state = "slider"

                if state == "slider":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.slider.hit_check()

            if state == "slider":
                game_on = self.slider.main_loop()
                if game_on:
                    pass
                else:
                    self.slider.bgm.stop()
                    self.endgame.update_score(self.slider.score)
                    state = "endgame"

            if state == "endgame":
                self.window.blit(self.slider.sub, (0, 0))
                self.endgame.main_loop()

                for button in self.endgame.list_of_buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.draw_button_active()
                    else:
                        button.draw_button_static()

            if state == "credits":
                self.window.blit(self.credits.image, (0, 0))
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

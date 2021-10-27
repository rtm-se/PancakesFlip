import pygame

WIDTH = 1024
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


DOT_HIT = pygame.USEREVENT + 1



class MainWindow:
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("sliders demo")
        pygame.font.init()
        self.font = pygame.font.SysFont('timesnewroman', 40)
        self.clock = pygame.time.Clock()
        self.WIN.get_height()
        self.score = 0


    def draw_func(self, slider):
        self.WIN.fill(WHITE)
        score_text = self.font.render(f'Score: {self.score}', 1, GREEN)
        pygame.draw.rect(self.WIN, BLACK, slider.background)
        self.WIN.blit(score_text, (self.WIN.get_width()//2 - score_text.get_width()//2, 20))
        for dot in slider.dots_list:
            pygame.draw.rect(self.WIN, RED, dot)
        pygame.draw.rect(self.WIN, GREEN, slider.slider)

        pygame.display.update()

    def main_loop(self, slider):
        run = True

        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and slider.hit_check():
                        self.score += 1
                    else:
                        self.score -= 1


            if len(slider.dots_list) <= 0:
                slider.dots_list = [slider.generate_dot() for _ in range(3)]
            slider.move_slider()
            self.draw_func(slider)


#pygame.event.post(pygame.event.Event(DOT_HIT))
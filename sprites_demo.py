import pygame

class Crosshair():
    pass



clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    clock.tick(60)
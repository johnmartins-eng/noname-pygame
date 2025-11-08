import pygame
from pygame.locals import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- Cores ---
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN_LIGHT = (50, 200, 50)
GOLD = (255, 215, 0)
PRESSED_COLOR = (100, 100, 255)
HIT_COLOR = (255, 50, 50)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("NoName")
    clock = pygame.time.Clock()

    app_running = True
    while app_running:
        clock.tick(60)

        # Processamento de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False

            # Lógica do Jogo
            # TODO

        screen.fill(BLACK)

        pygame.display.flip()

    pygame.quit()

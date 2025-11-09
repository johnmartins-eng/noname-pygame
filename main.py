import math
import pygame
from pygame.locals import *

from entities.player import Player


SCREEN_WIDTH =  900
SCREEN_HEIGHT = 500 

# --- Cores ---
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN_LIGHT = (50, 200, 50)
GOLD = (255, 215, 0)
PRESSED_COLOR = (100, 100, 255)
HIT_COLOR = (255, 50, 50)

FPS = 60

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("NoName")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    # Create player and add to group
    player = Player()
    all_sprites.add(player)

    app_running = True
    while app_running:
        clock.tick(FPS)
        screen.fill(GRAY)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False

        # Update & draw all sprites
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()

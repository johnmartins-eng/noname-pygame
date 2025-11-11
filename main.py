import math
import pygame
from pygame.locals import *

from entities.enemies.skeleton import Skeleton
from utils.camera import Camera
from entities.player import Player


SCREEN_WIDTH =  800
SCREEN_HEIGHT = 600 

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

    background = pygame.image.load("assets/backgrounds/bg.png").convert()
    background = pygame.transform.scale(background, (1600, 1600))

    all_sprites = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)
    skeleton = Skeleton()
    all_sprites.add(skeleton)
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    app_running = True
    while app_running:
        clock.tick(FPS)
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False


        all_sprites.update()

        camera.update(player)

        screen.blit(background, (-camera.camera_rect.x, -camera.camera_rect.y))

        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))

        pygame.display.flip()

    pygame.quit()

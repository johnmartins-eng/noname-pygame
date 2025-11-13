import math
import random
import pygame
from pygame.locals import *

from entities.enemies.skeleton import Skeleton
from entities.projectiles.fire import Fire
from utils.camera import Camera
from entities.player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAY = (100, 100, 100)
FPS = 60

SPAWN_INTERVAL = 1500  # milliseconds (1.5 seconds)
PROJECTILE_SPAWN_INTERVAL = 2000  # ms

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("NoName")
    clock = pygame.time.Clock()

    background = pygame.image.load("assets/backgrounds/bg.png").convert()
    background = pygame.transform.scale(background, (1600, 1600))

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    last_spawn_time = pygame.time.get_ticks()
    last_projectile_spawn = pygame.time.get_ticks()

    app_running = True
    while app_running:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_running = False

        if len(enemies) <= 20:
            if current_time - last_spawn_time >= SPAWN_INTERVAL:
                last_spawn_time = current_time

                radius = player.base_radius

                offset_x = random.uniform(-radius, radius)
                offset_y = random.uniform(-radius, radius)

                new_x = player.rect.x + offset_x
                new_y = player.rect.y + offset_y

                new_skeleton = Skeleton(x=new_x, y=new_y)
                all_sprites.add(new_skeleton)
                enemies.add(new_skeleton)

        # projectile spawning (move to player update later)
        if current_time - last_projectile_spawn >= PROJECTILE_SPAWN_INTERVAL:
            last_projectile_spawn = current_time
            fire = Fire(player)
            all_sprites.add(fire)
            projectiles.add(fire)

        # colision (move to player or projectile update later)
        collisions = pygame.sprite.groupcollide(projectiles, enemies, True, False)
        for projectile, hit_list in collisions.items():
            for enemy in hit_list:
                projectile.on_hit(enemy)

        all_sprites.update(player)
        camera.update_position(player)

        screen.fill(GRAY)
        screen.blit(background, (-camera.camera_rect.x, -camera.camera_rect.y))
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))

        pygame.display.flip()

    pygame.quit()

import pygame
from entities.projectiles.base_projectile import BaseProjectile
from utils.direction_enum import DirectionEnum


class Fire(BaseProjectile):
    def __init__(self, player, speed=10.0):
        super().__init__(player, speed)

    def load_frames(self):
        for i in range(0, 6):
            img = pygame.image.load(f"assets/projectiles/fire/basic/sprite_{str(i)}.png").convert_alpha()
            self.frames.append(pygame.transform.scale(img, (40, 40)))

    def update_animation(self):
        if self.frame_count >= 60:
            self.frame_count = 0

        frame_intervals = [0, 10, 20, 30, 40, 50]
        frame_ids = [0, 1, 2, 3, 4, 5]

        for i in range(len(frame_intervals) - 1):
            if frame_intervals[i] <= self.frame_count < frame_intervals[i + 1]:
                self.active_frame = frame_ids[i]
                break

        self.frame_count += 1
        self.image = self.frames[self.active_frame]

    
    def update(self, *args, **kwargs):
        self.update_animation()
        self.move_projectile()

    def move_projectile(self):
        if self.direction == DirectionEnum.RIGHT:
            self.rect.x += self.speed
        if self.direction == DirectionEnum.LEFT:
            self.rect.x -= self.speed
        if self.direction == DirectionEnum.UP:
            self.rect.y += self.speed
        if self.direction == DirectionEnum.DOWN:
            self.rect.y -= self.speed
        if self.direction == DirectionEnum.DIAGONAL_RIGHT_DOWN:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        if self.direction == DirectionEnum.DIAGONAL_LEFT_DOWN:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        if self.direction == DirectionEnum.DIAGONAL_RIGHT_UP:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if self.direction == DirectionEnum.DIAGONAL_LEFT_UP:
            self.rect.x -= self.speed
            self.rect.y += self.speed

import pygame
from entities.base_entity import AnimationModeEnum
from entities.enemies.base_enemy import BaseEnemy


class Skeleton(BaseEnemy):
    def __init__(self, x=405, y=205, health=40, base_damage=5, speed=1.5):
        super().__init__(x, y, health, base_damage, speed)
        self.animation_mode = AnimationModeEnum.RUNNING

    
    def load_frames(self):
        # running frames
        for i in range(0, 12):
            name = f"sprite_0{i}.png" if i < 10 else f"sprite_{i}.png"
            img = pygame.image.load(f"assets/enemies/skeleton/{name}").convert_alpha()
            self.frames.append(pygame.transform.scale(img, (50, 70)))

    def update_animation(self):
        if self.frame_count >= 60:
            self.frame_count = 0

        if self.animation_mode == AnimationModeEnum.RUNNING:
            frame_intervals = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
            frame_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        for i in range(len(frame_intervals) - 1):
            if frame_intervals[i] <= self.frame_count < frame_intervals[i + 1]:
                self.active_frame = frame_ids[i]
                break

        self.frame_count += 1
        self.image = self.frames[self.active_frame]

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def go_to_player(self, target: pygame.sprite.Sprite):
        pass

    def update(self):
        self.update_animation()
        self.go_to_player()
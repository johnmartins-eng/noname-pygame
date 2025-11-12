import pygame
import math

from entities.base_entity import AnimationModeEnum, BaseEntity

START_POS_X = 400
START_POS_Y = 200

PLAYER_SPEED = 5

class Player(BaseEntity):
    def __init__(self):
        super().__init__(x=START_POS_X, y=START_POS_Y, health=200, base_damage=10, speed=3.0)

    def load_frames(self):
        # idle frames
        for i in range(0, 6):
            img = pygame.image.load(f"assets/character/idle/sprite_0{i}.png").convert_alpha()
            self.frames.append(pygame.transform.scale(img, (70, 70)))

        # running frames
        for i in range(6, 14):
            name = f"sprite_0{i}.png" if i < 10 else f"sprite_{i}.png"
            img = pygame.image.load(f"assets/character/running/{name}").convert_alpha()
            self.frames.append(pygame.transform.scale(img, (70, 70)))

    def update_animation(self):
        if self.frame_count >= 60:
            self.frame_count = 0

        if self.animation_mode == AnimationModeEnum.IDLE:  # idle
            frame_intervals = [0, 10, 20, 30, 40, 50, 60]
            frame_ids = [0, 1, 2, 3, 4, 5]
        elif self.animation_mode == AnimationModeEnum.RUNNING:  # running
            frame_intervals = [7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60]
            frame_ids = [6, 7, 8, 9, 10, 11, 12]

        for i in range(len(frame_intervals) - 1):
            if frame_intervals[i] <= self.frame_count < frame_intervals[i + 1]:
                self.active_frame = frame_ids[i]
                break

        self.frame_count += 1
        self.image = self.frames[self.active_frame]
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def __handle_input(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_s]:
            dy = 1
        if keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_d]:
            dx = 1

        moving = dx != 0 or dy != 0

        if moving:
            self.animation_mode = AnimationModeEnum.RUNNING 

            length = math.sqrt(dx * dx + dy * dy)
            dx /= length
            dy /= length
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            if dx > 0:
                self.facing_right = True
            elif dx < 0:
                self.facing_right = False
        else:
            self.animation_mode = AnimationModeEnum.IDLE

    def update(self, *args, **kwargs):
        self.__handle_input()
        self.update_animation()
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            #TODO: make a screen when player loses.
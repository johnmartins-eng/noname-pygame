import pygame
import math

START_POS_X = 400
START_POS_Y = 200

PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, x=START_POS_X, y=START_POS_Y, x_speed=PLAYER_SPEED, y_speed=PLAYER_SPEED):
        super().__init__()

        self.x_speed = x_speed
        self.y_speed = y_speed
        self.facing_right = True
        self.mode = 0  # 0 = idle, 1 = running
        self.frame_count = 0
        self.active_frame = 0

        # Load animations
        self.frames = []
        self.__load_frames()

        # Current image and rect
        self.image = pygame.transform.scale(pygame.image.load(self.frames[self.active_frame]), (70, 70))
        self.rect = self.image.get_rect(topleft=(x, y))

    def __load_frames(self):
        # idle-animation
        for i in range(0,6):
            self.frames.append("assets/character/idle/sprite_0" + str(i) + ".png")

        # running-animation
        for i in range(6, 14):
            if i < 10:
                self.frames.append("assets/character/running/sprite_0" + str(i) + ".png")
            else:
                self.frames.append("assets/character/running/sprite_" + str(i) + ".png")

    def __update_animation(self):
        if self.frame_count >= 60:
            self.frame_count = 0

        if self.mode == 0:  # idle
            frame_intervals = [0, 10, 20, 30, 40, 50, 60]
            frame_ids = [0, 1, 2, 3, 4, 5]
        else:  # running
            frame_intervals = [7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60]
            frame_ids = [6, 7, 8, 9, 10, 11, 12]

        for i in range(len(frame_intervals) - 1):
            if frame_intervals[i] <= self.frame_count < frame_intervals[i + 1]:
                self.active_frame = frame_ids[i]
                break

        self.frame_count += 1

    def handle_input(self):
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
            self.mode = 1 

            length = math.sqrt(dx * dx + dy * dy)
            dx /= length
            dy /= length
            self.rect.x += dx * self.x_speed
            self.rect.y += dy * self.y_speed

            if dx > 0:
                self.facing_right = True
            elif dx < 0:
                self.facing_right = False
        else:
            self.mode = 0 

    def update(self):
        self.handle_input()
        self.__update_animation()

        self.image = pygame.transform.scale(pygame.image.load(self.frames[self.active_frame]), (70, 70))

        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

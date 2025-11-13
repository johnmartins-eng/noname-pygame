import pygame
from abc import ABC, abstractmethod
from enum import Enum

class AnimationModeEnum(Enum):
    IDLE = 0,
    RUNNING = 1,
    ATTACKING = 2,
    DYING = 3


class BaseEntity(pygame.sprite.Sprite, ABC):
    def __init__(self, x: float, y: float, health: int, base_damage: int, speed: float):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.base_damage = base_damage

        self.dying = False
        

        self.frames: list[pygame.Surface] = []
        self.image: pygame.Surface | None = None
        self.rect: pygame.Rect | None = None

        self.facing_right: bool = True
        self.animation_mode: AnimationModeEnum = AnimationModeEnum.IDLE
        self.frame_count: float = 0
        self.active_frame: int = 0

        self.load_frames()

        if self.frames:
            self.image = self.frames[0]
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        else:
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 255))
            self.rect = self.image.get_rect(topleft=(self.x, self.y))

    @abstractmethod
    def load_frames(self):
        raise NotImplementedError

    @abstractmethod
    def update_animation(self):
        raise NotImplementedError
    
    @abstractmethod
    def take_damage(self, amount):
        raise NotImplementedError
    
import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target: pygame.sprite.Sprite):
        return target.rect.move(-self.camera_rect.x, -self.camera_rect.y)

    def update_position(self, target: pygame.sprite.Sprite):
        x = target.rect.centerx - self.width // 2
        y = target.rect.centery - self.height // 2


        self.camera_rect.x = x
        self.camera_rect.y = y
from entities.base_entity import BaseEntity
from abc import ABC

class BaseEnemy(BaseEntity, ABC):
    def __init__(self, x, y, health=40, base_damage=5, speed=1.5, assets=[]):
        super().__init__(x, y, health, base_damage, speed, assets)
        

import pygame


class AssetsManager:
    _instance = None
    
    def __init__(self):
        self.__images = {}
        self.fonts = {}

        self.load_all_assets()
    
    @staticmethod
    def get_instance():
        if AssetsManager._instance is None:
            AssetsManager._instance = AssetsManager()
        return AssetsManager._instance
    
    def load_all_assets(self):
        list_frames = []
        for i in range(0, 12):
            name = f"sprite_0{i}.png" if i < 10 else f"sprite_{i}.png"
            img = pygame.image.load(
                f"assets/enemies/skeleton/walking/{name}").convert_alpha()
            list_frames.append(pygame.transform.scale(img, (50, 70)))

        for i in range(0, 15):
            name = f"sprite_0{i}.png" if i < 10 else f"sprite_{i}.png"
            img = pygame.image.load(
                f"assets/enemies/skeleton/dying/{name}").convert_alpha()
            list_frames.append(pygame.transform.scale(img, (50, 70)))

        self.__images['skeleton'] = list_frames

    def get_images(self, name: str) -> list:
        return self.__images.get(name)
    
    
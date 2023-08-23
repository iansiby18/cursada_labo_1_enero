import pygame

class Personaje:
    
    def __init__(self, tamaño, origen, path_imagen):
        self.superficie = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.midbottom = origen




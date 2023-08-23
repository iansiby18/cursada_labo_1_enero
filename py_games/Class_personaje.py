import pygame

class Personaje:

    def __init__(self, tamaño, origen, path_imagen):
        self.superficie = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.superficie, tamaño)
        self.sonido_colision = pygame.mixer.Sound("Recursos/ñam.mp3")
        self.sonido_colision.set_volume(1)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.midbottom = origen
    
    def mover_imagen(self, sentido: str, desplazamiento: int, tamaño_pantalla):
        if sentido == "Vertical":
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top > tamaño_pantalla[1]:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > tamaño_pantalla[0]:
                self.rectangulo.right = 0
    
    def detectar_colision(self, otra_imagen):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.sonido_colision.play()
            
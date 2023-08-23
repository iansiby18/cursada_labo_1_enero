from Class_imagen import Imagen
import pygame, sys

#CONSTANTES
LARGO = 800 
ALTO = 600

FPS = 30

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

pygame.init()

PANTALLA = pygame.display.set_mode((LARGO,ALTO)) #determina el tamaño de la pantalla en pixeles

clock = pygame.time.Clock()
color_vertical = {"color_inicial": VERDE, "color_colision":ROJO}
color_horizontal = {"color_inicial": AZUL_CLARO, "color_colision":BLANCO}

imagen_vertical = Imagen((100, 100), color_vertical, (LARGO/2, ALTO/2))
imagen_horizontal = Imagen((100, 100), color_horizontal, (LARGO-100, ALTO/2))
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    PANTALLA.fill(NEGRO)
    PANTALLA.blit(imagen_vertical.superficie, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.superficie, imagen_horizontal.rectangulo)
    
    imagen_horizontal.mover_imagen("Horizontal", 10, (LARGO,ALTO))
    imagen_vertical.mover_imagen("Vertical", 10, (LARGO,ALTO))
    
    imagen_horizontal.detectar_colision(imagen_vertical)

    pygame.draw.line(PANTALLA, AZUL, (400,0), (400,800), 1)
    pygame.draw.line(PANTALLA, AZUL, (0,300), (800,300), 1)
    pygame.display.update()

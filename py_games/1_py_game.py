import pygame, sys

#CONSTANTES
LARGO = 500 
ANCHO = 400

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

pygame.init()

PANTALLA = pygame.display.set_mode((LARGO,ANCHO)) #determina el tamaño de la pantalla en pixeles
PANTALLA.fill(BLANCO)

pygame.draw.rect(PANTALLA, VERDE, (100, 50, 100, 200), 1)
pygame.draw.line(PANTALLA, ROJO, (100, 100), (199, 50), 2)
pygame.draw.circle(PANTALLA, AZUL_CLARO, (125, 250), 25, 2)
pygame.draw.ellipse(PANTALLA, NEGRO, (275, 200, 40, 80), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
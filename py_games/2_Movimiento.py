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

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (LARGO/2, ALTO/2)

imagen_horizontal = pygame.Surface((100, 100))
imagen_horizontal.fill(AZUL_CLARO)
rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (LARGO-100, ALTO/2)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    PANTALLA.fill(NEGRO)
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)
    rectangulo_vertical.y += 10
    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0
    rectangulo_horizontal.x += 10
    if rectangulo_horizontal.left > LARGO:
        rectangulo_horizontal.right = 0

    pygame.draw.line(PANTALLA, AZUL, (400,0), (400,800), 1)
    pygame.draw.line(PANTALLA, AZUL, (0,300), (800,300), 1)
    pygame.display.update()
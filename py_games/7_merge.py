from Class_personaje import Personaje
import pygame, sys

#CONSTANTES
#CONSTANTES
LARGO = 1000 
ALTO = 500
FPS = 60
screen_size = (LARGO, ALTO)

pygame.init()

PANTALLA = pygame.display.set_mode(screen_size) #determina el tamaño de la pantalla en pixeles

icono = pygame.image.load("Recursos/icono_homero.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("Recursos/fondo_casa.jpg")
fondo_escalado = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo_escalado,(0,0))
clock = pygame.time.Clock()

homero= Personaje((200, 200), (LARGO/2, ALTO),"Recursos/homero.png")
dona = Personaje((100, 100), (LARGO/2, ALTO), "Recursos/dona.png")

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    PANTALLA.blit(fondo_escalado,(0,0))
    PANTALLA.blit(dona.superficie, dona.rectangulo)
    PANTALLA.blit(homero.superficie, homero.rectangulo)
    
    homero.mover_imagen("Horizontal", 20, (LARGO,ALTO))
    dona.mover_imagen("Vertical", 5, (LARGO,ALTO))
    homero.detectar_colision(dona)
    
    pygame.display.update()

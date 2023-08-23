from Class_imagen import Imagen
import pygame, sys

#CONSTANTES
LARGO = 1000 
ALTO = 500
screen_size = (LARGO, ALTO)

pygame.init()

PANTALLA = pygame.display.set_mode(screen_size) #determina el tamaño de la pantalla en pixeles

icono = pygame.image.load("Recursos/icono_homero.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("Recursos/fondo_casa.jpg")
fondo_escalado = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo_escalado,(0,0))

#musica

pygame.mixer.music.load("Recursos/intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

import pygame
import random


BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
ANCHO_VENTANA = 600
ALTO_VENTANA = 600

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

fuente = pygame.font.SysFont("consolas", 25)
texto = fuente.render("Hola 1c", False, VERDE, AZUL_CLARO)

flag = True
while flag:
    VENTANA.fill(NEGRO)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    
    VENTANA.blit(texto, (0,0))
    
    pygame.display.update()

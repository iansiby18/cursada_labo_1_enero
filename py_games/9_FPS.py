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
flag = True

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("prueba fps") #nombre para cuando se abre la ventana del juego

fuente = pygame.font.SysFont("consolas", 25)
texto = fuente.render("Hola 1c", False, VERDE, AZUL_CLARO)

circulos = []

for i in range(50):
    x = random.randint(1, ANCHO_VENTANA -1)
    y = random.randint(1, ALTO_VENTANA -1)
    circulos.append([x,y])

reloj = pygame.time.Clock()

while flag:
    tiempo = reloj.tick(60)
    VENTANA.fill(NEGRO)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    
    # VENTANA.blit(texto, (0,0))
    for c in circulos:
        c[0] += 1
        c[1] += 2 
        if c[0] > ANCHO_VENTANA:
            c[0] = 0
        if c[1] > ALTO_VENTANA:
            c[1] = 0
    for c in circulos:
        pygame.draw.circle(VENTANA, ROJO, (c[0], c[1]),5 ,10)
    
    pygame.display.update()
    # pygame.time.delay() esto es para que vaya mas lento 

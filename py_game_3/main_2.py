import pygame
import sys
from configuraciones import *

###################################FUNCIONES DE MOVIMIENTO#######################################

def mover_rectangulo(rectangulo_personaje : pygame.rect, velocidad):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos
    
    largo = len(accion_personaje)
    if contador_pasos >= largo: 
        contador_pasos = 0
    
    pantalla.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos += 1



def actualizar_pantalla(pantalla, que_hace, rectangulo_personaje, velocidad):

    match que_hace:
        case "Derecha":
            animar_personaje(pantalla,rectangulo_personaje, velocidad, personaje_camina)
            mover_rectangulo(rectangulo_personaje, velocidad)
        case "Izquierda":
            animar_personaje(pantalla,rectangulo_personaje, velocidad, personaje_camina_izquierda)
            mover_rectangulo(rectangulo_personaje, velocidad)
        case "Quieto":
            pass


#################################################################################################

W, H = 1900, 900 
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((W, H))

#FONDO 
fondo = pygame.image.load("Recursos/fondo_space.png")
fondo = pygame.transform.scale(fondo, (W,H))


#PERSONAJE
x_inicial = H/2 - 400
y_inicial = 750
contador_pasos = 0 
velocidad = 10

rectangulo_personaje = personaje_camina[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

posicion_actual_x = 0 

que_hace = "Quieto"

while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys= pygame.key.get_pressed()
    
    if(keys[pygame.K_RIGHT]):
        que_hace = "Derecha"
    elif(keys[pygame.K_LEFT]):
        que_hace = "Izquierda"
    else:
        que_hace = "Quieto"
    
    PANTALLA.blit(fondo,(0,0))
    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad)

    pygame.display.update()
import pygame
import sys
from configuraciones import *
from modo import *

###################################FUNCIONES DE MOVIMIENTO#######################################
def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, piso: pygame.Rect):
    global desplazamiento_y
    global esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje,personaje_animacion)

        rectangulo_personaje.y += desplazamiento_y
        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y = desplazamiento_y + gravedad
        if rectangulo_personaje.colliderect(piso):
            esta_saltando = False
            desplazamiento_y = 0 
            rectangulo_personaje.bottom = piso.top

def mover_rectangulo(rectangulo_personaje : pygame.rect, velocidad):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos
    
    largo = len(accion_personaje)
    if contador_pasos >= largo: 
        contador_pasos = 0
    
    pantalla.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos += 1



def actualizar_pantalla(pantalla, que_hace, rectangulo_personaje, velocidad, piso):
    global desplazamiento_y
    match que_hace:
        case "Derecha":
            animar_personaje(pantalla,rectangulo_personaje, velocidad, personaje_camina)
            mover_rectangulo(rectangulo_personaje, velocidad)
        case "Izquierda":
            animar_personaje(pantalla,rectangulo_personaje, velocidad, personaje_camina_izquierda)
            mover_rectangulo(rectangulo_personaje, velocidad)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
        case "Quieto":
            animar_personaje(pantalla,rectangulo_personaje,personaje_quieto)
    aplicar_gravedad(pantalla,personaje_salta,rectangulo_personaje,piso)


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
y_inicial = 650
contador_pasos = 0 
velocidad = 10


posicion_actual_x = 0 

lista_animaciones = [personaje_camina,personaje_camina_izquierda,personaje_quieto,personaje_salta]

reescalar_imagen(lista_animaciones, 75, 85)

rectangulo_personaje = personaje_camina[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

#SALTO

gravedad = 1 
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

#SUPERFICIE 

piso = pygame.Rect(0, 0, W, 20)
piso.top = rectangulo_personaje.bottom

que_hace = "Quieto"

while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.K_DOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()


    keys= pygame.key.get_pressed()
    
    if(keys[pygame.K_RIGHT]):
        que_hace = "Derecha"
    elif(keys[pygame.K_LEFT]):
        que_hace = "Izquierda"
    elif(keys[pygame.K_UP]):
        que_hace = "Salta"
    else:
        que_hace = "Quieto"
    
    PANTALLA.blit(fondo,(0,0))
    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad, piso)
    
    if get_modo():
        pygame.draw.rect(PANTALLA,"Blue", rectangulo_personaje,2)
        pygame.draw.rect(PANTALLA,"Green", piso, 2)


    pygame.display.update()
import pygame
import sys
from configuraciones import *
from modo import *

###################################FUNCIONES DE MOVIMIENTO#######################################

def se_encuentra_con(rectangulo_personaje: pygame.Rect, otro_rectangulo: pygame.Rect):
    r1_izquierda = rectangulo_personaje.x
    r1_arriba = rectangulo_personaje.y
    r1_derecha = rectangulo_personaje.x + rectangulo_personaje.width
    r1_abajo = rectangulo_personaje.y + rectangulo_personaje.height
    r2_izquierda = otro_rectangulo.x
    r2_arriba = otro_rectangulo.y
    r2_derecha = otro_rectangulo.x + rectangulo_personaje.width
    r2_abajo = otro_rectangulo.y + rectangulo_personaje.height

    return r1_derecha > r2_izquierda and r1_izquierda < r2_derecha and r1_arriba < r2_abajo and r1_abajo > r2_arriba

def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 10, principal.top, 10, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
    diccionario["top"] = pygame.Rect(principal.left,principal.top, principal.width, 10)

    return diccionario

def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, pisos):
    global desplazamiento_y
    global esta_saltando
    
    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje["main"], personaje_animacion)

        for lados in rectangulo_personaje:
            rectangulo_personaje[lados].y += desplazamiento_y

        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y = desplazamiento_y + gravedad

    for plataforma in pisos:
        if se_encuentra_con(rectangulo_personaje,plataforma):
            esta_saltando = False
            desplazamiento_y = 0 
            rectangulo_personaje["main"].bottom = plataforma["main"].top + 1
            print("colisiono")
            break       
        else:
                esta_saltando = True

def mover_rectangulo(rectangulo_personaje : pygame.rect, velocidad):
    for lados in rectangulo_personaje:
        rectangulo_personaje[lados].x += velocidad


def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos
    
    largo = len(accion_personaje)
    if contador_pasos >= largo: 
        contador_pasos = 0
    
    pantalla.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos += 1



def actualizar_pantalla(pantalla, que_hace, lados_personaje, velocidad, plataformas):
    global desplazamiento_y, esta_saltando
    
    pantalla.blit(fondo,(0,0))
    pantalla.blit(plataforma,(rectangulo_plataforma.x, rectangulo_plataforma.y))
    
    match que_hace:
        case "Derecha":
            if not esta_saltando:
                animar_personaje(pantalla,lados_personaje["main"], personaje_camina)
            mover_rectangulo(lados_personaje, velocidad)
        case "Izquierda":
            if not esta_saltando:
                animar_personaje(pantalla,lados_personaje["main"], personaje_camina_izquierda)
            mover_rectangulo(lados_personaje, velocidad *-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
        case "Quieto":
            if not esta_saltando:
                animar_personaje(pantalla,lados_personaje["main"],personaje_quieto)
    aplicar_gravedad(pantalla,personaje_quieto,lados_personaje, plataformas)

#################################################################################################

W, H = 1200, 600 
FPS = 18


pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((W, H))

#FONDO 
fondo = pygame.image.load("Recursos/fondo_nivel_3.jpg")
fondo = pygame.transform.scale(fondo, (W,H))


#PERSONAJE
x_inicial = H/2 
y_inicial = 430
contador_pasos = 0 
velocidad = 10

que_hace = "Quieto"

posicion_actual_x = 0 

lista_animaciones = [personaje_camina, personaje_camina_izquierda, personaje_quieto]

reescalar_imagen(lista_animaciones, 75, 85)

rectangulo_personaje = personaje_camina[0].get_rect()
rectangulo_pies = pygame.Rect(314, 505, 30, 10)
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial


lados_personaje = obtener_rectangulos(rectangulo_personaje)

#SALTO

gravedad = 1 
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

#SUPERFICIE 

#PISO

piso = pygame.Rect(0, 0, W, 20)
piso.top = rectangulo_personaje.bottom

lados_piso = obtener_rectangulos(piso)

#PLATAFORMA

plataforma = pygame.image.load("Recursos/0.png")
plataforma = pygame.transform.scale(plataforma, (75,50))
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = 600
rectangulo_plataforma.y = 450

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

lista_plataforma = [piso, rectangulo_plataforma]

while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        if evento.type == pygame.MOUSEBUTTONDOWN:  # Verifica si se ha realizado un clic del mouse
            if evento.button == 1:  # Verifica si se ha hecho clic con el botón izquierdo del mouse
                x_clic, y_clic = evento.pos  # Obtiene las coordenadas del clic
                print(f"Se hizo clic en las coordenadas ({x_clic}, {y_clic})")

    keys= pygame.key.get_pressed()
    
    if(keys[pygame.K_RIGHT] and rectangulo_personaje.right < W - velocidad):
        que_hace = "Derecha"
    elif(keys[pygame.K_LEFT]):
        que_hace = "Izquierda"
    elif(keys[pygame.K_UP]):
        que_hace = "Salta"
    else:
        que_hace = "Quieto"
    
    
    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(plataforma,(rectangulo_plataforma.x,rectangulo_plataforma.y))
    
    actualizar_pantalla(PANTALLA, que_hace, lados_personaje, velocidad, lista_plataforma)
    
    if get_modo():
        for lados in lados_personaje:
            pygame.draw.rect(PANTALLA, "Red", lados_personaje[lados],2)
        for lados in lados_piso:
            pygame.draw.rect(PANTALLA, "Blue", lados_piso[lados],2)
        for lados in lados_plataforma:
            pygame.draw.rect(PANTALLA, "Black", lados_plataforma[lados],2)


    pygame.display.update()

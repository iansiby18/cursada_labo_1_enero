import pygame
import random
from donas import *

#TAMAÑO HOMERO
WIDTH = 200
HEIGHT = 200 

TAMAÑO_PANTALLA = (800, 800)
FPS = 120  

#CONSTANTES BOCA HOMERO
x = 493
y = 658
z = 40

score = 0
flag = True
pygame.init()
RELOJ = pygame.time.Clock()

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 100) 

#CONFIGURACIONES
screen = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("HOMER DONUTS")
icono = pygame.image.load("ico.png")
pygame.display.set_icon(icono)
#FONDO
fondo = pygame.image.load("fondo.png")
fondo_final = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

#MUSICA
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("musica.mp3")
sonido_fondo.set_volume(0.1)
sonido_fondo.play(-1)

#FUENTE
fuente = pygame.font.SysFont("helvetica",50)
#HOMERO
imagen_homero = pygame.image.load("derecha.png")
imagen_homero = pygame.transform.scale(imagen_homero, (WIDTH, HEIGHT))
rectangulo_homero = imagen_homero.get_rect()
rectangulo_homero.x = 400
rectangulo_homero.y = 570
# rectangulo_homero.width = 200
# rectangulo_homero.height = 200 
rectangulo_boca = pygame.Rect(x, y, z, z)

personaje = {"superficie": imagen_homero, "rectangulo": rectangulo_homero,
             "rectangulo_boca": rectangulo_boca, "puntaje": score}

#DONAS 
lista_donas = crear_lista_donas(5)

while flag:
    RELOJ.tick(FPS)
    #EVENTOS    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.USEREVENT:
            if evento.type == tick:
                update(lista_donas)
    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT]:
        imagen_homero = pygame.image.load("izquierda.png")
        imagen_homero = pygame.transform.scale(imagen_homero, (WIDTH, HEIGHT))
        screen.blit(imagen_homero,rectangulo_homero)
        nueva_x = rectangulo_homero.x + -10
        if nueva_x > 0 and nueva_x < 600:
            rectangulo_homero.x = rectangulo_homero.x + -10 
            rectangulo_boca.x = rectangulo_boca.x + -10
    if lista_teclas[pygame.K_RIGHT]:
        imagen_homero = pygame.image.load("derecha.png")
        imagen_homero = pygame.transform.scale(imagen_homero, (WIDTH, HEIGHT))
        screen.blit(imagen_homero,rectangulo_homero)
        nueva_x = rectangulo_homero.x + 10
        if nueva_x > 0 and nueva_x < 600:
            rectangulo_homero.x = rectangulo_homero.x + 10 
            rectangulo_boca.x = rectangulo_boca.x + 10

    screen.blit(fondo_final, (0,0))
    screen.blit(imagen_homero,rectangulo_homero)

    for dona in lista_donas:
        screen.blit(dona["superficie"], dona["rectangulo"])


    actualizar_pantalla(lista_donas,personaje,screen)
    puntaje = fuente.render("Score: {0}".format(personaje["puntaje"]),True, (255,0,0))
    screen.blit(puntaje, (0,0))

    pygame.draw.rect(screen,(255,0,0), rectangulo_boca, 2)
    pygame.display.update()
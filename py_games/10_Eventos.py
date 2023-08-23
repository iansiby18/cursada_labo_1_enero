import pygame

ANCHO_VENTANA = 600
ALTO_VENTANA = 600
flag = True

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Prueba de eventos") #nombre para cuando se abre la ventana del juego

while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas [pygame.K_0]:
        print("0")
    if lista_teclas [pygame.K_LEFT]:
        print("Izquierda")
    if lista_teclas [pygame.K_RIGHT]:
        print("Derecha")
    if lista_teclas [pygame.K_ESCAPE]:
        flag = False
    pygame.display.update()
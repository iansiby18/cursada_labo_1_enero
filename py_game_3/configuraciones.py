import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada

def reescalar_imagen(lista_animaciones, W, H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, (W,H))

personaje_quieto = [
    pygame.image.load("Recursos/Quieto/4.png"),
    pygame.image.load("Recursos/Quieto/5.png"),
    pygame.image.load("Recursos/Quieto/5.png"),
    pygame.image.load("Recursos/Quieto/7.png"),
]

personaje_camina = [
    pygame.image.load("Recursos/Camina/Adelante/0.png"),
    pygame.image.load("Recursos/Camina/Adelante/1.png"),
    pygame.image.load("Recursos/Camina/Adelante/2.png"),
    pygame.image.load("Recursos/Camina/Adelante/3.png"),
    pygame.image.load("Recursos/Camina/Adelante/5.png"),
]

personaje_salta = [
    pygame.image.load("Recursos/Salta/0.png")
]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
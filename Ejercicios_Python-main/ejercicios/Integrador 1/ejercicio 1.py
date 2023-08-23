
from data import lista_personajes
from os import system

def mostrar_super_heroes():
    print("Los Super Heroes son: ")
    for super_heroe in lista_personajes:
        print(super_heroe['nombre'])

def mostrar_nombre_y_altura():
    print("El nombre del super heroe y la estura es:")
    for super_heroe in lista_personajes:
        print(f"{super_heroe['nombre']} - {float(super_heroe['altura']):.1f}")

def mostrar_super_heroe_mas_alto():
    
    bandera_mas_alto = False
    altura_mas_alto = 0
    
    print("El super heroe mas alto es: ")
    
    for super_heroe in lista_personajes :
        if float(super_heroe["altura"]) > altura_mas_alto or bandera_mas_alto == False:
            bandera_mas_alto = True
            altura_mas_alto = float(super_heroe["altura"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["altura"]) == altura_mas_alto:
            print(super_heroe["nombre"])

def mostrar_super_heroe_mas_bajo():

    bandera_mas_bajo = False
    altura_mas_bajo = 0
    
    print("El super heroe mas bajo es: ")
    
    for super_heroe in lista_personajes :
        if float(super_heroe["altura"]) < altura_mas_bajo or bandera_mas_bajo == False:
            bandera_mas_bajo = True
            altura_mas_bajo = float(super_heroe["altura"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["altura"]) == altura_mas_bajo:
            print(super_heroe["nombre"])

def mostrar_promedio_de_altura():
    contador_super_heroes = 0 
    promedio_altura_super_heroe = 0 
    acumulador_altura = 0

    for super_heroe in lista_personajes:
        contador_super_heroes += 1
        acumulador_altura += float(super_heroe['altura'])
    
    promedio_altura_super_heroe = acumulador_altura/contador_super_heroes
    print(f"El promedio de altura es: {promedio_altura_super_heroe:.1f}")

def mostrar_super_heroe_mas_pesado():
    
    bandera_mas_pesado = False
    peso_mas_grande = 0
    
    print("El super heroe mas pesado es: ")
    
    for super_heroe in lista_personajes :
        if float(super_heroe["peso"]) > peso_mas_grande or bandera_mas_pesado == False:
            bandera_mas_pesado = True
            peso_mas_grande = float(super_heroe["peso"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["peso"]) == peso_mas_grande:
            print(super_heroe["nombre"])

def mostrar_super_heroe_mas_liviano():
    
    bandera_mas_liviano = False
    peso_mas_bajo = 0
    
    print("El super heroe mas liviano es: ")
    
    for super_heroe in lista_personajes :
        if float(super_heroe["peso"]) < peso_mas_bajo or bandera_mas_liviano == False:
            bandera_mas_liviano = True
            peso_mas_bajo = float(super_heroe["peso"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["peso"]) == peso_mas_bajo:
            print(super_heroe["nombre"])

system("cls")

while True:
    respuesta = int(input("""
    1. Mostrar super heroes
    2. Mostrar super heroes con su altura
    3. Mostrar promedio de altura
    4. Mostrar super heroes mas altos
    5. Mostrar super heroes mas bajos
    6. Mostrar super heroes mas pesados
    7. Mostrar super heroes mas livianos 
    8. Salir
    """))
    match respuesta:
        case 1:
            mostrar_super_heroes()
        case 2: 
            mostrar_nombre_y_altura()
        case 3:
            mostrar_promedio_de_altura()
        case 4:
            mostrar_super_heroe_mas_alto()
        case 5:
            mostrar_super_heroe_mas_bajo()
        case 6:
            mostrar_super_heroe_mas_pesado()
        case 7: 
            mostrar_super_heroe_mas_liviano()
        case 8:
            break


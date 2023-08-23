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

def buscar_super_heroes_masculinos():
    list_super_heroes_masculinos =[]
    for super_heroe in lista_personajes:
        if super_heroe["genero"] == 'M':
            nombre_super_heroe = super_heroe['nombre']
            list_super_heroes_masculinos.append(nombre_super_heroe)
    
    return list_super_heroes_masculinos

def buscar_super_heroes_femeninos():
    list_super_heroes_femeninos =[]
    for super_heroe in lista_personajes:
        if super_heroe["genero"] == 'F':
            nombre_super_heroe = super_heroe["nombre"]
            list_super_heroes_femeninos.append(nombre_super_heroe)
    
    return list_super_heroes_femeninos

def buscar_super_heroe_mas_alto_masculino():
    
    bandera_mas_alto = False
    heroe_mas_alto = 0
    
    for super_heroe in lista_personajes :
        if super_heroe["genero"] == "M" and float(super_heroe["altura"]) > heroe_mas_alto or bandera_mas_alto == False:
            bandera_mas_alto = True
            heroe_mas_alto = float(super_heroe["altura"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["altura"]) == heroe_mas_alto:
            super_heroe_mas_alto_masculino = super_heroe['nombre']
    return super_heroe_mas_alto_masculino

def buscar_super_heroe_mas_alto_femenino():
    
    bandera_mas_alto = False
    heroe_mas_alto = 0
    
    for super_heroe in lista_personajes :
        if super_heroe["genero"] == "F" and float(super_heroe["altura"]) > heroe_mas_alto or bandera_mas_alto == False:
            bandera_mas_alto = True
            heroe_mas_alto = float(super_heroe["altura"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["altura"]) == heroe_mas_alto:
            super_heroe_mas_alto_femenino = super_heroe['nombre']
    return super_heroe_mas_alto_femenino

def buscar_super_heroe_mas_bajo_femenino():
    
    bandera_mas_bajo = False
    heroe_mas_bajo = 0
    
    for super_heroe in lista_personajes :
        if super_heroe["genero"] == "F" and float(super_heroe["altura"]) < heroe_mas_bajo or bandera_mas_bajo == False:
            bandera_mas_bajo = True
            heroe_mas_bajo = float(super_heroe["altura"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["altura"]) == heroe_mas_bajo:
            super_heroe_mas_bajo_femenino = super_heroe['nombre']
    return super_heroe_mas_bajo_femenino

def buscar_super_heroe_mas_bajo_masculino():
    
    bandera_mas_bajo = False
    heroe_mas_bajo = 0
    
    for super_heroe in lista_personajes :
        if super_heroe["genero"] == "M" and float(super_heroe["altura"]) < heroe_mas_bajo or bandera_mas_bajo == False:
            bandera_mas_bajo = True
            heroe_mas_bajo = float(super_heroe["altura"])
    
    for super_heroe in lista_personajes:
        if float(super_heroe["altura"]) == heroe_mas_bajo:
            super_heroe_mas_bajo_masculino = super_heroe['nombre']
    return super_heroe_mas_bajo_masculino

def calcular_promedio_altura_masculinos():
    
    acumulador_altura = 0 
    contador_super_heroes_masculinos = 0 

    for super_heroe in lista_personajes:
        if super_heroe['genero'] == "M":
            contador_super_heroes_masculinos += 1
            acumulador_altura += float(super_heroe["altura"])
    promedio_altura_heroes_masculinos = acumulador_altura / contador_super_heroes_masculinos

    return promedio_altura_heroes_masculinos

def calcular_promedio_altura_femeninos():
    
    acumulador_altura = 0 
    contador_super_heroes_femenino = 0 

    for super_heroe in lista_personajes:
        if super_heroe['genero'] == "F":
            contador_super_heroes_femenino += 1
            acumulador_altura += float(super_heroe["altura"])
    promedio_altura_heroes_femenino = acumulador_altura / contador_super_heroes_femenino

    return promedio_altura_heroes_femenino

def contar_color_ojos():
    dic = {}
    for super_heroe in lista_personajes:
        if super_heroe['color_ojos'] in dic:
            dic[super_heroe['color_ojos']] += 1
        else:
            dic[super_heroe['color_ojos']] = 1

    return dic

def contar_color_pelo():
    dic = {}
    for super_heroe in lista_personajes:
        if super_heroe['color_pelo'] in dic:
            dic[super_heroe['color_pelo']] += 1
        else:
            dic[super_heroe['color_pelo']] = 1

    return dic

def contar_inteligencias():
    dic = {}
    for super_heroe in lista_personajes:
        if super_heroe["inteligencia"] == "":
            super_heroe["inteligencia"] = "No Tiene"
            
        if super_heroe['inteligencia'] in dic:
            dic[super_heroe['inteligencia']] += 1
        else:
            dic[super_heroe['inteligencia']] = 1

    return dic

def agrupar_por_color_de_ojos():
    dic = {}
    
    for super_heroe in lista_personajes:
        color_ojos = super_heroe['color_ojos']
        nombre = super_heroe["nombre"]
        
        if color_ojos in dic:
            dic[color_ojos].append(nombre)
        else:
            dic[color_ojos] = [nombre]

    return dic

def agrupar_por_color_de_pelos():
    dic = {}
    
    for super_heroe in lista_personajes:
        color_pelos = super_heroe['color_pelo']
        nombre = super_heroe["nombre"]
        
        if color_pelos in dic:
            dic[color_pelos].append(nombre)
        else:
            dic[color_pelos] = [nombre]

    return dic

def agrupar_por_inteligencia():
    dic = {}
    
    for super_heroe in lista_personajes:
        if super_heroe["inteligencia"] == "":
            super_heroe["inteligencia"] = "No Tiene"
        inteligencia = super_heroe['inteligencia']
        nombre = super_heroe["nombre"]
        
        if inteligencia in dic:
            dic[inteligencia].append(nombre)
        else:
            dic[inteligencia] = [nombre]

    return dic


system("cls")

while True:
    respuesta = int(input("""
    1 . Mostrar nombre de superheroes (general)
    2 . Mostrar nombre de superheroes con su altura (general)
    3 . Mostrar promedio de altura (general)
    4 . Mostrar nombre de superheroes mas altos (general)
    5 . Mostrar nombre de superheroes mas bajos (general)
    6 . Mostrar nombre de superheroes mas pesados (general)
    7 . Mostrar nombres de superheroes mas livianos (general)
    8 . Mostrar nombres de superheroes 
    9 . Mostrar nombres de las superheroinas
    10. Mostrar nombres de los superheroes mas alto 
    11. Mostrar nombres de las superheroinas mas altas  
    12. Mostrar nombre de los superheroes mas bajos 
    13. Mostrar nombre de las superheroinas mas bajas 
    14. Mostrar promedio de altura de los heroes
    15. Mostrar promedio de altura de las heroinas 
    16. Mostrar listado de color de ojos y la cantidad de cada uno 
    17. Mostrar listado de color de pelo y la cantidad de cada uno  
    18. Mostrar el listado de inteligencia y la cantidad de cada uno 
    19. Listar superheroes agrupados por color de ojos
    20. Listar superheroes agrupados por color de pelo 
    21. Listar superheroes agrupados por inteligencia
    22. Salir
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
            lista_super_heroes_masculinos = buscar_super_heroes_masculinos()
            print("Los superheroes son:")
            for nombre_masculino in lista_super_heroes_masculinos:
                print(nombre_masculino)
        case 9:
            lista_super_heroes_femeninos = buscar_super_heroes_femeninos()
            print("Las superheroinas son: ")
            for nombre_femenino in lista_super_heroes_femeninos:
                print(nombre_femenino)
        case 10:
            super_heroe_alto_masculino = buscar_super_heroe_mas_alto_masculino ()
            print(f"Los superheroes mas altos son: {super_heroe_alto_masculino}")
        case 11:
            super_heroe_alto_femenino = buscar_super_heroe_mas_alto_femenino ()
            print(f"Las superheroinas mas altas son: {super_heroe_alto_femenino}")
        case 12:
            super_heroe_bajo_masculino = buscar_super_heroe_mas_bajo_masculino()
            print("Los superheroes mas bajos son: {super_heroe_bajo_masculino}")
        case 13:
            super_heroe_bajo_femenino = buscar_super_heroe_mas_bajo_femenino()
            print("Las superheroinas mas bajas son: {super_heroe_bajo_femenino}")
        case 14:
            promedio_altura_masculino = calcular_promedio_altura_masculinos()
            print("El promedio de altura de los "
                f"superheroes es: {promedio_altura_masculino:.1f}")
        case 15:
            promedio_altura_femenino = calcular_promedio_altura_femeninos()
            print("El promedio de altura de las "
                f"superheroinas es: {promedio_altura_femenino:.1f}")
        case 16:
            numero_por_cada_ojo = contar_color_ojos()
            print("El listado de colores de ojos con su cantidad es: ")
            for color, numero in numero_por_cada_ojo.items():
                print(f"{color} {numero}")
        case 17: 
            numero_por_cada_pelo = contar_color_pelo()
            print("El listado de colores de pelo con su cantidad es: ")
            for color, numero in numero_por_cada_pelo.items():
                print(f"{color} {numero}")
        case 18:
            numero_por_inteligencia = contar_inteligencias()
            print("El listado de inteligencia con su cantidad es: ")
            for inteligencia, numero in numero_por_inteligencia.items():
                print(f"{inteligencia} {numero}")
        case 19:
            nombre_heroe_y_color_ojo = agrupar_por_color_de_ojos()
            print("Los nombres de los superheroes agrupados por "
                "su color de ojos son: ")
            for color, nombre in nombre_heroe_y_color_ojo.items():
                print(f"{color} : {nombre}")   
        case 20:
            nombre_heroe_y_color_pelo = agrupar_por_color_de_pelos()
            print("Los nombres de los superheroes agrupados por "
                "su color de pelo son: ")
            for color, nombre in nombre_heroe_y_color_pelo.items():
                print(f"{color} : {nombre}")      
        case 21:
            nombre_heroe_inteligencia = agrupar_por_inteligencia()
            print("Los nombres de los superheroes agrupados por "
                "su inteligencia son: ")
            for inteligencia, nombre in nombre_heroe_inteligencia.items():
                print(f"{inteligencia} : {nombre}")  
        case 22:
            break


from data import lista_bzrp
from os import system

def mostrar_canciones():
    print("Las canciones son: ")
    for cancion in lista_bzrp:
        print(cancion['title'])

def mostrar_temas_mas_vistos():

    maximo_reproducciones = 0
    bandera_primer_tema = False

    print(f"Las canciones con mas reproduciciones son: ")
    for cancion in lista_bzrp:
        if cancion["views"] > maximo_reproducciones or bandera_primer_tema == False:
            bandera_primer_tema = True
            maximo_reproducciones = cancion["views"]
    for cancion in lista_bzrp:
        if cancion["views"] == maximo_reproducciones:
            print(cancion["title"])

def mostrar_temas_menos_vistos():
    minimo_reproducciones = 0
    bandera_primer_tema = False

    print(f"Las canciones con menos reproduciciones son: ")
    for cancion in lista_bzrp:
        if cancion["views"] < minimo_reproducciones or bandera_primer_tema == False:
            bandera_primer_tema = True
            minimo_reproducciones = cancion["views"]
    for cancion in lista_bzrp:
        if cancion["views"] == minimo_reproducciones:
            print(cancion["title"])

def mostrar_suma_reproducciones():
    acumulador_reproducciones = 0

    for cancion in lista_bzrp:
        acumulador_reproducciones += cancion["views"]
    print(f"El total de todas las reproducciones es: {acumulador_reproducciones}")

def mostrar_promedio_reproducciones():
    acumulador_reproducciones = 0
    contador_canciones = 0

    for cancion in lista_bzrp:
        acumulador_reproducciones += cancion["views"]
        contador_canciones += 1
    promedio_reproducciones = acumulador_reproducciones / contador_canciones
    print(f"El promedio de reproducciones es: {promedio_reproducciones:.2f}")

def mostrar_cancion_mas_larga():

    bandera_cancion_mas_larga = False
    cancion_mas_larga = 0

    for cancion in lista_bzrp:
        if int(cancion["length"]) > cancion_mas_larga or bandera_cancion_mas_larga == False:
            bandera_cancion_mas_larga = True
            cancion_mas_larga = cancion['length']

    for cancion in lista_bzrp:
        if cancion["length"] == cancion_mas_larga:
            print(f"La cancion mas larga es: {cancion['title']}") 

def mostrar_cancion_mas_corta():

    bandera_cancion_mas_corta = False
    cancion_mas_corta = 0

    for cancion in lista_bzrp:
        if int(cancion["length"]) < cancion_mas_corta or bandera_cancion_mas_corta == False:
            bandera_cancion_mas_corta = True
            cancion_mas_corta = cancion['length']

    for cancion in lista_bzrp:
        if cancion["length"] == cancion_mas_corta:
            print(f"La cancion mas corta es: {cancion['title']}") 
system("cls")

while True:
    respuesta = int(input("""
    1. Mostrar lista de canciones
    2. Mostrar temas mas vistos 
    3. Mostrar temas menos vistos
    4. Mostrar suma de reproducciones
    5. Mostrar promedio de reproducciones 
    6. Mostrar cancion mas larga
    7. Mostrar cancion mas corta
    8. Salir
    """))
    match respuesta:
        case 1:
            mostrar_canciones()
        case 2: 
            mostrar_temas_mas_vistos()
        case 3:
            mostrar_temas_menos_vistos()
        case 4:
            mostrar_suma_reproducciones()
        case 5:
            mostrar_promedio_reproducciones()
        case 6:
            mostrar_cancion_mas_larga()
        case 7:
            mostrar_cancion_mas_corta()
        case 8:
            break

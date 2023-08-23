import re
import json
from os import system



def traer_datos(path):

    """
    brief: Abre el archivo, lo separa en partes y asigna las partes 
    a una lista de diccionarios
    parameters: path: la direccion del archivo 
    return: Retorna una lista con los diccionarios de los pokemones 
    """

    archivo = open(path, "r", encoding= "utf-8")
    lectura = archivo.readlines()
    pokemones = [] 
    lectura.pop(0)
    for linea in lectura:
        pokemon = {}
        personaje = linea.split(",")
        pokemon["id"] = int(personaje[0])
        pokemon["nombre"] = personaje[1]
        pokemon["tipo"] = personaje[2].split("/")
        pokemon["poder_ataque"] = int(personaje[3])
        pokemon["poder_defensa"] = int(personaje[4])
        pokemon["habilidades"] = re.findall("[^|*$|\n]+", personaje[5])
        pokemones.append(pokemon)
    return pokemones

def contar_cada_tipo(lista: list):
    
    """
    brief: crea un diccionario con los tipos y le asigna la cantidad
    de pokemones que hay de cada uno  
    parameters: lista: lista con los diccionarios de cada pokemon 
    return: Retorna un diccionario con los tipos de pokemon y la
    cantidad de cada uno 
    """

    contador_tipo = {}
    for pokemon in lista:
        for tipo in pokemon["tipo"]:
            if tipo in contador_tipo:
                contador_tipo[tipo] += 1
            else:
                contador_tipo[tipo] = 1
    return contador_tipo

def listar_tipo_y_cantidad(lista: list):

    """
    brief: muestra los tipos de pokemones con la cantidad de cada uno 
    parameters: lista: lista con los diccionarios de cada pokemon 
    return:
    """
    
    tipo_y_cantidad = contar_cada_tipo(lista)

    print("Los tipos de pokemones y sus cantidades son: ")
    for key in tipo_y_cantidad:  
        print(f"{key} : {tipo_y_cantidad[key]}")

def listar_tipo_y_nombre(lista: list):

    """
    brief: muestra los tipos de pokemones con la cantidad de cada uno 
    parameters: lista: lista con los diccionarios de cada pokemon 
    """
    
    tipos = []
    for pokemon in lista:
        for tipo in pokemon['tipo']:
            if tipo not in tipos:
                tipos.append(tipo)
    
    for tipo in tipos:
        print(f"--------------------{tipo}--------------------")
        for pokemon in lista:
            if tipo in pokemon['tipo']:
                print(f"Nombre: {pokemon['nombre']:<12}"
                      f"Poder de ataque: {pokemon['poder_ataque']}")

def listar_pokemones_por_habilidad(lista: list, descripcion: str):
    
    """
    brief: muestra los nombres, tipos y el promedio de poderes de los
    pokemones que tienen una habilidad especifica  
    parameters: lista: lista con los diccionarios de cada pokemon 
    return:
    """

    descripcion = descripcion.capitalize()
    pokemon_con_descripcion = []
    
    for pokemon in lista:
        if descripcion in pokemon["habilidades"]:
            promedio_poderes = (int(pokemon["poder_ataque"]) + 
                                int(pokemon["poder_defensa"]))/2
            pokemon_con_descripcion.append((pokemon["nombre"], 
                                            pokemon["tipo"], promedio_poderes))
    
    for pokemon in pokemon_con_descripcion:
        print(f"Nombre: {pokemon[0]}", end= " ")
        if len(pokemon[1]) > 1:
            print(f", tipos: {pokemon[1][0]}, "
                  f"{pokemon[1][1]}", end= " ")
        else:
            print(f", tipo: {pokemon[1][0]}", end= " ")
        print(f"y el promedio de poderes es: {pokemon[2]}")

def ordenar_por_poder_o_nombre(lista: list):

    """
    brief: ordena los pokemones por su punto de ataque, en caso que 
    sean iguales, los ordena por orden alfabetico de la A a la Z  
    parameters: lista: lista con los diccionarios de cada pokemon 
    return:
    """

    n = len(lista)

    for i in range(n-1):
        for j in range(i+1,n):
            if lista[i]['poder_ataque'] > lista[j]['poder_ataque'] or(
                lista[i]['poder_ataque'] == lista[j]['poder_ataque'] and 
                lista[i]['nombre'] > lista[j]['nombre']):
                lista[i], lista[j] = lista[j], lista[i]
    for pokemon in lista:
        print(f"ID pokedex: {pokemon['id']}")
        print(f"Nombre: {pokemon['nombre']}")
        if len(pokemon["tipo"]) > 1:
            print(f"Tipos: {pokemon['tipo'][0]}, {pokemon['tipo'][1]}")
        else:
            print(f"Tipo: {pokemon['tipo'][0]}")
        print(f"Poder de ataque: {pokemon['poder_ataque']}")
        print(f"Poder de defensa: {pokemon['poder_defensa']}")
        if len(pokemon["habilidades"]) > 1:
            print(f"Habilidades: {pokemon['habilidades'][0]}, "
                  f"{pokemon['habilidades'][1]}")
        else:
            print(f"Habilidad: {pokemon['habilidades'][0]}")
        print("--------------------------------------------------------")

import json

def crear_json(lista:list, descripcion: str):

    """
    brief: Crea un JSON con los pokemones de un tipo particular 
    parameters: lista: lista con los diccionarios de cada pokemon
                descripcion: tipo para que guarde los pokemones de 
                este mismo en el JSON que se va a crear  
    return: devuelve el tipo del pokemon ingresado
    """

    nombre_lista = descripcion.capitalize()
    descripcion = descripcion.capitalize()
    pokemon = {nombre_lista: []}
    for personaje in lista:
        if descripcion in personaje["tipo"]:
            pokemon_filtrado = {}
            pokemon_filtrado["nombre"] = personaje["nombre"]
            if personaje["poder_ataque"] > personaje["poder_defensa"]:
                pokemon_filtrado["n_poder"] = personaje["poder_ataque"]
                pokemon_filtrado["poder"] = "Ataque"
            elif personaje["poder_defensa"] > personaje["poder_ataque"]:
                pokemon_filtrado["n_poder"] = personaje["poder_defensa"]
                pokemon_filtrado["poder"] = "Defensa"
            else:
                pokemon_filtrado["n_poder"] = personaje["poder_ataque"]
                pokemon_filtrado["poder"] = "Ambos"
            pokemon[nombre_lista].append(pokemon_filtrado)

    with open('pokemones.json', 'w') as file:
        json.dump(pokemon, file, indent=4, 
                  ensure_ascii=False, default=str)
    return descripcion

def leer_json(nombre_archivo, lista: list, descripcion: str):

    """
    brief: lee un JSON y imprime los valores 
    parameters: nombre_archivo: direccion del json
                lista: lista con los diccionarios de cada pokemon 
                descripcion: el tipo de pokemon que esta en el json 
    return:
    """

    tipo_de_pokemon = crear_json(lista, descripcion)
    with open(nombre_archivo, 'r') as archivo:
        pokemones = json.load(archivo)
        for pokemon in pokemones[tipo_de_pokemon]:
            print(f"{pokemon['nombre']} - {pokemon['n_poder']} - "
                  f"{pokemon['poder']}")
            

def mostrar_habilidades(lista: list):

    """
    brief: recorre todas las habilidades de los diccionarios de la 
    lista y los guarda en una lista nueva si es que no estan
    parameters: lista: lista con los diccionarios de cada pokemon 
    return: retorna una lista con las habilidades
    """

    habilidades = []
    for pokemon in lista:
        for habilidad in pokemon["habilidades"]:
            if habilidad not in habilidades:
                habilidades.append(habilidad)
    return habilidades

def mostrar_tipo(lista: list):

    """
    brief: recorre todas las habilidades de los diccionarios de la 
    lista y los guarda en una lista nueva si es que no estan
    parameters: lista: lista con los diccionarios de cada pokemon 
    return: retorna una lista con las habilidades
    """
    tipos = []
    for pokemon in lista:
        for tipo in pokemon["tipo"]:
            if tipo not in tipos:
                tipos.append(tipo)
    return tipos

def mostrar_menu():
    
    """
    brief: muestra el menu de opciones
    parameters: 
    return: 
    """

    print("""
    1.  Traer datos desde archivo
    2.  Listar cantidad por tipo
    3.  Listar pokemones por tipo
    4.  Listar pokemones por habilidad
    5.  Listar pokemones ordenados
    6.  Guardar Json
    7.  Leer Json
    8.  Crear nuevo pokemon 
    9.  Guardar Pokemon en el archivo CSV 
    10. Salir del programa
    """)

def menu_principal():
    
    """
    brief: Imprime el menu y pide una opcion
    parameters: 
    return: retorna la opcion ingresada por el usuario 
    """

    mostrar_menu()
    opcion = input("Ingrese una opcion:")
    opcion = opcion.lower()
    return opcion

def crear_pokemones(pokemones):
    contador = 0
    for pokemon in pokemones:
        contador = contador + 1
    
    id_pokemon = contador + 1
    nombre = input("Ingrese nombre: ")
    tipos = mostrar_tipo(pokemones)
    print(tipos)
    tipo_nuevo = []
    tipo = input("Ingrese el tipo de pokemon: ")
    tipo = tipo.strip()
    tipo = tipo.capitalize()
    while tipo not in tipos:
        tipo = input("Ingrese el tipo de pokemon: ")
        tipo = tipo.strip()
        tipo = tipo.capitalize()
    tipo_nuevo.append(tipo)
    poder_ataque = input("Ingrese el poder de ataque: ")
    if poder_ataque.isnumeric():
        poder_ataque = int(poder_ataque)
    while type(poder_ataque) == str:
        if poder_ataque.isnumeric():
            poder_ataque = int(poder_ataque)
        else: 
            poder_ataque = input("Error, ingrese un poder de ataque valido: ")
    while poder_ataque not in range(1,1000) :
        poder_ataque = int(input("Error: Ingrese el poder de ataque "
                                 "(entre 1 y 999): "))
    poder_defensa = input("Ingrese el poder de defensa: ")
    if poder_defensa.isnumeric():
        poder_defensa = int(poder_defensa)
    while type(poder_defensa) == str:
        if poder_defensa.isnumeric():
            poder_defensa = int(poder_defensa)
        else: 
            poder_defensa = input("Error, ingrese un poder de defensa valido: ")
    while poder_defensa not in range(1,1000) :
        poder_defensa = int(input("Error: Ingrese el poder de defensa "
                                 "(entre 1 y 999): "))
    habilidades = mostrar_habilidades(pokemones)
    print(habilidades)
    habilidad_nueva = []
    habilidad = input("Ingrese la habilidad del pokemon: ")
    habilidad = habilidad.strip()
    habilidad = habilidad.capitalize()
    while habilidad not in habilidades:
        habilidad = input("Error: Ingrese la habilidad del pokemon: ")
        habilidad = habilidad.strip()
        habilidad = habilidad.capitalize()
    habilidad_nueva.append(habilidad)
    pokemon = {}
    pokemon["id"] = id_pokemon
    pokemon["nombre"] = nombre
    pokemon["tipo"] = tipo_nuevo
    pokemon["poder_ataque"] = poder_ataque
    pokemon["poder_defensa"] = poder_defensa
    pokemon["habilidades"] = habilidad_nueva
    
    return pokemon

def guardar_csv(path, lista_pokemones: list):

    archivo = open(path, "w")
    for pokemon in lista_pokemones:
        archivo.write(pokemon)
    archivo.close()

def pokemon_menu(path):

    """
    brief: Gestiona el menu de opciones, llamando a todas las funciones
    segun la necesidad del usuario
    parameters: path: direccion donde esta el archivo csv 
    return:
    """
    # path = "pokemones.csv"
    flag_importar_csv = False
    flag_crear_json = False
    while True:
        opcion = menu_principal()
        while opcion not in ["1","2","3","4","5","6","7","8", "9", "10"]:
            opcion = menu_principal()
        match (opcion):
            case "1":
                pokemones= traer_datos(path)
                flag_importar_csv = True
                system("pause")
            case "2":
                if flag_importar_csv == True:
                    listar_tipo_y_cantidad(pokemones)
                else:
                    print("Primero ingresar a la opcion 1")
                system("pause")
            case "3":
                if flag_importar_csv == True:
                    listar_tipo_y_nombre(pokemones)
                else:
                    print("Primero ingresar a la opcion 1")
                system("pause")
            case "4":
                if flag_importar_csv == True:
                    descripciones = mostrar_habilidades(pokemones)
                    print(descripciones)
                    descripcion = input("ingrese una habilidad: ")
                    descripcion = descripcion.capitalize()
                    if descripcion in descripciones:
                        system("cls")
                        listar_pokemones_por_habilidad(pokemones, descripcion)
                    else: 
                        print("habilidad no encontrada! ")
                else:
                    print("Primero ingresar a la opcion 1")
                system("pause")
            case "5":
                if flag_importar_csv == True:
                    ordenar_por_poder_o_nombre(pokemones)
                else:
                    print("Primero ingresar a la opcion 1")
                system("pause")
            case "6":
                if flag_importar_csv == True:
                    descripciones = mostrar_tipo(pokemones)
                    print(descripciones)
                    descripcion = input("ingrese un tipo: ")
                    descripcion = descripcion.capitalize()
                    if descripcion in descripciones:
                        crear_json(pokemones, descripcion)
                        flag_crear_json = True
                else:
                    print("Primero ingresar a la opcion 1")
                system("pause")
            case "7":
                if flag_crear_json == True:
                    tipo_de_pokemon = crear_json(pokemones,descripcion)
                    leer_json("pokemones.json",pokemones,tipo_de_pokemon)
                else:
                    print("Primero ingresar a la opcion 6")
                system("pause")
            case "8":
                if flag_importar_csv == True:
                    pokemon = crear_pokemones(pokemones) 
                    pokemones.append(pokemon)
                    print("Pokemon creado exitosamente! ")
                else:
                    print("Ingrese a la opcion 1! ")
                system("pause")
            case "9":
                if flag_importar_csv == True:
                    guardar_csv("csv_nuvo.csv", pokemones)
                else:
                    print("Ingrese a la opcion 1!")
            case "10":
                print("Gracias por usar el programa! ")
                break
        system("cls")
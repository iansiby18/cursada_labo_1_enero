

def stark_normalizar_datos(lista_personaje:list):
    
    """
    brief: si los datos no son del tipo que tiene que ser los normaliza
    parameters:
                lista_personajes: lista de heroes
    return: retorna false si no se modifico nada y true si se normalizo algun dato
    """
    bandera_modificacion = False
    if not lista_personaje:
        print("Error: Lista de héroes vacía")
    for heroe in lista_personaje:
        if not type(heroe["altura"] ) is float:
            heroe ["altura"] = float(heroe["altura"])
            bandera_modificacion = True
        if not type(heroe["peso"] ) is float:
            heroe ["peso"] = float(heroe["peso"])
            bandera_modificacion = True
        if not type(heroe["fuerza"] ) is int:
            heroe ["fuerza"] = int(heroe["fuerza"])
            bandera_modificacion = True
    return bandera_modificacion 




def obtener_nombre(heroe: dict):
    """
    brief: obtiene el nombre del heroe
    parameters:
                lista_personajes: lista de heroes
    return: retorna el nombre del heroe 
    """
    nombre_heroe = heroe["nombre"]
    return f"Nombre : {nombre_heroe}"

def imprimir_dato(dato: str):
    """
    brief: imprime un dato 
    parameters:
                dato: dato a imprimir
    """
    print(dato)

def stark_imprimir_nombres_heroes(lista_heroes: list):
    """
    brief: imprime la lista de heroes
    parameters:
                lista_personajes: lista de heroes
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    if not lista_heroes:
        return -1
    else:
        for heroe in lista_heroes:
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)
        return 0 

def obtener_nombre_y_dato(heroe: dict, key: str):
    """
    brief: obtiene un heroe y un dato del diccionario
    parameters:
                heroe: heroe del que vamos a obtener datos
                key: clave del heroe 
    return: retorna el nombre del heroe y la key 
    """
    nombre_heroe = obtener_nombre(heroe)
    valor_key = heroe[key]
    return f"{nombre_heroe} | {key} : {valor_key} "

def stark_imprimir_nombres_alturas(lista_heroe: list):
    """
    brief: imprime la lista de heroes con la altura de cada uno 
    parameters:
                lista_personajes: lista de heroes
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    if not lista_heroe:
        return -1
    else:
        for heroe in lista_heroe:
            print(obtener_nombre_y_dato(heroe, 'altura'))
        return 0

def calcular_max(lista_personajes: list, key: str):
    """
    brief:Calcular el maximo en una funcion en base a una clave
    parameters:
                lista_personajes: lista de heroes
                key: clave sobre la que voy a hacer la busqueda
    return: retorna el nombre del heroe con la clave maxima a comparar
    """
    bandera_maximo = False
    key_maximo = 0 
    for heroe in lista_personajes:
        if heroe[key] > key_maximo or bandera_maximo == False:
            bandera_maximo = True
            key_maximo = heroe[key]
    for heroe in lista_personajes:
        if heroe[key] == key_maximo:
            heroe_max = (heroe)
    return heroe_max

def calcular_min(lista_personajes: list, key: str):
    """
    brief:Calcular el minimo en una funcion en base a una clave
    parameters:
                lista_personajes: lista de heroes
                key: clave sobre la que voy a hacer la busqueda
    return: retorna el nombre del heroe con la clave minima a comparar
    """

    bandera_minimo = False
    key_minimo = 0 
    for heroe in lista_personajes:
        if heroe[key] < key_minimo or bandera_minimo == False:
            bandera_minimo = True
            key_minimo = heroe[key]
    for heroe in lista_personajes:
        if heroe[key] == key_minimo:
            heroe_min = (heroe)
    return heroe_min

def calcular_max_min_dato(lista: list,  comparador: str, key: str):
    """
    brief: calcula el maximo o minimo heroe segun la llave que reciba
    parameters:
                lista_personajes: lista de heroes
                comparador: minimo o maximo, segun lo que queramos comparar 
                key: clave de heroe 
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    if not lista:
        return -1
    else:
        if comparador.lower() == "maximo" :
            heroe = calcular_max(lista, key)
        elif comparador.lower() == "minimo":
            heroe = calcular_min(lista, key)
        return heroe

def stark_calcular_imprimir_heroe(lista: list, comparador: str, key: str):
    """
    brief: imprime el heroe con la mayor o menor clave 
    parameters:
                lista_personajes: lista de heroes
                comparador: minimo o maximo, segun lo que queramos comparar 
                key: clave de heroe 
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    if not lista:
        return -1 
    else:
        heroe = calcular_max_min_dato(lista,comparador,key)
        if heroe:
            nombre_y_dato = obtener_nombre_y_dato(heroe, key)
            if comparador.lower() == "maximo":
                imprimir_dato(f"Mayor {key}: {nombre_y_dato}")
            elif comparador.lower() == "minimo":
                imprimir_dato(f"Menor {key}: {nombre_y_dato}")
            return 0


def sumar_dato_heroe(lista: list, key: str):
    """
    brief: suma los valores de la clave 
    parameters:
                lista_personajes: lista de heroes 
                key: clave de heroe 
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    suma = 0
    for heroe in lista:
        if type(heroe) == dict :
            if key in heroe:
                suma += heroe[key]
    return suma

def dividir(dividendo, divisor):
    """
    brief: divide dos valores  
    parameters:
                divisor: numero a dividir
                dividendo: numero que divide al divisor 
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
        return resultado
    
def calcular_promedio(lista: list, key: str):
    """
    brief: calcula promedio de la llave 
    parameters:
                lista: lista de heroes 
                key: clave de heroe  
    return: retorna el promedio
    """
        
    cantidad_heroes = len(lista)
    suma_de_datos = sumar_dato_heroe(lista,key)
    resultado = suma_de_datos / cantidad_heroes
    return resultado

def stark_calcular_imprimir_promedio_altura(lista: list):
    """
    brief: calcula e imprime el promedio de altura de todo la lista  
    parameters:
                lista: lista de heroes 
    return: retorna -1 si no hay lista o 0 si hay lista
    """
    if not lista:
        return -1
    else: 
        altura_promedio = calcular_promedio(lista, 'altura')
        print(f"La altura promedio es: {altura_promedio:.1f}")
        return 0 

def imprimir_menu():
    """
    brief: imprime el menu   
    parameters: 
    return: retorna el menu 
    """
    menu = """
    1. Imprimir nombre de heroe
    2. Imprimir nombre y altura
    3. Imprimir nombre del heroe con el mayor o menor valor ingresado 
    4. Imprimir promedio de altura 
    5. Salir
    """
    return menu

def validar_entero(numero: str):
    """
    brief: valida enteros   
    parameters:
                numero: el numero a validar   
    return: true si es numero o si es string y lo combierte en numero, si no retorna false 
    """
    retorno = False

    if type(numero) == str:
        if numero.isdigit():
            retorno = True
    elif type(numero) == int:
        retorno = True
    return retorno

def stark_menu_principal():
    """
    brief: imprime el menu, pide una opcion y la valida   
    parameters:
    return: retorna la opcion si es un entero y esta en rango de opciones 
            o retorna -1 si la opcion es incorrecta o no es entero 
    """

    print(imprimir_menu())
    opcion = input("Ingrese una opcion: ")
    opcion = int(opcion)
    if validar_entero(opcion) == True and opcion >= 1 and opcion <= 5:
        opcion = int(opcion)
        return opcion
    else :
        return -1

def stark_marvel_app(lista : list):
    """
    brief: muesta el menu, pide la opcion y ejecuta el menu 
    parameters:
                lista: lista de heroes
    """
    if stark_normalizar_datos(lista) == False:
        pass
    else: 
        stark_normalizar_datos(lista)
        print("Datos Modificados")
    
    while True:
        opcion = stark_menu_principal()
        match(opcion):
            
            case 1:
                if stark_imprimir_nombres_heroes(lista) != 0:
                    print("No hay una lista")
            
            case 2:
                if stark_imprimir_nombres_alturas(lista) != 0:
                    print("No hay lista")
            
            case 3:
                comparador = input("Ingrese Maximo o Minimo para hacer la comparacion: ")
                while comparador != "maximo" and comparador != "minimo":
                    comparador = input("Ingrese Maximo o Minimo para hacer la comparacion: ")
                
                key = input("Ingrese el dato a comparar(Altura, Peso, Fuerza): ")
                key = key.lower()
                while key != "altura" and key != "fuerza" and key != "peso":
                    key = input("Ingrese el dato a comparar(Altura, Peso, Fuerza):")
                    key = key.lower()
                
                
                if stark_calcular_imprimir_heroe(lista,comparador, key) != 0:
                    print("No hay lista")
            case 4:
                if stark_calcular_imprimir_promedio_altura(lista) != 0:
                    print("No hay lista")

            case 5: 
                break
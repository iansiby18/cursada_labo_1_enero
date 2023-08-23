from os import system

def extraer_iniciales(nombre_heroe: str):
    
    """
    brief: extrae las iniciacles del nombre del heroe
    parameters:
                nombre_heroe: valor del nombre del heroe
    return: retorna las iniciales seguidas de un punto
    """

    iniciales = ""
    if not nombre_heroe:
        return "N/A"
    else:
        nombre = nombre_heroe.replace("-", " ")
        nombre = nombre.split(" ")
        if len(nombre) > 2:
            if "the" in nombre:
                nombre.remove("the")
        iniciales = ".".join([inicial[0].upper() for inicial in nombre])
        return iniciales + "."

def definir_iniciales_nombre(heroe: dict):

    """
    brief: crea en el diccionario la clave iniciales y le asigna kas iniciales
    parameters:
                heroe: diccionario de heroe 
    return: retorna false si no recibe un diccionario o no tiene la clave heroe
            y si pudo crear la clave y asignar valor devuelve true 
    """

    if type(heroe) != dict or "nombre" not in heroe:
        return False
    else:
        nombre = heroe["nombre"]
        iniciales = extraer_iniciales(nombre)
        heroe["iniciales"] = iniciales
        return True

def agregar_iniciales_nombre(lista: list):
    
    """
    brief: recorre la lista y le agrega a cada heroe la clave iniciales
            y el valor correspondiente
    parameters:
            lista: lista de heroes
    return: retorna false si no recibe una lista o si no puede asignar la clave
            y el valor al heroe correspondiente
    """
    if type(lista) != list or len(lista) < 1:
        return False
    else:
        for heroe in lista:
            if not definir_iniciales_nombre(heroe):
                print('El origen de datos no contiene el formato correcto')
                return False
            

def stark_imprimir_nombres_con_iniciales(lista: list):
    
    """
    brief: recorre la lista de heroes e imprime el nombre de cada uno con las iniciales
    parameters:
                lista: lista de heroes
    return: 
    """

    if  type(lista) == list or len(lista) > 0 :
        agregar_iniciales_nombre(lista)
        for heroe in lista:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")

def generar_codigo_heroe(id_heroe: int, genero_heroe: str):
    
    """
    brief: genera un codigo de identificacion para cada heroe 
    parameters:
                id_heroe: id del heroe
                genero_heroe:  genero del heroe
    return: retorna identificador (genero en mayuscula - id relleno de 0)
    """

    genero_heroe = genero_heroe.upper()
    if type(id_heroe) != int or not genero_heroe or genero_heroe not in ('M', 'F', 'NB'):
        return "N/A"
    else:
        id_heroe = str(id_heroe)
        if genero_heroe == "NB":
            identificador = f"{genero_heroe}-{id_heroe.zfill(7)}"
        else:
            identificador = f"{genero_heroe}-{id_heroe.zfill(8)}"
    return identificador

def agregar_codigo_heroe(heroe: dict, id_heroe: int):
    
    """
    brief: agrega el codigo del heroe al diccionario 
    parameters:
                heroe: diccionario de heroe 
                id_heroe: id heroe 
    return: retorna false si no hay un diccionario de heroe o si el codigo es largo
            del codigo es mayor a 10 caracteres y devuelve true si se pudo crear 
            la clave codigo_heroe y se le pudo asigar el codigo 
    """

    if not heroe:
        return False
    
    codigo_heroe=generar_codigo_heroe(id_heroe, heroe["genero"])

    if len(codigo_heroe)!= 10:
        return False
    elif len(codigo_heroe)== 10:
        heroe["codigo_heroe"] = codigo_heroe
        return True

def stark_generar_codigos_heroes(lista: list):

    """
    brief: genera un codigo para cada heroe y se los asigna a cada heroe
    parameters:
                lista: lista de heroes
    return: none 
    """

    contador = 0 
    if not lista:
        print("El origen de datos no contiene el formato correcto")
        return
    for heroe in lista:
        if type(heroe) != dict or 'genero' not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return
        else:    
            contador += 1
            agregar_codigo_heroe(heroe,contador)
    print(f"Se asignaron {contador} codigos")
    print(f"* El codigo del primer heroe es: {lista[0]['codigo_heroe']}")
    print(f"* El codigo del ultimo heroe es: {lista[-1]['codigo_heroe']}")

def sanitizar_entero(numero_str: str):
    
    """
    brief: intenta convertir el dato a entero
    parameters:
                numero_str: string con un numero
    return: retorna -2 si el numero es negativo, -1 si no es numero, -3 si no se pudo 
            convertir a entero y si se pudo convertir retorna el numero convertido 
    """

    numero_str = numero_str.strip()

    if numero_str.startswith("-") and numero_str[1:].isdigit():
        return -2

    if not numero_str.isdigit():
        return -1
    
    try:
        numero = int(numero_str)
    except:
        return -3
    return numero

def sanitizar_flotante(numero_str: str):

    """
    brief: intenta convertir el numero a flotante
    parameters:
                numero_str: string con un numero
    return: retorna -2 si el numero es negativo, -1 si no es numero, -3 si no se pudo 
            convertir a flotante y si se pudo convertir retorna el numero convertido 
    """

    numero_str = numero_str.strip()

    if numero_str.startswith('-'):
        return -2
    
    elif not all(caracter.isdigit() or caracter == '.' for caracter in numero_str):
        return -1
    
    try:
        numero = float(numero_str)
    except:
        return -3
    
    return numero

def sanitizar_string(valor_str: str, valor_por_defecto: str = '-'):

    """
    brief: devuelve el dato en string si lo pudo convertir
    parameters:
                valor_str: string 
                valor_por_defecto = valor que esta definido con '-'
    return: retorna el valor por defecto si el string esta vacio, si se ingreso algun numero
            retorna 'N/A' y si el valor ingresado son solo letras retorna el valor en minuscula
    """

    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if not valor_str:
        return valor_por_defecto.lower()

    if any(char.isdigit() for char in valor_str):
        return "N/A"

    valor_str = valor_str.replace('/', ' ')
    return valor_str.lower()

def sanitizar_dato(heroe: dict, key: str, tipo_dato: str):
    """
    brief: convierte si puede el valor en el tipo de datos que quieras 
    parameters:
                heroe: diccionario del heroe 
                key: clave del diccionario heroe:
                tipo_dato: valor al que se quiera sanitizar 
    return: retorna false si el tipo de dato es distinto a string, entero, flotante
            o si la clave no esta en heroe, si se pudo convertir retorna true
    """
    tipo_dato = tipo_dato.lower()
    key = key.lower()
    valor_a_sanitizar = heroe[key]
    retorno = False

    if tipo_dato != "string" and tipo_dato != "entero" and tipo_dato != "flotante":
        print("Tipo de dato no reconocido")
        return retorno
    
    if key not in heroe:
        print("La clave no pertenece al Heroe")
        return retorno


    if tipo_dato == "entero":
        valor_sanitizado = sanitizar_entero(valor_a_sanitizar)
        retorno = True
    elif tipo_dato == "flotante":
        valor_sanitizado = sanitizar_flotante(valor_a_sanitizar)
        retorno = True
    elif tipo_dato == "string":
        valor_sanitizado = sanitizar_string(valor_a_sanitizar)
        retorno = True
    heroe[key] = valor_sanitizado
    return retorno

def  stark_normalizar_datos(lista_heroes: list):
    
    """
    brief: normaliza los datos de la lista y los guarda ta normalizados
    parameters:
                lista_heroes: lista de heroes 
    return: 
    """
    if not lista_heroes:
        print("ERROR, Lista vacia")
    
    for heroe in lista_heroes:
        sanitizar_dato(heroe, "altura", "flotante")
        sanitizar_dato(heroe, "peso", "flotante")
        sanitizar_dato(heroe, "color_ojos", "string")
        sanitizar_dato(heroe, "color_pelo", "string")
        sanitizar_dato(heroe, "fuerza", "entero")
        sanitizar_dato(heroe, "inteligencia", "string")
    print("Datos normalizados")

def generar_indice_nombres(lista_heroes: list):
    
    """
    brief: convierte si puede el valor en el tipo de datos que quieras 
    parameters:
                heroe: diccionario del heroe 
                key: clave del diccionario heroe:
                tipo_dato: valor al que se quiera sanitizar 
    return: retorna false si el tipo de dato es distinto a string, entero, flotante
            o si la clave no esta en heroe, si se pudo convertir retorna true
    """
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")
        return []
    
    for heroe in lista_heroes:
        if type(heroe) != dict or  "nombre" not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return []
    
    nombres = []
    for heroe in lista_heroes:
        nombres_aux = heroe["nombre"].split()
        nombres.extend(nombres_aux)
    return nombres

def stark_imprimir_indice_nombre(lista_heroes: list):
    
    """
    brief: imprimi los nombres separados con guion todo junto 
    parameters:
                lista_heroes: lista de heroes 
    return:
    """

    lista_indice_nombres= generar_indice_nombres(lista_heroes)
    caracter_separador = "-"
    print(caracter_separador.join(lista_indice_nombres))

def convertir_cm_a_mtrs(valor_cm: float):
    
    """
    brief: convierte si puede el valor en el tipo de datos que quieras 
    parameters:
                valor_cm: valor en centimetros
    return: retorna el valor en metros si se convirtio, sino retorna -1
    """
    if type(valor_cm) == float or type(valor_cm) == int :
        if type(valor_cm)== int:
            valor_cm = float(valor_cm)
        valor_mts= valor_cm / 100
        return valor_mts
    else:
        return -1

def generar_separador(patron: str, largo: int , imprimir: bool = True):

    """
    brief: convierte si puede el valor en el tipo de datos que quieras 
    parameters:
                patron: patron que se va a repetir para generar el separador
                largo: largo del patron que se va a repetir
                imprimir: bool, si es true imprime, si es false lo retona
    return: si imprimir es false retorna el parametro
    """

    if (len(patron) == 0 or len(patron) > 2) and (largo < 1 or largo > 235):
        print("N/A")
    
    if len(patron) == 2:
        if largo % 2 != 0:
            parametro = (patron * (largo // 2)) + patron[0]
        else: 
            parametro = patron * (largo // 2) 
    else:    
        parametro = patron * largo
    if imprimir == True:
        print(parametro)
    else:
        return parametro

def generar_encabezado(titulo: str):

    """
    brief: genera el encabezado 
    parameters:
                titulo: titulo 
    return: retorna entre el separador el titulo
    """

    separador = generar_separador("*",110, False)
    titulo = titulo.upper()
    return f"{separador}\n\n{titulo}\n\n{separador}"

def imprimir_ficha_heroe(heroe: dict):

    """
    brief: imprime la ficha con los datos del heroe  
    parameters:
                heroe: diccionario del heroe  
    return:
    """

    altura_en_cm = float(heroe["altura"])
    altura_en_mts = convertir_cm_a_mtrs(altura_en_cm)
    print(generar_encabezado("principal"))
    print(f"""
    {'NOMBRE DEL HEROE:':<30} {heroe["nombre"]} ({heroe["iniciales"]})
    {'IDENTIDAD SECRETA:':<30} {heroe["identidad"]}
    {'CONSULTORA:' :<30} {heroe["empresa"]}
    {'CODIGO DE HEROE:' :<30} {heroe["codigo_heroe"]}
    """)
    print(generar_encabezado("fisico"))
    print(f"""
    {'ALTURA:':<30} {altura_en_mts:.2f} MTS
    {'PESO:':<30} {heroe["peso"] } KG
    {'FUERZA:' :<30} {heroe["fuerza"]} N
    """)
    print(generar_encabezado("señas particulares"))
    print(f"""
    {'COLOR DE OJOS:':<30} {heroe["color_ojos"]}
    {'COLOR DE PELO :':<30} {heroe["color_pelo"] }
    """)

def stark_navegar_fichas(lista: list):

    """
    brief: modifica el indice para moverse entre los heroes de la lista e imprime la lista 
    parameters:
                lista: lista de heroe 
    return: 
    """
    indice = 0

    while True:
        system("cls")
        imprimir_ficha_heroe(lista[indice])
        opcion = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n")
        opcion = opcion.lower() 
        
        if opcion == "1":
            if indice == 0:
                indice = len(lista)-1
            else:
                indice = indice - 1
        elif opcion == "2":
            if indice == len(lista)-1:
                indice = 0
            else:
                indice = indice + 1
        elif opcion == "s":
            break
        system("cls")

def imprimir_menu():
    """
    brief: imprime el menu 
    parameters:
    return:
    """
    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir
    ____________________________________________________________
    """)

def stark_menu_principal():
    """
    brief: imprime el menu y pide una opcion  
    parameters: 
    return: retorna la opcion ingresada
    """
    imprimir_menu()
    opcion = input("Ingrese una opcion:")
    opcion = opcion.lower()
    return opcion

def stark_marvel_app_3(lista: list):

    """
    brief: muestra el menu, valida la opcion recibida y segun  la opcion llama a la 
            funcion que realiza la opcion elegida  
    parameters:
                lista: lista de heroes 
    return:
    """
    flag_codigos = False
    flag_datos = False
    flag_iniciales = False
    while True:
        opcion = stark_menu_principal()
        while opcion not in ["1","2","3","4","5","s"]:
            opcion = stark_menu_principal()
        match (opcion):
            case "1":
                stark_imprimir_nombres_con_iniciales(lista)
                flag_iniciales = True
                system("pause")
            case "2":
                stark_generar_codigos_heroes(lista)
                flag_codigos = True
                system("pause")
            case "3":
                stark_normalizar_datos(lista)
                flag_datos = True
                system("pause")
            case "4":
                stark_imprimir_indice_nombre(lista)
                system("pause")
            case "5":
                if flag_datos == True and flag_codigos == True and flag_iniciales == True:
                    stark_navegar_fichas(lista)
                else:
                    print("Ingresar a la opcion 1, 2 y 3 antes de navegar por las fichas")
                    system("pause")
            case "s":
                break
        system("cls")

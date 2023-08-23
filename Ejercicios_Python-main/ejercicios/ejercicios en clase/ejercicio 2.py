'''
EJERCICIO 2
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”
Alumno: Sibikousky, Ian Marco 
Division: 1C
'''
seguir = "si"
while(seguir == "si"):
    numero_opcion = int(input("Ingrese un numero entre el 1 y el 8: "))
    while(numero_opcion < 1 or numero_opcion > 8):
        numero_opcion = int(input("Error, regla de estilo inexistente. Ingrese un numero entre el 1 y el 8: "))
    match(numero_opcion):
            case 1:
                print("hola1")
            case 2:
                print("hola2") 
            case 3:
              print("hola3")
            case 4:
               print("hola4")
            case 5:
                print("hola5")
            case 6:
                print("hola6")
            case 7: 
                print("hola7")
            case 8:
                print("hola8")
                
    seguir = input("Quiere continuar: ")



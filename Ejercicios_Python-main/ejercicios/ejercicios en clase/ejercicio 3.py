'''
EJERCICIO 3
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
Alumno: Sibikousky, Ian Marco 
Division: 1C
'''
contador_votos = 0
contador_masculino_votaron_participantes = 0
contador_genero_femenino = 0
acumulador_edad_femenino = 0
promedio_edad_mujeres = 0
bandera_mas_joven = True
nombre_votante_mas_joven = ""
edad_votante_mas_joven = 100
contador_votos_marcos = 0
contador_votos_nacho = 0
contador_votos_julieta = 0
porcentaje_votos_marcos = 0
porcentaje_votos_nacho = 0
porcentaje_votos_julieta = 0
ganador_del_reality = ""
respuesta = "si"

while (respuesta == "si"):
   nombre_votante = input("Ingrese nombre del votante ")
   edad_votante = int(input("Ingrese la edad del votante "))
   while(edad_votante<13):
      edad_votante = int(input("Reingrese su edad (Solo mayores de 13) "))
   genero_votante = input("Ingrese genero del votante ")
   while(genero_votante != "masculino" and genero_votante != "femenino" and genero_votante != "otro" ):
      genero_votante = input("Reingrese genero del votante (masculino, femenino, otro) ")
   nombre_participante = input("Ingrese el nombre del participante ")
   while(nombre_participante != "Julieta" and nombre_participante != "Nacho" and nombre_participante != "Marcos"):
       nombre_participante = input("Reingrese el nombre del participante (Nacho, Julieta o Marcos) ")
   contador_votos += 1
  
   if(genero_votante == "femenino"):
      contador_genero_femenino += 1
      acumulador_edad_femenino += edad_votante
    
   if((genero_votante == "masculino") and (edad_votante > 25 and edad_votante < 40) and 
      (nombre_participante == "Nacho" or nombre_participante == "Julieta") ):
      contador_masculino_votaron_participantes += 1
      
   match(nombre_participante):
     case "Nacho":
       contador_votos_nacho += 1
     case "Julieta":
       contador_votos_julieta += 1
     case "Marcos":
       contador_votos_marcos += 1
       
   if nombre_participante == "Nacho":
     if((bandera_mas_joven == True) or (edad_votante < edad_votante_mas_joven)):
       edad_votante_mas_joven = edad_votante
       nombre_votante_mas_joven = nombre_votante
       bandera_mas_joven = False
  
   respuesta = input("quiere seguir ingresando votos (si o no)")

if(contador_genero_femenino > 1):
 promedio_edad_mujeres = acumulador_edad_femenino / contador_genero_femenino

porcentaje_votos_julieta = (contador_votos_julieta*100) / contador_votos
porcentaje_votos_marcos = (contador_votos_marcos*100) / contador_votos
porcentaje_votos_nacho = (contador_votos_nacho*100) / contador_votos

if((contador_votos_julieta > contador_votos_nacho) and (contador_votos_julieta > contador_votos_marcos)):
  ganador_del_reality = "Julieta"
elif (contador_votos_marcos > contador_votos_nacho):
  ganador_del_reality = "Marcos"
else:
  ganador_del_reality = "Nacho"
  
if(promedio_edad_mujeres > 1):
 print(f"El promedio de edad de las mujeres votantes es {promedio_edad_mujeres}")
else: 
 print("No se ingresaron mujeres")
print(f"La cantidad de hombres entre 25 y 40 años que votaron a Nacho o a Julieta es: {contador_masculino_votaron_participantes}")
print(f"El nombre del votante mas joven que voto a Nacho es: {nombre_votante_mas_joven} ")
print(f"El porcentaje de votos que recibio Julieta es: {porcentaje_votos_julieta}% con {contador_votos_julieta} votos")
print(f"El porcentaje de votos que recibio Nacho es: {porcentaje_votos_nacho}% con {contador_votos_nacho} votos ")
print(f"El porcentaje de votos que recibio Marcos es: {porcentaje_votos_marcos}% con {contador_votos_marcos} votos")
print(f"El ganador del reality es: {ganador_del_reality}")

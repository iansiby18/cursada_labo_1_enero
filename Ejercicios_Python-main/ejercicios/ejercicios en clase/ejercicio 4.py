'''
EJERCICIO 4
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
Alumno: Sibikousky, Ian Marco 
Division: 1C
'''

lista_contador_de_compras = range(0,15)
acumulador_de_numeros= 0
acumulador_precio_bruto = 0 
acumulador_peso_total = 0
bandera_tipo_mas_caro = True
precio_mas_caro = 0
tipo_producto_mas_caro = ""
acumulador_precio_por_kg = 0
'''
while(contador_de_compras <= 15 and contador_de_compras >= 1):
    contador_de_compras -= 1 
'''

for n in lista_contador_de_compras:
    peso_producto = int(input("Ingrese el peso del producto(entre 10 y 100): "))
    while(peso_producto < 10 and peso_producto > 100):
        peso_producto = int(input("Peso incorrecto. Ingrese el peso del producto (entre 10 y 100): "))
    precio_por_kg = int(input("Ingrese el precio por KG del producto: "))
    while(precio_por_kg < 0 ):
        precio_por_kg = int(input("ERROR. Ingrese el precio por KG del producto: "))
    tipo_variedad_producto = input("Ingrese el tipo de variedad del producto (vegetal, animal, mezcla)")
    while((tipo_variedad_producto != "vegetal") and (tipo_variedad_producto != "animal") and (tipo_variedad_producto != "mezcla")):
        tipo_variedad_producto = input("ERROR. Ingrese el tipo de variedad del producto (vegetal, animal, mezcla)")
    precio_bruto = precio_por_kg * peso_producto
    acumulador_precio_bruto = acumulador_precio_bruto + precio_bruto
    acumulador_peso_total = acumulador_peso_total + peso_producto
    acumulador_precio_por_kg = acumulador_precio_por_kg + precio_por_kg
    
    if((bandera_tipo_mas_caro == True) or (precio_por_kg > precio_mas_caro)):
       precio_mas_caro = precio_por_kg
       tipo_producto_mas_caro = tipo_variedad_producto
       bandera_tipo_mas_caro = False
promedio_precio_total = acumulador_precio_por_kg / 15

print(f"El importe total a pagar sin descuento es: {acumulador_precio_bruto}")

if(acumulador_peso_total > 300):
    precio_con_descuento_veinticinco= acumulador_precio_bruto - (acumulador_precio_bruto * 0.25)
    print(f"El precio con el descuento por llevar mas de 300 kg es: {precio_con_descuento_veinticinco}")
elif(acumulador_peso_total > 100):
    precio_con_descuento_quince = acumulador_precio_bruto - (acumulador_precio_bruto * 0.15)
    print(f"El precio con el descuento por llevar mas de 100 kg es: {precio_con_descuento_quince}")

print(f"El tipo de producto mas caro es: {tipo_producto_mas_caro}")
print(f"El promedio de precio por kilo en total es: {promedio_precio_total:.2f}")





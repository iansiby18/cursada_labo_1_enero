'''
EJERCICIO 1 
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (barbijo, jabón o alcohol)
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
Alumno: Sibikousky, Ian Marco 
Division: 1C
'''
                                                                                                                                                                        
tipo_producto = input("Ingrese tipo (barbijo, jabón o alcohol): ")
while(tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol"):
   tipo_producto = input("Tipo de producto invalido, reingrese tipo de producto (barbijo, jabón o alcohol): ")
precio_producto = float(input("Ingrese el precio: "))
cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
marca_producto = input("Ingrese la marca: ")
fabricante_producto = input("Ingrese el nombre del fabricante: ")


print(f"El tipo de producto es: {tipo_producto}")
print(f"El precio del producto  es: {precio_producto:.2f}")
print(f"La cantidad de unidades es: {cantidad_unidades}")
print(f"La marca del producto es: {marca_producto}")
print(f"El fabricante del producto es: {fabricante_producto}")
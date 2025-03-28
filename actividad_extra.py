# Desarrollar un programa en Python que permita gestionar un inventario
# simple de productos, incluyendo funciones básicas como agregar productos,
# eliminar productos y mostrar el inventario.
# El programa debe tener un menú interactivo que permita al usuario
# seleccionar las siguientes operaciones:
# Agregar un nuevo producto al inventario, solicitando al usuario el nombre y
# la cantidad inicial del producto.
# Eliminar un producto existente del inventario, solicitando al usuario el
# nombre del producto a eliminar.
# Mostrar el inventario actual, que incluya el nombre y la cantidad de cada
# producto.
# Salir del programa.
# El inventario puede ser almacenado utilizando un diccionario simple, donde
# las claves sean los nombres de los productos y los valores sean las cantidades. Se
# deben manejar situaciones simples como la introducción de productos duplicados
# o la eliminación de productos inexistentes.
import random, pprint, sys

def agregar_productos(mi_inventario):
    """Esta funcion agrega productos al inventario solicitando al usuario nombre del producto y cantidad
    """
    nombre = input("Nombre del producto a agregar: ")
    cantidad = input("Cantidad: ")
    mi_inventario[nombre] = int(cantidad)
    return mi_inventario

def eliminar_productos(mi_inventario):
    """Esta funcion elimina productos al inventario solicitando al usuario nombre del producto
    """
    nombre = input("Nombre del producto a eliminar: ")
    del mi_inventario[nombre]
    return mi_inventario
    
def mostrar_inventario(mi_inventario):
    """Esta funcion muestra el inventario actual
    """
    pprint.pprint(mi_inventario)
    
mi_inventario = {
    'producto_1': random.randrange(100),
    'producto_2': random.randrange(100),
    'producto_3': random.randrange(100),
    'producto_4': random.randrange(100),
    'producto_5': random.randrange(100),
    'producto_6': random.randrange(100),
}

n = 1

while n != 0:

    options = input( '''Selecciona que tarea queres realizar:
           1) Agregar un producto
           2) Eliminar un producto
           3) Consultar el inventario actual
      
           Opción:
           ''')
    match int(options):
        case 1: 
            agregar_productos(mi_inventario)
        case 2:
            eliminar_productos(mi_inventario)
        case 3:
            mostrar_inventario(mi_inventario)

    n = int(input ("Para finalizar el programa ingresar 0, para regresar al MENU, cualquier tecla: "))
    if n == 0:
        sys.exit(1)


"""
Ejercicio 13: Mini Sistema de Gestión de Inventario

Este programa simula un sistema básico de inventario para una tienda.
Permite agregar productos, registrar ventas y mostrar el inventario actual.

Cada producto se almacena como un diccionario con:
- "nombre"
- "precio"
- "cantidad"

El inventario completo es una lista de estos diccionarios.

Conceptos usados:
- Listas y diccionarios
- Funciones
- Bucle while
- Condicionales
- Manejo de entradas con input()
- Buenas prácticas (PEP 8)
"""

# Lista para almacenar el inventario de productos
inventario = []

def agregar_producto(nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    :param nombre: Nombre del producto
    :param precio: Precio por unidad
    :param cantidad: Cantidad disponible
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print("Producto agregado correctamente.")


def realizar_venta(nombre, cantidad_vendida):
    """
    Realiza una venta y actualiza la cantidad en el inventario.

    :param nombre: Nombre del producto vendido
    :param cantidad_vendida: Cantidad que se desea vender
    """
    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                total = producto["precio"] * cantidad_vendida
                print(f"Venta realizada. Total: ${total:.2f}")
            else:
                print("No hay suficiente cantidad disponible.")
            return
    print("Producto no encontrado.")


def mostrar_inventario():
    """
    Muestra todos los productos en el inventario con sus detalles.
    """
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            print("-" * 20)


# Menú principal del sistema
while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))
            agregar_producto(nombre, precio, cantidad)
        except ValueError:
            print("Error: precio o cantidad no válidos.")

    elif opcion == "2":
        nombre = input("Nombre del producto a vender: ")
        try:
            cantidad_vendida = int(input("Cantidad a vender: "))
            realizar_venta(nombre, cantidad_vendida)
        except ValueError:
            print("Error: cantidad inválida.")

    elif opcion == "3":
        mostrar_inventario()

    elif opcion == "4":
        print("Saliendo del sistema de inventario.")
        break

    else:
        print("Opción no válida. Intenta otra vez.")

"""
Ejercicio 9: Agenda de Contactos con Diccionario

Este programa simula una agenda telefónica usando un diccionario.
Permite añadir contactos, buscar un número por nombre y ver todos los contactos.

Conceptos usados:
- Diccionarios
- Funciones (def)
- input() para entrada de datos
- Bucle for para recorrer el diccionario
"""

# Diccionario vacío para guardar los contactos
agenda = {}

# Función para agregar un nuevo contacto
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto agregado correctamente.")

# Función para buscar un contacto por su nombre
def buscar_contacto(nombre):
    if nombre in agenda:
        print("Teléfono de", nombre + ":", agenda[nombre])
    else:
        print("Ese contacto no está en la agenda.")

# Función para mostrar todos los contactos
def mostrar_contactos():
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        print("Contactos guardados:")
        for nombre in agenda:
            print(nombre, "->", agenda[nombre])

# Menú principal
while True:
    print("\n--- MENÚ AGENDA ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Número de teléfono: ")
        agregar_contacto(nombre, telefono)

    elif opcion == "2":
        nombre = input("Escribe el nombre del contacto a buscar: ")
        buscar_contacto(nombre)

    elif opcion == "3":
        mostrar_contactos()

    elif opcion == "4":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

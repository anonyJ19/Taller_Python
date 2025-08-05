"""
Ejercicio: Gestión de Lista de Compras

Este programa permite al usuario gestionar una lista de compras.
Se puede agregar, eliminar, ver la lista o salir del programa.

Conceptos usados:
- Listas y sus métodos: append(), remove()
- Bucle while
- Condicionales: if, elif, else
- Función input() para leer datos del usuario
"""

lista_compras = []  # Lista vacía para guardar los productos

while True:
    # Menú de opciones
    print("\n--- MENÚ ---")
    print("1. Agregar ítem a la lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")

    opcion = input("Escribe el número de la opción: ")

    if opcion == "1":
        item = input("Escribe el producto que quieres agregar: ")
        lista_compras.append(item)
        print(f"'{item}' fue agregado a la lista.")

    elif opcion == "2":
        item = input("Escribe el producto que quieres eliminar: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' fue eliminado de la lista.")
        else:
            print(f"'{item}' no está en la lista.")

    elif opcion == "3":
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            print("Lista de compras:")
            for producto in lista_compras:
                print("-", producto)

    elif opcion == "4":
        print("Saliendo del programa...")
        break  # Termina el bucle

    else:
        print("Opción no válida. Intenta de nuevo.")

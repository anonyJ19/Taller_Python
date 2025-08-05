"""
Ejercicio 14: Simulador de Cajero Automático (ATM)

Este programa simula un cajero automático que permite al usuario:
- Consultar el saldo
- Depositar dinero
- Retirar dinero

La lógica está dividida en funciones y se maneja un saldo inicial.

Conceptos usados:
- Funciones
- Bucle while
- Condicionales
- Variables
- Input/Output
- Buenas prácticas (PEP 8)
"""

# Saldo inicial
saldo = 100000


def consultar_saldo():
    """
    Muestra el saldo actual disponible.
    """
    print(f"Tu saldo actual es: ${saldo}")


def depositar(monto):
    """
    Suma el monto ingresado al saldo global.

    :param monto: cantidad de dinero a depositar
    """
    global saldo
    saldo += monto
    print(f"Has depositado ${monto}. Nuevo saldo: ${saldo}")


def retirar(monto):
    """
    Resta el monto al saldo si hay suficiente dinero.

    :param monto: cantidad de dinero a retirar
    """
    global saldo
    if monto <= saldo:
        saldo -= monto
        print(f"Has retirado ${monto}. Saldo restante: ${saldo}")
    else:
        print("Fondos insuficientes para esta operación.")


# Menú principal del cajero automático
while True:
    print("\n CAJERO AUTOMÁTICO ")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        consultar_saldo()

    elif opcion == "2":
        try:
            monto = int(input("¿Cuánto deseas depositar? "))
            if monto > 0:
                depositar(monto)
            else:
                print("El monto debe ser mayor que cero.")
        except ValueError:
            print("Error: debes ingresar un número válido.")

    elif opcion == "3":
        try:
            monto = int(input("¿Cuánto deseas retirar? "))
            if monto > 0:
                retirar(monto)
            else:
                print("El monto debe ser mayor que cero.")
        except ValueError:
            print("Error: debes ingresar un número válido.")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

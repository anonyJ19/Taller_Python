# Adivina el número
import random
"""
programa de juego adivina el numero secreto
"""

numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
intentos = 5  # Número de intentos permitidos
adivinado = False  # Bandera para saber si adivinó

print("Adivina el número secreto entre 1 y 100. Tienes 5 intentos.")

while intentos > 0:
    numero = int(input("Ingrese un número: "))

    if numero > numero_secreto:
        print("El número es menor que el número secreto.")

    elif numero < numero_secreto:
        print("El número es mayor que el número secreto.")

    else:
        print("¡Felicidades! Adivinaste el número secreto.")
        adivinado = True  # Cambia la bandera si lo adivinó
        break  # Sale del ciclo

    intentos -= 1  # Resta un intento después de cada intento fallido

# Si se acabaron los intentos y no lo adivinó
if not adivinado:
    print(f"Lo siento. El número secreto era {numero_secreto}.")
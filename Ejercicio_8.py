"""
Ejercicio 8: Validador de Palíndromos

Este programa tiene una función que recibe una palabra o frase
y verifica si es un palíndromo se lee igual al derecho y al revés,
ignorando espacios y mayúsculas.

Conceptos usados:
- Funciones
- Strings: replace(), lower()
- Slicing [::-1]
- Valores booleanos (True o False)
"""

# Función para verificar si es palíndromo
def es_palindromo(texto):
    texto = texto.lower()  # Pasar todo a minúscula
    texto = texto.replace(" ", "")  # Quitar espacios
    texto_al_reves = texto[::-1]  # Invertir el texto

    if texto == texto_al_reves:
        return True
    else:
        return False

# Probar la función
frase = input("Escribe una palabra o frase: ")

if es_palindromo(frase):
    print("Sí es un palíndromo.")
else:
    print("No es un palíndromo.")

"""
Ejercicio 10: Contador de Frecuencia de Palabras

Este programa tiene una función que recibe un texto y devuelve un diccionario
donde cada palabra es una clave y su valor es el número de veces que aparece.

Conceptos usados:
- Diccionarios y método get()
- Funciones (def)
- Strings: lower(), split()
- Bucle for para recorrer las palabras
"""

# Función que cuenta la frecuencia de palabras
def contar_palabras(texto):
    texto = texto.lower()  # Pasar todo a minúsculas
    palabras = texto.split()  # Separar en palabras
    conteo = {}  # Diccionario vacío para guardar los resultados

    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1  # Sumar 1 si ya existe, si no, empieza en 1

    return conteo  # Retornar el diccionario con los conteos

# Probar la función con texto ingresado
entrada = input("Escribe un texto: ")
resultado = contar_palabras(entrada)

# Mostrar las palabras y cuántas veces aparecen
print("Frecuencia de palabras:")
for palabra in resultado:
    print(palabra, "->", resultado[palabra])

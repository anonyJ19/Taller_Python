"""
Ejercicio 11: Elementos Comunes y Únicos entre Listas

Este programa tiene una función que recibe dos listas y devuelve una tupla con tres conjuntos:
1. Elementos que están en ambas listas.
2. Elementos que solo están en la primera lista.
3. Elementos que solo están en la segunda lista.

Conceptos usados:
- Funciones (def)
- Listas
- Conjuntos (sets)
- Operadores de conjuntos: & (intersección), - (diferencia)
"""

# Función que compara dos listas y devuelve los tres conjuntos
def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    comunes = set1 & set2  # Elementos en ambas listas
    solo_primera = set1 - set2  # Elementos únicos de la primera
    solo_segunda = set2 - set1  # Elementos únicos de la segunda

    return (comunes, solo_primera, solo_segunda)

# Ejemplo de prueba
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

resultado = comparar_listas(lista_a, lista_b)

# Mostrar los resultados
print("Elementos en ambas listas:", resultado[0])
print("Solo en la primera lista:", resultado[1])
print("Solo en la segunda lista:", resultado[2])

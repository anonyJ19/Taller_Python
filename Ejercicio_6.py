"""
Ejercicio 6: Análisis de Calificaciones en una Lista

Este programa tiene una función que recibe una lista de calificaciones .
La función calcula y retorna el promedio, la calificación más alta y la más baja.
Luego, se prueba la función con una lista de ejemplo.

Agrs:
- Listas
- Tuplas
- Funciones (def, return)
- Funciones integradas: sum(), len(), max(), min()
"""

# Función que analiza las calificaciones
def analizar_calificaciones(lista):
    promedio = sum(lista) / len(lista)  # Calcula el promedio
    mayor = max(lista)  # Encuentra la nota más alta
    menor = min(lista)  # Encuentra la nota más baja
    return (promedio, mayor, menor)  # Retorna una tupla con los resultados

# Lista de calificaciones de ejemplo
calificaciones = [3.5, 4.0, 2.8, 5.0, 3.9]

# Llamar la función y guardar el resultado
resultado = analizar_calificaciones(calificaciones)

# Mostrar los resultados
print("Promedio:", resultado[0])
print("Calificación más alta:", resultado[1])
print("Calificación más baja:", resultado[2])

"""
Ejercicio 12: Conversor de Unidades

Este programa usa un diccionario con factores de conversión y una función
que permite convertir una cantidad de una unidad a otra.

Conceptos usados:
- Diccionarios
- Funciones con varios parámetros
- return
- Manejo de errores con if ... in ...
"""

# Diccionario con factores de conversión (de metros a otras unidades)
factores_conversion = {
    "pies": 3.28084,
    "yardas": 1.09361,
    "centimetros": 100,
    "milimetros": 1000,
    "kilometros": 0.001
}

# Función para convertir unidades
def convertir(cantidad, unidad_origen, unidad_destino):
    if unidad_origen != "metros":
        return "Por ahora solo se admite convertir desde metros."

    if unidad_destino in factores_conversion:
        factor = factores_conversion[unidad_destino]
        resultado = cantidad * factor
        return resultado
    else:
        return "Unidad de destino no válida."

# Prueba del programa
print("Conversor desde metros a otras unidades.")
cantidad = float(input("Ingresa la cantidad en metros: "))
unidad_destino = input("¿A qué unidad quieres convertir? (pies, yardas, centimetros, milimetros, kilometros): ")

resultado = convertir(cantidad, "metros", unidad_destino)

# Mostrar resultado
if type(resultado) == str:
    print("Error:", resultado)
else:
    print(f"{cantidad} metros equivale a {resultado} {unidad_destino}.")

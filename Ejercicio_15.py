"""
Ejercicio 15: Generador de Reportes de Estudiantes

Este programa guarda las notas de los estudiantes y muestra un reporte con su promedio
y si aprobaron o no.
"""

# Diccionario con los estudiantes y sus calificaciones
estudiantes = {
    "Ana": [4.0, 4.5, 5.0],
    "Juan": [2.5, 3.0, 2.9],
    "Luisa": [3.2, 3.5, 3.8],
    "Pedro": [1.5, 2.0, 1.8]
}


def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    suma = sum(notas)
    cantidad = len(notas)
    promedio = suma / cantidad
    return promedio


def obtener_estado(promedio):
    """Devuelve 'Aprobado' si el promedio es mayor o igual a 3.0, si no 'Reprobado'."""
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_reporte(estudiantes):
    """Muestra el reporte de todos los estudiantes con promedio y estado."""
    print("Reporte de Calificaciones:")
    print("-------------------------")
    for nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = calcular_promedio(notas)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")
    print("-------------------------")


# Llamamos la función para mostrar el reporte
generar_reporte(estudiantes)

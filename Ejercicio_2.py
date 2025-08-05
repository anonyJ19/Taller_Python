"""
Ejercicio: Verificación de edad

Este programa solicita al usuario que ingrese su edad
y determina si es menor o mayor de edad.
"""

def verificar_edad():
    """
    esta funcion nos ayuda a evaluar condiciones

    args:
      edad: es nuestra variable
      if:Nos deja el valor de edad, para saber cuando es recien nacido

      elif: nos ayuda a validar si el if no se cumple pasa a elif a validar una condicion

      else: cierra el ciclo de elif

    """
edad = int(input("Ingrese su edad: "))  # Solicita la edad al usuario

if edad < 18:
        print("Usted es un joven ")
else:
        print("usted es un joven adulto")



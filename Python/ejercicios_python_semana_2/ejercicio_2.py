"""Ejercicio 2: Aprobado o reprobado Crea un programa que reciba la calificación de un estudiante (0 a 100)
 e indique si está aprobado (60 o más) o reprobado (menos de 60).
"""
calificacion = input("Ingrese su calificación. Debe ser un número del 0 al 100\n")
try:
    calificacion = float(calificacion)
    if calificacion >= 0 and calificacion <=100:
        if calificacion >= 60:
            print("Aprobaste!!")
        else:
            print("Reprobaste")
    else:
        print("El número ingresado está fuera del rango")
except ValueError:
    print("El dato ingresado no es un número")

"""Ejercicio 3: Tabla de multiplicar Escribe un programa
 que muestre la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un bucle for.
"""

try:
    numero_a_multiplicar = float(input("Ingrese un número del 1 al 10\n"))
    if numero_a_multiplicar >= 1 and numero_a_multiplicar <= 10:
        for x in range(1,11):
            print(f"{x} x {numero_a_multiplicar} = {x * numero_a_multiplicar}")
            x+=1
    else:
        print("El número ingresado no está dentro del rango permitido")
except ValueError:
    print("El dato ingresado no es un número")
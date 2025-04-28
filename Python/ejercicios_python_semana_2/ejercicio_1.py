#Ejercicio 1: Clasificador de números Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.
numero = input("Ingrese un número \n")
try:
    numero = float(numero)
    if numero >= 0:
        print(f"El número {numero} es positivo")
    elif numero == 0:
        print("El número es igual a 0")
    else: 
        print(f"El número {numero} es negativo")
except ValueError:
    print("El dato ingresado no es un número")

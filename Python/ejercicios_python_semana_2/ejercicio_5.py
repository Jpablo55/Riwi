"""Ejercicio 5: Adivina el número Crea un programa que genere un número aleatorio entre 1 y 10, y le pida al usuario que lo adivine. 
El programa debe indicar si el número ingresado es mayor, menor o correcto. El usuario tiene hasta 3 intentos.
"""
import random


numeroAleatorio = random.randint(1, 10)
try:
    for x in range(3):
        numeroIngresado = int(input("Adivina el número: Ingrese un número entero del 1 al 10.  \n"))
        if numeroIngresado > 0 and numeroIngresado <=10:
            if numeroIngresado == numeroAleatorio:
                print(f"Felicidades!! has adivinado. El número es {numeroAleatorio}")
                break
            elif x == 2:
                print(f"Lo siento. Perdiste. El número era {numeroAleatorio}")
            else:
                print(f"Lo siento. Vuelve a intentarlo. Te quedan {3-(x+1)} intentos")
        else:
            print("El número ingresado no está dentro del rango permitido")
        
except ValueError:
    print("El dato ingresado no es un número")
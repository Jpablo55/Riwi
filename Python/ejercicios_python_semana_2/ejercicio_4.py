"""Ejercicio 4: Contador regresivo Crea un programa que pida un número positivo al usuario 
y haga una cuenta regresiva desde ese número hasta 0 usando un bucle while.
"""
try:
    numeroPositivo = int(input("Ingrese un número positivo\n"))
    if numeroPositivo > 0:
         while numeroPositivo >= 0:
            print(numeroPositivo)
            numeroPositivo-=1
    else:
        print("El número no es positivo")

except ValueError:
    print("El dato ingresado no es un número")

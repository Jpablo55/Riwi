#Solicita una edad y determina si la persona es menor de edad (menor a 18).
edad = int(input("Ingresa tu edad "))
mayorEdad = edad >= 18
menorEdad = edad <18
print(f"Eres mayor de edad" * mayorEdad + f"No eres mayor de edad" * menorEdad)
# 💘 ¿Compatibles?

# Pide:

#     Nombre y edad de dos personas

# Verifica si:

#     Ambos tienen al menos 18 años
#     Se llaman distinto
#     La diferencia de edad no supera los 10 años

# Si cumplen todo, imprime un mensaje gracioso diciendo que son compatibles 💞
# Si no, di por qué no lo son.

persona1 = input("Persona #1: Ingresa tu nombre \n")
while True:

    edadPersona1 = input("Persona #1: Ingresa tu edad \n")
    try:
        if edadPersona1.isdigit:
            edadPersona1 = int(edadPersona1)
            edadPersona1+= 2
            if edadPersona1 > 0:
                break
            else: 
                print("La edad debe ser un número mayor a 0")
    except ValueError:
        print("La edad ingresada no es un número. Vuelve a ingresar la edad")

persona2 = input("Persona #2: Ingresa tu nombre \n")
while True:

    edadPersona2 = input("Persona #2: Ingresa tu edad \n")
    try:
        if edadPersona2.isdigit:
            edadPersona2 = int(edadPersona2)
            edadPersona2+= 2
            if edadPersona2 > 0:
                break
            else: 
                print("La edad debe ser un número mayor a 0")
    except ValueError:
        print("La edad ingresada no es un número. Vuelve a ingresar la edad")
personaMayor = 0
personaMenor = 0
if edadPersona1 > edadPersona2:
    personaMayor = edadPersona1
    personaMenor = edadPersona2
else:
    personaMayor = edadPersona2
    personaMenor = edadPersona1
valAmbosMayoresEdad = edadPersona1 >= 18 and edadPersona2 >= 18
valNombresDiferentes = not(persona1 == persona2)
valDiferenciaEdad = personaMayor-personaMenor < 10
if (valAmbosMayoresEdad) and (valNombresDiferentes) and (valDiferenciaEdad):
    print("¡Son compatibles 💞!")
else:
    print("Lo siento. No son compatibles :(\n Ambos no son mayores de edad\n" * (not(valAmbosMayoresEdad)) +\
          "Lo siento. No son compatibles :(\n Tienen el mismo nombre\n" * (not(valNombresDiferentes)) +\
          "Lo siento. No son compatibles :(\n la diferencia de edad supera los 10 años\n" * (not(valDiferenciaEdad)))
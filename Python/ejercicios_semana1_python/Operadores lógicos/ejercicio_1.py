#Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.
edad = int(input("Ingresa tu edad "))
licenciaConduccion = input('Tienes licencia de conducción? ingresa "Si" o "No" ')
mayorEdad = edad >= 18
if licenciaConduccion == "Si" or licenciaConduccion == "si":
    licenciaConduccion = True
else:
    licenciaConduccion = False
if licenciaConduccion and mayorEdad:
    print("Puedes conducir")
else: 
    print("No puedes conducir")


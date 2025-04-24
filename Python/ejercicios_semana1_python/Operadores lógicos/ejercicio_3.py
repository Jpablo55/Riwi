#Dado un número, determina si está en el rango de 10 a 50 (inclusive).
numeroIngresado = float(input("Ingrese un número "))
rangoPermitido = numeroIngresado <= 50 and numeroIngresado >=10
fueraDeRango = not rangoPermitido
print("El número ingresado está dentro del rango permitido (De 10 a 50)" * rangoPermitido\
       + "El número ingresado no está dentro del rango permitido (De 10 a 50)" * fueraDeRango)
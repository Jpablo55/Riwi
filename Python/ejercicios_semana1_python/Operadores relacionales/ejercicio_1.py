# Pide dos números e indica cuál es mayor o si son iguales
numero1 = float(input("Ingresa un número "))
numero2 = float(input("Ingresa otro número "))
numero1Mayor = numero1 > numero2
numero2Mayor = numero2 > numero1
numerosIguales = numero2 == numero1
print(f"{numero1} es mayor que {numero2}"* numero1Mayor + f"{numero2} es mayor que {numero1}"* numero2Mayor\
     + f"Ambos numeros son iguales" * numerosIguales)

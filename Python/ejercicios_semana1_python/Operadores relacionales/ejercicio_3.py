# Escribe un programa que compare dos cadenas de texto e indique si son iguales o distintas.
texto1 = input("Escribe una cadena de texto ")
texto2 = input("Escribe otra cadena de texto ")
textosIguales = texto1 == texto2
textosDiferentes = not textosIguales
print("Las cadenas de texto no son iguales" * textosDiferentes + "Las cadenas de texto son iguales" * textosIguales)
#Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.
def valConversion(texto):
    val = False
    try:
        if int(texto):
            val = True
    except ValueError:
        print("El texto ingresado contiene caracteres no numericos")
    return val
numeroIngresado = input("Ingrese un numero ")
valNumero = valConversion(numeroIngresado)
valTexto = not valNumero
print("El dato ingresado es un número"* valNumero + "El dato ingresado no es un número"* valTexto)
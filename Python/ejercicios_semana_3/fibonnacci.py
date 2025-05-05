numero_actual: int = 0
siguiente_numero: int = 1

for _ in range(10):
    print(numero_actual)
    numero_actual, siguiente_numero = siguiente_numero, numero_actual + siguiente_numero


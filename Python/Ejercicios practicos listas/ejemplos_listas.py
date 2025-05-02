# numeros = [3, 1, 4]
# print(sorted(numeros))  # [1, 3, 4]  (numeros intacta)
# for idx, n in enumerate(numeros, 1):
#     print(idx, n)


# frutas: list[str] = ["Manzana", "Pera", "Guayaba", "Banano", "Mango"]
# for i, fruta in enumerate(frutas):
#     print(i, fruta)

# pares = [n for n in range(20) if n % 2 == 0]
# print(pares)

# matriz = [[i*j for j in range(5)] for i in range(3)]
# print(matriz)

#Ejercicios prácticos 

#Números primos

# def es_primo(n:int) -> bool:
#     return n > 1 and all(n%i != 0 for i in range(2, int(n**0.5)+1))
# listaEnteros: list[int] = [1,10,5,8,3,9,4,12,2,22,15]
# listaPrimos: list[int] = [numero for numero in listaEnteros if es_primo(numero)]
# print(listaPrimos)

#Intercalar listas
frutas: list[str] = ["Manzana", "Pera", "Guayaba", "Banano", "Mango"]
nombres: list[str] = ["Pedro", "Mariana", "Diego"]
listasFusionadas: list[str] = []
longitudFrutas: int = frutas.__len__()
longitudNombres: int = nombres.__len__()
longitudMayor = 0
if(longitudNombres > longitudFrutas):
    longitudMayor = longitudNombres
else:
    longitudMayor = longitudFrutas
for i in range(longitudMayor):
    if longitudFrutas - 1 >= i:
        listasFusionadas.append(frutas[i])
    if longitudNombres - 1 >= i:
        listasFusionadas.append(nombres[i])
print(listasFusionadas)


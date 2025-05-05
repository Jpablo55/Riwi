inicioFibonnacci: int = 0
secuenciaFibonnacci: int = 1
numeroAnterior: int = 0
for i in range(10):   
    if inicioFibonnacci == 0:
            print(inicioFibonnacci)
            inicioFibonnacci+=1
    else:
          print(secuenciaFibonnacci)
          secuenciaFibonnacci += numeroAnterior
          numeroAnterior = secuenciaFibonnacci - numeroAnterior

#Se reciben datos de entrada
nombreProducto = input("Ingrese el nombre del producto ")
#Bucles de validación de datos de entrada
while True:
    precioUnitario = input("Ingrese el precio unitario ")
    if precioUnitario.isdigit() and float(precioUnitario) > 0:
        precioUnitario = float(precioUnitario)
        break
    else:
        print("El dato ingresado no es un número o no es positivo")
while True:
    cantidadProducto = input("Ingrese la cantidad deseada del producto ")
    if cantidadProducto.isdigit() and int(cantidadProducto):
        cantidadProducto = int(cantidadProducto)
        break
    else:
        print("El dato ingresado no es un número o no es positivo")
while True:
    porcentajeDescuento = input("Ingrese el porcentaje de descuento (Debe ser un numero del 0 al 100) ")
    if porcentajeDescuento.isdigit() and float(porcentajeDescuento) <= 100 and float(porcentajeDescuento) >= 0:
        porcentajeDescuento = float(porcentajeDescuento)
        break
    else:
        print("El porcentaje no está dentro del rango permitido")
#Procesos aritmeticos para calcular el costo total de la compra
precioSinDescuento = precioUnitario * cantidadProducto
descuento = (porcentajeDescuento/100)* precioSinDescuento
costoTotalCompra = 0
#Validación si hay o no hay descuento
if porcentajeDescuento != 0:
    costoTotalCompra = precioSinDescuento - descuento
else:
    costoTotalCompra = precioSinDescuento
print(f"Producto: {nombreProducto} \nPrecio: {precioUnitario:.2f}  \nCantidad: {cantidadProducto} \nDescuento: \nCosto total: {costoTotalCompra:.2f}")
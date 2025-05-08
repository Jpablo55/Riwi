inventario: dict = {}
def añadir_producto(product: str, precio:float, amount: int):
    inventario[product] = (precio, amount)
añadir_producto('pastel de pollo',3500,7)
añadir_producto('pollo',3500,5)
def consultar_producto(product: str):
    if product in inventario:
        print(f'Producto: {product}\nPrecio: {inventario[product][0]}\nCantidad: {inventario[product][1]}')
    else:
        print('El producto que has buscado no existe')
consultar_producto('pastel de pollo')
def actualizar_producto(product:str,precio:float):
    if product in inventario:
        inventario[product] = (precio, inventario[product][1])
    else:
        print('El producto ingresado no existe. Dirígete a "Añadir producto"')
actualizar_producto('pollo', 2500)
print(inventario['pollo'])
def eliminar_producto(product: str):
    if product in inventario:
        del inventario[product]
    else:
        print('El producto que quieres eliminar no existe')

def calcular_total():
    total = 0  
    for i in inventario:
        calcular_valor_total = lambda inv: inv[i][0] * inv[i][1]
        total += calcular_valor_total(inventario)
    # calcular_valor_total = lambda inv: sum(precio*cantidad for precio, cantidad in inv.values())
    print(f'El valor total del inventario es {total}')
calcular_total()
def menu_funciones():
    print('1. Añadir productos\n2. Consultar productos\n3. Actualizar precios\n4. Eliminar productos\n5. Calcular el valor total del inventario')
menu_funciones()
while True:
    try:
        opcion:int = int(input('Ingresa el número de la opción a elegir\n'))
        if opcion > 5 or opcion < 1:
            print("La opción seleccionada no existe")
            continue
        else:
            break
    except ValueError:
        print("El dato ingresado no es un número")
if opcion == 1:
    while True:
        try:
            producto:str = input('')
            precio: float = int(input(''))
            cantidad: int = float(input(''))
            añadir_producto()
        except ValueError:
            print('')



inventario: dict = {}
def añadir_producto(product: str, precio:float, amount: int):
    if product not in inventario:
        inventario[product] = (precio, amount)
        print(f'El producto ha sido agregado exitosamente\n')
    else:
        print('El producto ya existe. Para actualizar dirigete al menú y selecciona "Actualizar precios"')
def consultar_producto(product: str):
    if product in inventario:
        print(f'Producto: {product}\nPrecio: {inventario[product][0]}\nCantidad: {inventario[product][1]}\n')
    else:
        print('El producto que has buscado no existe')
def actualizar_producto(product:str,precio:float):
    if product in inventario:
        inventario[product] = (precio, inventario[product][1])
        print('Producto actualizado exitosamente\n')

    else:
        print('El producto ingresado no existe. Dirígete a "Añadir producto\n"')
def eliminar_producto(product: str):
    if product in inventario:
        del inventario[product]
        print('Producto eliminado exitosamente\n')
    else:
        print('El producto que quieres eliminar no existe\n')

def calcular_total():
    total = 0  
    for i in inventario:
        calcular_valor_total = lambda inv: inv[i][0] * inv[i][1]
        total += calcular_valor_total(inventario)
    # calcular_valor_total = lambda inv: sum(precio*cantidad for precio, cantidad in inv.values())
    if total != 0:
        print(f'El valor total del inventario es {total}\n')
    else:
        print('\nEl inventario está vacío\n')
def menu_productos_existentes():
    for producto in inventario:
        precio = inventario[producto][0]
        cantidad = inventario[producto][1]
        print(f'')
def menu_funciones():
    print('1. Añadir productos\n2. Consultar productos\n3. Actualizar precios\n4. Eliminar productos\n5. Calcular el valor total del inventario\n6. Salir')

while True:
    try:
        menu_funciones()
        opcion:int = int(input('Ingresa el número de la opción a elegir\n'))
        if opcion == 1:
            while True:
                try:
                    producto:str = input('Ingresa el nombre del producto\n').lower().strip()
                    while True:
                        precio: float = float(input('Ingresa el precio\n'))
                        if precio < 0:
                            print('El precio debe ser un número positivo')
                            continue
                        else:
                            break
                    while True:
                        cantidad: int = int(input('Ingresa la cantidad\n'))
                        if cantidad < 0:
                            print('La cantidad debe ser un número positivo')
                            continue
                        else:
                            break
                    añadir_producto(product= producto, precio= precio, amount= cantidad)
                    break
                except ValueError:
                    print('Uno(o varios) de los datos ingresados no es correcto. Precio y cantidad deben ser números')
        elif opcion == 2:          
            producto: str = input('Ingresa el nombre del producto a buscar\n').lower().strip()
            consultar_producto(producto)
        elif opcion == 3:
            try:
                producto:str = input('Ingrese el nombre del producto que desea actualizar\n').lower().strip()
                while True:
                        precio: float = int(input('Ingresa el precio nuevo\n'))
                        if precio < 0:
                            print('El precio debe ser un número positivo')
                            continue
                        else:
                            break
                actualizar_producto(producto, precio)
            except ValueError:
                print('El precio debe ser un número')
        elif opcion == 4:
            producto:str = input('Ingrese el nombre del producto que desea eliminar').lower().strip()
            eliminar_producto(producto)
        elif opcion == 5:   
            calcular_total()
        elif opcion == 6:
            break
        if opcion > 6 or opcion < 1:
            print("La opción seleccionada no existe")
            continue
    except ValueError:
        print("El dato ingresado no es un número")




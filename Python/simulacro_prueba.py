biblioteca: dict = {}
totalExistencias:str = 'Copias totales'
cantidadDisponible:str = 'Cantidad disponible'
generos: list[str] = ['Fiction', 'Non-Fiction', 'Science', 'Biography', 'Children']
def añadir_libro(titulo:str = '', autor:str = '', cantidad:int = 0, genero:str =''):      
        biblioteca[titulo] = {'Titulo': titulo,'Autor': autor, cantidadDisponible: cantidad, 'Genero': genero, totalExistencias: cantidad}
añadir_libro('Inferno','Aurelio',5,'Fiction' )
añadir_libro('Terreneitor','Aurelio',5,'Biography' )

def buscar_libro(titulo:str):
        try:
            print(biblioteca[titulo])
        except:
              print('El libro que has buscado no existe')
def prestamo_libro(titulo:str):
        if biblioteca[titulo][cantidadDisponible] > 0:
            biblioteca[titulo][cantidadDisponible] -= 1
        else: 
            print('No hay existencias disponibles en este momento')
def seleccion_genero(option: str)->str:
        if option == 1:
            return generos[0]
        elif option == 2:
            return generos[1]  
        elif option == 3:
            return generos[2]  
        elif option == 4:
            return generos[3]  
        elif option == 5:
            return generos[4] 
        else:
            print('\nLa opción seleccionada no existe\n')
def menu_generos():
    print(f'Género:\n1. Fiction\n2. Non-Fiction\n3. Science\n4. Biography\n5. Children ')
def menu_funciones():
     print('1. Añadir libros a la biblioteca\n2. Buscar libros por título\n3. Registrar préstamo de libros\n4. Devolver libros\n5. Eliminar libros del catálogo\n6. Listar libros por género\n7. Mostrar resumen de inventario')
# opcion:int = 0
# while  opcion <= 0 or opcion > 5:
#     try:
#       menu_generos() 
#       opcion = int(input('Ingrese el número de la opción que desea elegir\n'))
#       genero = seleccion_genero(opcion)       
#     except ValueError:
#         print('El dato ingresado no corresponde a ninguna opcion')
# print(genero)
                
def devolver_libro(titulo:str):
        if biblioteca[titulo][cantidadDisponible] == biblioteca[titulo][totalExistencias]:
            print('Todas las copias del libro ya han sido devueltas anteriormente')
        else:
               biblioteca[titulo][cantidadDisponible] += 1

def eliminar_libro(titulo:str):
        if biblioteca[titulo][cantidadDisponible] == biblioteca[titulo][totalExistencias]:
              del biblioteca[titulo]
        else:
               print('Aún faltan copias por devolver')
def listar_por_genero(genero:str):
      print(f'Títulos del género {genero}')
      for i in biblioteca:
            if biblioteca[i]['Genero'] == genero:
                print(f'- {i}')
                  
def inventario_biblioteca():
    totalLibros:int = 0
    copiasDisponibles: int = 0
    for i in biblioteca:
        totalLibros += biblioteca[i][totalExistencias]
        copiasDisponibles += biblioteca[i][cantidadDisponible]
    print(f'Cantidad total de libros: {totalLibros} \nCopias disponibles: {copiasDisponibles}')
while True:
      menu_funciones()
      try:
            seleccion_funcion = int(input('Ingresa el número de la opción a elegir\n'))
      except ValueError:
            print('El dato ingresado no es un número. Por favor vuelve a intentarlo')
            
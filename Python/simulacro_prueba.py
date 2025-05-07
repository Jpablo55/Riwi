biblioteca: dict = {}
totalExistencias:str = 'Copias totales'
cantidadDisponible:str = 'Cantidad disponible'
generos: list[str] = ['Fiction', 'Non-Fiction', 'Science', 'Biography', 'Children']
def añadir_libro(titulo:str = '', autor:str = '', cantidad:int = 0, genero:str =''):
        for i in generos:
            if i   
        #biblioteca[titulo] = {'Titulo': titulo,'Autor': autor, cantidadDisponible: cantidad, 'Genero': genero, totalExistencias: cantidad}
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
"""
1. Determinar el estado de aprobación:
    a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100).
    b. Evaluar si está aprobada o reprobada basándose en la calificación
    ingresada.
"""
def resultadoCalificacion():
    rangoMax: int = 100
    rangoMin: int = 0
    while True:
        try:
            calificacion:float = float(input("Ingrese su calificación (0 a 100)\n"))
            if calificacion > rangoMax or calificacion < rangoMin:
                print("El número ingresado está fuera del rango")
                continue
            if calificacion >= 60:
                print("Aprobaste!!")
                break
            else:
                print("Reprobaste")
                break
        except ValueError:
            print("El dato ingresado no es un número")

"""
2. Calcular el promedio:
    a. Permitir al usuario ingresar una lista de calificaciones (separadas por
    comas).
    b. Calcular y mostrar el promedio de las calificaciones en la lista.
"""
def promedio():
    calificaciones: list = []    
    while True:
        try:
            calificacionesIngresadas: str =  input("Ingresa las calificaciones para calcular el promedio. Sepáralas por comas (ejemplo: 2, 25,57,80,5)\n")
            calificaciones_separadas: list[str] = calificacionesIngresadas.split(",")
            sumaCalificaciones:float = 0
            try:
                for calificacion in calificaciones_separadas:
                    calificacionSinEspacios: str = calificacion.strip()
                    calificacionFloat: float = float(calificacionSinEspacios)
                    calificaciones.append(calificacionFloat)
                    sumaCalificaciones += float(calificacion)
                promedioCal:float = sumaCalificaciones/calificaciones.__len__()
                print(f"El promedio de tus calificaciones fue {promedioCal:.1f}")
            except ValueError:
                print("Alguno de los datos ingresados no es un número ")
                continue
        except ValueError:
                print("El dato ingresado no es un número")
        break    

"""
3. Contar calificaciones mayores que un valor específico:
    a. Solicitar al usuario un valor numérico.
    b. Contar y mostrar cuántas calificaciones en la lista son mayores que ese
    valor.
"""
def calificacionesMayores():
    calificaciones: list[float] = [55,54.4,59.9,60,99,87,4,33,2,52,40,30,21,25,19,13,12,10]
    calificaciones_mayores: list[float] = []
    try:
        numeroIngresado:float = float(input("Ingrese un número \n"))
        for calificacion in calificaciones:
            if calificacion > numeroIngresado:
                calificaciones_mayores.append(calificacion)
        print(f"Hay {calificaciones_mayores.__len__()} calificaciones mayores a {numeroIngresado} \n \
              ")
        if not not calificaciones_mayores:
            contador = 1
            for  calificacion in calificaciones_mayores:
                print(f"{contador}#  {calificacion}")
                contador += 1
    except ValueError:
        print("El dato ingresado no es un número")

"""
4. Verificar y contar calificaciones específicas:
    a. Permitir al usuario ingresar una lista de calificaciones (separadas por
    comas) y una calificación específica.
    b. Contar y mostrar cuántas veces aparece dicha calificación en la lista.
"""
def conteoCalificacion():
    calificaciones: list = []    
    while True:
        try:
            calificacionesIngresadas: str =  input("Ingresa una lista de calificaciones. Sepáralas por comas (ejemplo: 2, 25,57,80,5)\n")
            calificacionEspecifica: float = float(input("Ingresa una calificación específica \n")) 
            calificaciones_separadas: list[str] = calificacionesIngresadas.split(",")
            cantidadDeCoincidencias: int = 0
            try:
                for calificacion in calificaciones_separadas:
                    calificacionSinEspacios: str = calificacion.strip()
                    calificacionFloat: float = float(calificacionSinEspacios)
                    calificaciones.append(calificacionFloat)
                    if calificacionFloat == calificacionEspecifica:
                        cantidadDeCoincidencias +=1
                
                print(f"{calificacionEspecifica} aparece {cantidadDeCoincidencias} veces en la lista de calificaciones")
            except ValueError:
                print("Alguno de los datos ingresados no es un número ")
                continue
        except ValueError:
                print("El dato ingresado no es un número")
        break    

#Menú de selección
menu = "\
1. Determinar el estado de aprobación\n\
2. Calcular el promedio\n\
3. Contar calificaciones mayores que un valor específico\n\
4. Verificar y contar calificaciones específicas\n\
\n(Para salir, ingrese cualquier otro caracter)"
print(menu)
opcion = input("Ingrese el número de la opción que desea elegir\n")
if opcion == "1":
    resultadoCalificacion()
elif opcion == "2":
    promedio()
elif opcion == "3":
    calificacionesMayores()
elif opcion == "4":
    conteoCalificacion()
else:
    print("Eso es todo. Hasta una próxima 👋")

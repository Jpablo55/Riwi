"""1. Determinar el estado de aprobación:
a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100).
b. Evaluar si está aprobada o reprobada basándose en la calificación
ingresada.
2. Calcular el promedio:
a. Permitir al usuario ingresar una lista de calificaciones (separadas por
comas).
b. Calcular y mostrar el promedio de las calificaciones en la lista.
3. Contar calificaciones mayores que un valor específico:
a. Solicitar al usuario un valor numérico.
b. Contar y mostrar cuántas calificaciones en la lista son mayores que ese
valor.
4. Verificar y contar calificaciones específicas:
a. Permitir al usuario ingresar una lista de calificaciones (separadas por
comas) y una calificación específica.
b. Contar y mostrar cuántas veces aparece dicha calificación en la lista."""
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
def promedio():
    calificaciones: list = []    
    while True:
        try:
            calificacionesIngresadas: str =  input("Ingresa las calificaciones para calcular el promedio. Sepáralas por comas (ejemplo: 2, 25,57,80,5)\n")
            calificaciones_separadas: list[str] = calificacionesIngresadas.split(",")
            print()
            try:
                for calificacion in calificaciones_separadas:
                    calificacionSinEspacios: str = calificacion.strip()
                    calificacionFloat: float = float(calificacionSinEspacios)
                    calificaciones.append(calificacionFloat)
                
            except ValueError:
                print("Alguno de los datos ingresados no es un número ")
                continue
        except ValueError:
                print("El dato ingresado no es un número")
        break    
promedio()
    
# Determinar el estado de aprobación:
# Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
while True:
    try:
        calificacion = float(input("Ingrese la califición \n"))
        if(calificacion >= 0 and calificacion <=100):
            break
        else:
            print("El número ingresado no está dentro del rango")
    except ValueError:
        print("El valor ingresado no es un número")
if calificacion >= 60:
    print("Has aprobado la materia!!🫡")
else:
    print("Lo siento. Reprobaste 😵‍💫")
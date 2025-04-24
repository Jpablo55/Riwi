#Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.
experienciaLaboral = input('Tienes experiencia laboral? Escribe "Si" o "No" ')
tituloUniversitario = input('Tienes título universitario? Escribe "Si" o "No" ')
valExperiencia = False
valTitulo = False
if experienciaLaboral == "Si" or experienciaLaboral == "si":
    valExperiencia = True
if tituloUniversitario == "Si" or tituloUniversitario == "si":
    valTitulo = True
if valTitulo or valExperiencia:
    print("Puedes aplicar a la oferta laboral")
else: 
    print("No puedes aplicar a la oferta laboral")

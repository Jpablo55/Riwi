gestion_vuelos:dict = {
    'AOK-029':{
        'origen':'Medellín',
        'destino':'Budapest',
        'asientos disponibles':['A2','B1','C2','D2','G3'],
        'asientos ocupados':[],
        'horario':(16,50)
    }
}
print(gestion_vuelos['AOK-029']['asientos disponibles'])
def reserva_asientos(codigo_vuelo:str, numero_asiento:str):
    vuelo: dict = gestion_vuelos[codigo_vuelo]
    asientos_disponibles:dict = vuelo['asientos disponibles']
    if numero_asiento in asientos_disponibles:
        gestion_vuelos[codigo_vuelo]['asientos disponibles'].remove(numero_asiento)
        gestion_vuelos[codigo_vuelo]['asientos ocupados'].append(numero_asiento)
        print('\nSu reserva ha sido completada con éxito.\n')
        print(gestion_vuelos[codigo_vuelo]['asientos disponibles'])
        print(gestion_vuelos[codigo_vuelo]['asientos ocupados'])
    else:
        print('El asiento no está disponible')
reserva_asientos('AOK-029', 'A2')

def calculo_porcentaje_ocupado(codigo_vuelo):
    cantidad_ocupados:int = len(gestion_vuelos[codigo_vuelo]['asientos ocupados'])
    cantidad_disponibles:int = len(gestion_vuelos[codigo_vuelo]['asientos disponibles'])
    total_asientos:int = cantidad_ocupados + cantidad_disponibles
    porcentaje_ocupados:float = (cantidad_ocupados * 100)/total_asientos
    print(f'Asientos ocupados: {porcentaje_ocupados}%')
calculo_porcentaje_ocupado('AOK-029')
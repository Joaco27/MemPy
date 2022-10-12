import datetime
from src.handlers import csvActual
def tema():
    """Devuelve la tematica/criterio del dia"""
    
    nro_dia = datetime.datetime.today().weekday()
    dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    mañana, tarde =  [(0, 12), (13, 23) ]
    criterios_data = {}

    for dia in dias_semana:
        criterios_data[dia] = {mañana:{}, tarde: {}}


    hora = datetime.datetime.now().hour
    dia_semana =  dias_semana[nro_dia]

    rango = mañana if hora in mañana else tarde

    criterios_data['lunes'][mañana] = {'criterio':'Paises del mundo con menor poblacion','CSV':'countries of the worldMenos.csv'}
    criterios_data['lunes'][tarde] = {'criterio':'Autos Uno','CSV':'AutosUno.csv'}
    criterios_data['martes'][mañana] = {'criterio':'Animales Vertebrados','CSV':'animalesVertebrados.csv'}
    criterios_data['martes'][tarde] = {'criterio':'Paises del mundo con mayor poblacion','CSV':'countries of the world.csv'}
    criterios_data['miercoles'][mañana] = {'criterio':'Autos Dos','CSV':'AutosDos.csv'}
    criterios_data['miercoles'][tarde] = {'criterio':'Animales invertebrados','CSV':'animalesInvertebrados.csv'}
    criterios_data['jueves'][mañana] = {'criterio':'Paises del mundo con menor poblacion','CSV':'countries of the worldMenos.csv'}
    criterios_data['jueves'][tarde] = {'criterio':'Autos Uno','CSV':'AutosUno.csv'}
    criterios_data['viernes'][mañana] = {'criterio':'animales vertebrados','CSV':'animalesVertebrados.csv'}
    criterios_data['viernes'][tarde] = {'criterio':'Paises del mundo con mayor poblacion','CSV':'countries of the world.csv'}
    criterios_data['sabado'][mañana] = {'criterio':'Autos Dos','CSV':'AutosDos.csv'}
    criterios_data['sabado'][tarde] = {'criterio':'Animales invertebrados','CSV':'animalesInvertebrados.csv'}
    criterios_data['domingo'][mañana] = {'criterio':'animales vertebrados','CSV':'animalesVertebrados.csv'}
    criterios_data['domingo'][tarde] = {'criterio':'Paises del mundo con menor poblacion','CSV':'countries of the worldMenos.csv'}
    
    nombre=criterios_data[dia_semana][rango]['CSV']
    csvActual.setCsv(nombre)

    return criterios_data[dia_semana][rango]['criterio']

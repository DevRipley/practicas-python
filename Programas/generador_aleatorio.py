# Crea un módulo llamado generador_aleatorio 
# que incluya una función para generar números 
# aleatorios dentro de un rango especificado. 

import random # Importamos la libreria necesaria para la magia

# Definimos [min] y [max] que sera el rango de el numero aleatorio que queremos obtener.
def generar_numero_aleatorio(min, max):
    
    # Devolvemos con la funcion random entero dentro de min hasta max
    return random.randint(min, max)
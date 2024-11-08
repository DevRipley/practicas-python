# Crea un módulo llamado generador_aleatorio 
# que incluya una función para generar números 
# aleatorios dentro de un rango especificado. 

import random # Importamos la libreria necesaria para la magia

# Definimos esta y guardamos en variables de longitud [min] y [max]
def generar_numero_aleatorio(min, max):
    return random.randint(min, max)
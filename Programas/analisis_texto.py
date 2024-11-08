# Utiliza el módulo collections para 
# analizar un texto ingresado por el 
# usuario y contar la frecuencia de 
# cada palabra en el texto.

# Importamos el módulo [collections] y la función [Counter] para la magia
from collections import Counter

espacio = ''

def limpiar_palabra(palabra):
    
    # Eliminamos los caracteres para evitar problemas
    no_te_quiero = ".,;:¡!¿?()[]{}\"'"
    
    palabra = palabra.strip(no_te_quiero)
    
    return palabra

def analizar_texto(texto):
    # Aplicamos la limpieza en cada palabra
    palabras = [limpiar_palabra(p) for p in texto.split()]

    # Contamos la frecuencia de cada palabra
    frecuencia_palabras = Counter(palabras)

    # Esta vez decidi agregar el resultado aqui
    print("Frecuencia de palabras:")
    
    print(espacio)
    
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")

# Pedimos al usuario que digite el texto
texto = input("Ingresa un texto: ")

print(espacio)

# Llamamos a la funcion a hacer su magia
analizar_texto(texto)

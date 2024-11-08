# Crea una función llamada contar_palabras
# que tome una cadena de texto y devuelva
# el número de palabras en esa cadena.

# Definimos la funcion contar_palabras
def contar_palabras(cadena):
    # Divide la cadena en palabras utilizando espacios como separadores
    palabras = cadena.split()
    
    # Cuenta el numero de palabras en la lista ya separada
    numero_palabras = len(palabras)
    
    # Devuelve el numero de palabras
    return numero_palabras

#! EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO

# # Pedimos al usuario que ingrese su texto
# texto = str(input("Por favor, ingresa un texto para contar las palabras: ")) #String

# # Llamamos a la funcion para que haga su magia
# resultado = contar_palabras(texto)

# # Mostramos el resultado
# print(f'Numero de palabras en tu texto: {resultado}')


# Funcion contador de palabras finalizado.
contar_palabras()
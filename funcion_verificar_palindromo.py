#Crea una función llamada es_palindromo 
# que determine si una palabra ingresada 
# por el usuario es un palíndromo o no.

# Definicion de la funcion es_palindromo
def es_palindromo(palabra):
    
    # Convertir la palabra a minusculas para hacer
    # la comparación sin distincion de mayus y minus
    palabra = palabra.lower()
    
    # Verificar si la palabra es un palindromo
    # al compararla con su inversa
    return palabra == palabra[::-1]

#! EJEMPLO EJEMPLO EJEMPLO EJEMPLO

# # Solicitar al usuario que ingrese una palabra
# palabra_usuario = input("Por favor, ingresa una palabra para verificar si es un palíndromo: ")

# # Llamar a la función es_palindromo con el argumento proporcionado por el usuario
# es_palindromo_resultado = es_palindromo(palabra_usuario)

# # Mostrar el resultado al usuario
# if es_palindromo_resultado:
#     print(f'{palabra_usuario} es un palíndromo.')
# else:
#     print(f'{palabra_usuario} no es un palíndromo.')

# Funcion palindromo exitosa!
es_palindromo()
# Desarrolla una función llamada 
# generar_contraseña que genere una contraseña 
# aleatoria de 
# longitud especificada por el usuario.
import random # Importo la biblioteca para obtener caracteres al azar.
import string # Importo la biblioteca para manipular cadenas de texto.

def generar_passwd(longitud):
    # Defino los caracteres posibles para la contraseña.
    caracteres = string.ascii_letters + string.digits  
    
    # Genero la contraseña usando caracteres aleatorios.
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))  
    
    return contraseña

#! EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO

# # Solicito al usuario que ingrese la longitud deseada para la contraseña.
# longitud_contraseña = int(input("Digite su longitud: "))

# # Genero la contraseña y la muestro al usuario.
# nueva_passwd = generar_passwd(longitud_contraseña)

# print("Contraseña generada:", nueva_passwd)

# Guardamos la funcion
generar_passwd()
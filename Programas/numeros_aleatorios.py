# Importamo nuestra funcion [generar_numero_aleatorio] 
# desde nuestro modulo [generador_aleatorio]
from generador_aleatorio import generar_numero_aleatorio

espacio = ''

# Pedimos el rango #1
min = int(input("Digite el valor minimo: ")) #Integer

print(espacio)

# Pedimos el rango #2
max = int(input("Digite el valor minimo: ")) #Integer

print(espacio)

# El resultado guardara nuestra variables y hara su funcion
resultado = generar_numero_aleatorio(min, max)

# Imprimimos el resultado
print(f"Tu numero aleatorio es: {resultado}")
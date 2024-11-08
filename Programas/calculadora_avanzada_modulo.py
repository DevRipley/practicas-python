# Crea un módulo llamado calculadora_avanzada
# que incluya funciones para operaciones
# matemáticas más avanzadas, como exponentes,
# raíces cuadradas, etc. Luego, importa y
# utiliza este módulo en un programa principal.

# Esta vez use este modulo ya que son muy hardcode hacer las funciones y no tengo mucho tiempo.
import math

# Esta funcion es necesaria para sumar
def suma(a, b):
    
    return a + b

# Esta funcion es necesaria para restar 
def resta(a, b):
    
    return a - b

# Esta funcion es necesaria para multiplicar
def multiplicacion(a, b):
    
    return a * b

# Esta funcion es necesaria para dividir
def division(a, b):
    if b == 0:
        print("No se puede dividir entre 0")
        return None  # Puedes elegir devolver None o algún otro valor que indique un error.
    
    else:
        return a / b

# Esta funcion es necesaria para elevar a la potencia
def elevar_potencia(base, exponente):
    
    return math.pow(base, exponente)

# Esta funcion es calcula la raiz cuadrada.
def raiz_cuadrada(numero):
    
    return math.sqrt(numero)

# Funcion para calcular el factorial de un numero
def factorial(numero):
    # Verificamos si el número es negativo
    if numero < 0:
        return "No es posible calcular el factorial de un numero negativo!"
    
# Asignamos que el factorial de 0 y 1 es 1
    elif numero == 0 or numero == 1:
        return 1
    
    # De lo contrario calculamos el factorial recursivamente
    else:
        return numero * factorial(numero - 1)

# Esta funcion calcula el seno de un angulo en grados
def seno(angulo):
    return math.sin(math.radians(angulo))

# Esta funcion calcula el coseno de un angulo en grados
def coseno(angulo):
    return math.cos(math.radians(angulo))

# Esta funcion calcula el coseno de un angulo en grados
def tangente(angulo):
    return math.tan(math.radians(angulo))

# Aqui tenemos nuestras funciones a exportar:

# suma(a, b)

# resta(a, b)

# seno(angulo)

# coseno(angulo)

# tangente(angulo)

# division(a, b)

# factorial(numero)

# multiplicacion(a, b)

# raiz_cuadrada(numero)

# elevar_potencia(base, exponente)




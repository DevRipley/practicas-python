#Implementa una función llamada factorial 
# que calcule el factorial de un numero
# ingresado por el usuario.

# Definimos la funcion factorial

             #Ejemplo
def factorial(numero):
    
    # Declaramos el resultado en 1, ya que el factorial de 0 es 1
    resultado = 1
    
    # iteramos sobre cad numero desde el 1 hasta el numero pedido
    for i in range(1, numero + 1):
        
        # Multiplicar el resultado por el numero actual en la iteracion
        resultado *= i
    
    # Devolver el resultado del factorial
    return resultado

#! EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO EJEMPLO
# # Pedimos un numero
# numero_usuario = int(input("Digita un numero: "))

# # Llamamos a la funcion con el numero ingresado
# resultado_factorial = factorial(numero_usuario)

# print()

# # Mostrar el resultado al usuario
# print(f'El factorial de {numero_usuario} es: {resultado_factorial}')

# Funcion factorial terminada
factorial()
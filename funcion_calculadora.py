# Crea una función llamada calculadora que realice operaciones básicas
# como suma, resta, multiplicación y división. 
# El usuario debe ingresar dos números y la operación deseada.

import os # Importe del sistema

espacio = '' # Declare el espacio por aca!

def calculadora():
    
    # Pedimos dos numeros
    numero1 = float(input("Digite su primer numero: ")) #Floating
    numero2 = float(input("Digite su segundo numero: ")) #Floating

    print(espacio) # Espacio
    
    os.system("cls") # Limpieza del CMD
    
    # Menu principal
    print("""
    ╔════Menu Principal════╗
    ║                      ║ 
    ║  1- Suma             ║ 
    ║                      ║
    ║  2- Resta            ║
    ║                      ║
    ║  3- Multiplicacion   ║
    ║                      ║
    ║  4- Division         ║
    ║                      ║
    ╚══════════════════════╝
    """)

    # Pedimos que ingrese la operacion a realizar
    operacion = int(input("Selecciona tu Operacion [1 , 2, 3, 4]: ")) #Integer

    while True:
        # Realizamos la operación y mostramos el resultado
        if operacion == 1:
            resultado = numero1 + numero2
        elif operacion == 2:
            resultado = numero1 - numero2
        elif operacion == 3:
            resultado = numero1 * numero2
        elif operacion == 4:
            
            # Si el numero 2 y el numero 1 no es igual a 0 = imprimir la division!
            # Esto significa no es igual [!=]
            
            if numero2 != 0:
                resultado = numero1 / numero2

            else:
                # Imprimimos que no es divisible entre 0
                resultado = "No se puede dividir entre 0"

        
        if operacion > 4: # Si la operacion es mayor a 4
            resultado = "Esta operacion no se encuentra en el menu"
        
        if operacion < 1: # Si la operacion es menor a 1
            resultado = "Esta operacion no se encuentra en el menu"               

        print(espacio)
        
        print(f"El resultado es: {resultado}")
        break # Rompemos bucle
    
# Y asi es como creamos una funcion en python:
calculadora()

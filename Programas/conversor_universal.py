# Desde nuestro modulo [conversor_unidades] importamos
# Nuestras funciones

# Importamos las funciones de nuestro modulo de conversion
from conversor_unidades import (
    km_a_millas,
    millas_a_km,
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    gramos_a_kilogramos,
    kilogramos_a_gramos
)

# Importamos el modulo 'os' para limpiar la pantalla
import os

# Creamos una variable para espacios en blanco para mejorar la presentacion
espacio = ''

# Funcion para redondear el resultado a dos decimales y evitar ceros innecesarios
def redondear_resultado(resultado):
    # Verificamos si el resultado tiene más de dos decimales
    decimales = len(str(resultado).split('.')[1]) if '.' in str(resultado) else 0

    # Si hay más de dos decimales, redondeamos a 2
    if decimales > 2:
        resultado = round(resultado, 2)

    # Verificamos si el resultado es un numero entero para evitar ceros innecesarios
    if resultado == round(resultado):
        resultado = int(resultado)

    return resultado

# Iniciamos un bucle infinito para el menu principal
while True:
    # Limpiamos la pantalla para una mejor presentacion
    os.system('cls')

    # Presentamos nuestro programa con un mensaje de bienvenida
    print("🏋️    Bienvenido a el Conversor Universal   🏋️")

    print(espacio)

    # Mostramos el menu de conversiones
    print("""
    ╔════════════════════════════════════╗
    ║        MENU DE CONVERSIONES        ║
    ╠════════════════════════════════════╣
    ║ 1  - Kilometros a Millas 🚗        ║
    ║ 2  - Millas a Kilometros 🛣️         ║
    ║ 3  - Celsius a Fahrenheit 🌡️        ║
    ║ 4  - Fahrenheit a Celsius ❄️        ║
    ║ 5  - Gramos a Kilogramos 🏋️         ║
    ║ 6  - Kilogramos a Gramos ⚖️         ║
    ║ 0  - Salir                         ║
    ╚════════════════════════════════════╝
    """)

    # Pedimos al usuario elegir una opcion
    opcion = int(input("Digita una opcion [0 - 10]: "))  # Convierte la entrada a entero

    # Segun la opcion seleccionada, realizamos la conversion correspondiente
    if opcion == 1:
        os.system('cls')  # Limpiamos la pantalla

        print("Kilometros a Millas 🚗")
        print(espacio)

        # Pedimos al usuario la cantidad en kilometros
        kilometros = float(input("Digita tu cantidad en Km: "))  # Convierte la entrada a flotante

        # Calculamos el resultado y lo redondeamos segun nuestra funcion personalizada
        resultado = redondear_resultado(km_a_millas(kilometros))

        print(espacio)

        # Imprimimos el resultado en millas
        print(f"Cantidad en millas: {resultado}")

        print(espacio)

        # Esperamos a que el usuario presione ENTER antes de continuar
        input("[ENTER] para continuar..")

    # Repetimos la logica para las demás opciones del menu...
    elif opcion == 2:
        os.system('cls')

        print("Millas a Kilometros 🛣️")
        print(espacio)

        millas = float(input("Digita tu cantidad en Millas: "))
        resultado = redondear_resultado(millas_a_km(millas))

        print(espacio)
        print(f"Cantidad en kilometros: {resultado}")
        print(espacio)
        input("[ENTER] para continuar..")

    elif opcion == 3:
        os.system('cls')

        print("Celsius a Fahrenheit 🌡️")
        print(espacio)

        celsius = float(input("Digita tu temperatura en Celsius: "))
        resultado = redondear_resultado(celsius_a_fahrenheit(celsius))

        print(espacio)
        print(f"Temperatura en Fahrenheit: {resultado}° F")
        print(espacio)
        input("[ENTER] para continuar..")

    elif opcion == 4:
        os.system('cls')

        print("Fahrenheit a Celsius ❄️")
        print(espacio)

        fahrenheit = float(input("Digita tu temperatura en Fahrenheit: "))
        resultado = redondear_resultado(fahrenheit_a_celsius(fahrenheit))

        print(espacio)
        print(f"Temperatura en Celsius: {resultado}° C")
        print(espacio)
        input("[ENTER] para continuar..")

    elif opcion == 5:
        os.system('cls')

        print("Gramos a Kilogramos 🏋️")
        print(espacio)

        gramos = float(input("Digita tu cantidad en Gramos: "))
        resultado = redondear_resultado(gramos_a_kilogramos(gramos))

        print(espacio)
        print(f"Cantidad en Kilogramos: {resultado}")
        print(espacio)
        input("[ENTER] para continuar..")

    elif opcion == 6:
        os.system('cls')

        print("Kilogramos a Gramos ⚖️")
        print(espacio)

        kilogramos = float(input("Digita tu cantidad en Kilogramos: "))
        resultado = redondear_resultado(kilogramos_a_gramos(kilogramos))

        print(espacio)
        print(f"Cantidad en Gramos: {resultado}")
        print(espacio)
        input("[ENTER] para continuar..")

    elif opcion == 0:
        os.system('cls')

        print("""Gracias por utilizar mi programa! 
                
Nombre: Luis Dariel 
                
Matricula: 1-21-9673""")
        break

    else:
        print("Ingresa una opcion valida")  # Mensaje en caso de opcion no válida

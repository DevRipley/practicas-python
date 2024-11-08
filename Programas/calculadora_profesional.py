# Importare todo sobre el modulo calculadora_avanzada

from calculadora_avanzada_modulo import suma, resta, multiplicacion, division, seno, coseno, tangente, factorial, raiz_cuadrada, elevar_potencia

import os # Para la limpieza

espacio = '' # Para los espacios

resultado = 0 # Iniciamos la variable

while True:
    os.system("cls")
    
    # Bienvenida
    print("""
╔──────────────────────────────────────────────────────────────────────────────╗
│   ______ ___     __    ______ __  __ __     ___     ____   ____   ____   ___ │
│  / ____//   |   / /   / ____// / / // /    /   |   / __ \ / __ \ / __ \ /   |│
│ / /    / /| |  / /   / /    / / / // /    / /| |  / / / // / / // /_/ // /| |│
│/ /___ / ___ | / /___/ /___ / /_/ // /___ / ___ | / /_/ // /_/ // _, _// ___ |│
│\____//_/  |_|/_____/\____/_\____//_____//_/  |_|/_____/ \____//_/_|_|/_/__|_|│
│   / __ \ / __ \ / __ \ / ____// ____// ___/ /  _// __ \ / | / //   |   / /   │
│  / /_/ // /_/ // / / // /_   / __/   \__ \  / / / / / //  |/ // /| |  / /    │
│ / ____// _, _// /_/ // __/  / /___  ___/ /_/ / / /_/ // /|  // ___ | / /___  │
│/_/    /_/ |_| \____//_/    /_____/ /____//___/ \____//_/ |_//_/  |_|/_____/  │
╚──────────────────────────────────────────────────────────────────────────────╝
""")
    

    print(espacio)
    
    texto = """
                        ╔════════════════════════════╗
                        ║      Menú de Opciones      ║
                        ╠════════════════════════════╣
                        ║ 1. Elevar Potencia         ║
                        ║ 2. Raíz Cuadrada           ║
                        ║ 3. Factorial               ║
                        ║ 4. Seno                    ║
                        ║ 5. Coseno                  ║
                        ║ 6. Tangente                ║
                        ║ 7. Suma                    ║
                        ║ 8. Resta                   ║
                        ║ 9. Multiplicación          ║
                        ║ 10. División               ║
                        ║ 0. Salir                   ║
                        ╚════════════════════════════╝
    """

    
    
    def imprimir_texto_centro(texto):
        ancho_terminal = 80  # Ajusta este valor al ancho de tu terminal o ventana de consola
        texto_centro = texto.center(ancho_terminal)
        print(texto_centro)
    
    imprimir_texto_centro(texto)
    
    # Pedimos al usuario elegir una opcion
    decision = int(input("                         Digita una opcion [0 - 10]: ")) #Integer

    os.system("cls")

    # Rompemos el bucle si la decision es 0
    if decision == 0:
        print("""Gracias por utilizar mi programa! 
              
Nombre: Luis Dariel 
              
Matricula: 1-21-9673""")
        break

    # Pedimos valores para la operacion
    
    # Amplie un poco mis conocimientos y decodo hacer esto ya que ps hacer el codigo mas simple y 
    # menos codigo es lo que se busca
    # Para mas facil decidi agregar el input ya que estos son iguales:
    if decision in [4, 5, 6]:
        angulo = float(input("Digite el valor del angulo: ")) 
        
        print(espacio)
        
    if decision in [1]:
        base = float(input("Digita tu base: ")) # Floating
        
        print(espacio)
        
        exponente = float(input("Digita tu exponente: ")) # Floating
        
        print(espacio)
        
        resultado = elevar_potencia(base, exponente)

    elif decision in [2]:
        os.system("cls")
        
        print("Calcula tu Raiz cuadrada")
        
        print(espacio)
        
        numero = float(input("Digita tu numero: ")) # Floating
        
        resultado = raiz_cuadrada(numero)

    elif decision in [3]:
        os.system("cls")
        
        print("Calcula tu Factorial")
        
        print()
        
        numero = int(input("Digita tu numero: ")) # Integer
        
        resultado = factorial(numero)

    elif decision in [4]:
        # Estos no tendran un print ya que los agregue alla arriba para mas rapidez
        resultado = seno(angulo)

    elif decision in [5]:
        resultado = coseno(angulo)

    elif decision in [6]:
        resultado = tangente(angulo)

    elif decision in [7, 8, 9, 10]:
        # Pedimos el primer numero
        a = float(input("Digita tu 1er numero: ")) #Floating
        
        print(espacio)
        
        # Pedimos el segundo numero
        b = float(input("Digita tu 2do numero: ")) #Floating

        # Estos tampoco tendran prints ya que habra overlaping con el input y no me gusta:
        if decision == 7:
            resultado = suma(a, b)
            
        elif decision == 8:
            resultado = resta(a, b)
            
        elif decision == 9:
            resultado = multiplicacion(a, b)
            
        elif decision == 10:
            resultado = division(a, b)

    else:
        print("Opcion incorrecta, escoje una del 0 al 10.")

    print(espacio)
    
    # Utilize CHATGPT para que me ayude con este codigo, par asi verificar si el resultado tiene mas de dos decimales.
    decimales = len(str(resultado).split('.')[1]) if '.' in str(resultado) else 0

    # De ser asi que decimales sea mayor que 2 redondeamos a 2.
    if decimales > 2:
        resultado = round(resultado, 2)
        
    if resultado == round(resultado): # Esto verificara si el resultado es un numero entero para que asi no me lo exporte con 0 siendo entero.
     resultado = int(resultado)
    
    # Mostramos el resultado de cada operacion
    print(f"Resultado: {resultado}")
    
    print(espacio)
    
    #! DESEO DE SEGUIR DESEO DE SEGUIR DESEO DE SEGUIR DESEO DE SEGUIR
    
    deseo = input("Desea realizar otra operacion [SI, NO]: ")
    
    deseo = deseo.lower() # minuscula
    
    # Si deseo es igual a no:
    if deseo != "si":
        os.system('cls')
        
        print("""Gracias por utilizar mi programa! 
              
Nombre: Luis Dariel 
              
Matricula: 1-21-9673""")
        break
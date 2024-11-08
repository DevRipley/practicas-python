from operaciones_matematicas import suma, resta, multiplicacion, division
import os

while True:
    print("""
    ╔════════════════════════════╗
    ║      Menú de Opciones      ║
    ╠════════════════════════════╣
    ║ 1. Suma                    ║
    ║ 2. Resta                   ║
    ║ 3. Multiplicación          ║
    ║ 4. División                ║
    ║ 0. Salir                   ║
    ╚════════════════════════════╝
    """)

    espacio = ""

    print(espacio)

    opcion = int(input("Ingrese su opcion realizar (1-4): "))

    print(espacio)

    if opcion in [1, 2, 3, 4]:
        num1 = int(input("Ingrese su primer numero: "))
        
        print(espacio)
        
        num2 = int(input("Ingrese su segundo numero: "))
        
        if opcion == 1:
            resultado = suma(num1, num2)
        
        elif opcion == 2:
            resultado = resta(num1, num2)
        
        elif opcion == 3:
            resultado = multiplicacion(num1, num2)
        
        elif opcion == 4:
            resultado = division(num1, num2)

        print(espacio)
        
        print(f"Resultado: {resultado}")
        
        print(espacio)
        
        input("[Enter] para continuar..")
        
        os.system("cls")
        
    elif opcion == 0:
        print("Gracias por utilizar nuestro programa!")
        break

    else:
        print("Operacion incorrecta")
        
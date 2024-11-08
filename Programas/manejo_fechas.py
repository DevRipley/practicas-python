# Importamos el datetime
import os
import datetime

# Espacio epico
espacio = ''

# Obtenemos la fecha de el modulo
fecha_hora_actual = datetime.datetime.now()

# Declaramos que formato es igual a la fecha_hora_actual
# Use .strftime para formatear la fecha y hora en un formato legible.

# GUIA DE FORMATO

#----FECHA------
# %d Dias 
# %m Meses
# %Y Año

#----HORA-------
# %H Año
# %M Minutos
# %S Segundos

# Formato
print(espacio)

# Formatear la fecha y hora en un formato legible de 12 horas
formato_12h = fecha_hora_actual.strftime("""Hora: %I:%M:%S %p
Fecha: %d/%m/%Y""")

formato_24h = fecha_hora_actual.strftime("""Hora: %H:%M:%S
Fecha: %d/%m/%Y""")

while True:
    os.system('cls')
    
    print("""
    ╔════════════════════════╗
    ║         MENÚ           ║
    ╠════════════════════════╣
    ║ 1. Formato 24 horas ⏰ ║
    ║ 2. Formato 12 horas 🕒 ║
    ║ 3. Formato Default  🎫 ║
    ║ 4. Salir 👋            ║
    ╚════════════════════════╝
    """)

    # Pedimos al usuario digitar la opcion del menu
    decision = int(input("Digita tu opcion: ")) #Integer

    if decision == 1:
        os.system('cls')
        
        # Ahora imprimimos la fecha en un formato 24hrs
        print(f"""Hora en Republica Dominicana 24hrs""")
        
        print(espacio)
        
        print(formato_24h)
        
        print(espacio)
        
        input("[ENTER] para continuar..")

    elif decision == 2:
        os.system('cls')
        
        # Ahora imprimimos la fecha en un formato 12hrs
        print(f"""Hora en Republica Dominicana 12hrs""")
        
        print(espacio)
        
        print(formato_12h)
        
        print(espacio)
        
        input("[ENTER] para continuar..")
        
    elif decision == 3:
        os.system('cls')
        
        # Imprimimos la fecha sin formato. [default]
        print(f"Fecha default: {fecha_hora_actual}")
        
        print(espacio)
        
        input("[ENTER] para continuar..")
        
    elif decision == 4:
        os.system('cls')
        
        print("""Gracias por utilizar mi programa! 
                
Nombre: Luis Dariel 
                
Matricula: 1-21-9673""")
        break
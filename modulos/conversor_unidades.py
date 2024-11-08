# Diseña un módulo llamado conversor que tenga funciones
# para convertir entre diferentes unidades de medida
# (por ejemplo, de kilómetros a millas o de Celsius a Fahrenheit). 
# Importa y utiliza este módulo en un programa principal.

# Kilometros a millas:
def km_a_millas(kilometros):
    conversion_km = 0.621371
    
    millas = kilometros * conversion_km
    return millas

# Millas a Kilometros
def millas_a_km(millas):
    conversion_m = 1.60934
    
    kilometros = millas * conversion_m
    
    return kilometros

# Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Gramos a Kilogramos
def gramos_a_kilogramos(gramos):
    kilogramos = gramos * 1000
    return kilogramos

# Kilogramos a Gramos
def kilogramos_a_gramos(kilogramos):
    gramos = kilogramos / 1000
    return gramos

# Todas mis funciones
km_a_millas()
millas_a_km()
celsius_a_fahrenheit()
fahrenheit_a_celsius()
gramos_a_kilogramos()
kilogramos_a_gramos()
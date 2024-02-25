# usan los operadores basicos para hacer operaciones matematicas 
suma = 1 + 2
resta = 2 -1
multiplicacion = 2 * 2
Division = 9 / 3
print (suma)
print (resta)
print (multiplicacion)
print (Division)

#doble diagonal se usa para dividir y redondear el numero al inferior mas cercano
minutos = 1042
simple = minutos / 60
doble = minutos // 60
print ( 'simple ' , simple )
print ( 'doble ' , doble )

#operador modulo da el resto de la division
print (10 % 3 )

# Orden de las operaciones
# Python respeta el orden de las operaciones en matematicas. 
# El orden de las operaciones determina que las expresiones se deben evaluar en este orden:
#    Parentesis
#    Exponentes
#    Multiplicacion y division
#    Suma y resta

result_1 = 1032 + 26 * 2
print(result_1)

result_2 = 1032 + (26 * 2)
print(result_2)

# Se pueden convertir valores de cadena a int o float
# En caso de que la cadena contenga valores no permitidos para int o float, marcara error

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# round redondea el valor despues de .5 hacia arriba y menor a .5 hacia abajo
print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))

# la biblioteca math ayuda a redondear los valores, usando ceil para redondear hacia arriba y floor hacia abajo
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# ejercicio donde se inserta una cadena desde el teclado, se convierte a int, se hace una operacion y se convierte a valor absoluto
first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)
distance_km = second_planet - first_planet
print(abs(distance_km))
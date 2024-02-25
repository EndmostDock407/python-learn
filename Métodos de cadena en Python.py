# Se usa el metodo .title para hacer que la primer letra de cada palabra sea mayuscula
print("temperatures and facts about the moon".title())
print ("-----------------------------------------------------------------")
# el metodo .title tambien se puede aplicar a variables
heading = "temperatures and facts about the moon\n"
heading_upper = heading.title()
print(heading_upper)
print ("-----------------------------------------------------------------")

# Un método de cadena común es .split(). Sin argumentos
# el método separará la cadena en cada espacio. Esto crearía una lista de todas las palabras o números separados por un espacio:
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
print ("-----------------------------------------------------------------")

# en este caso hace la divicion de palabras/numeros en base al \n
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)
print ("-----------------------------------------------------------------")

# el metodo in buscara la plabra en la cadena otorgada y mandará un true o false en caso de encontrar o no la palabra
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")
print ("-----------------------------------------------------------------")

# Un enfoque para buscar la posición de una palabra específica en una cadena consiste en usar el método .find():
# va a devolver -1 si no encuentra la palabra
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
print ("-----------------------------------------------------------------")

# en caso de encontrar la plabra mostrará la posicion de ella, tomando en cuenta caracteres/numeros o espacios
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
print ("-----------------------------------------------------------------")

# Otra manera de buscar contenido consiste en usar el método .count(), que devuelve el número total de repeticiones
# de una palabra determinada en una cadena:
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
print ("-----------------------------------------------------------------")

# metodo .lower convierte minusculas todo
print("The Moon And The Earth".lower())
print ("-----------------------------------------------------------------")
# metodo .upper convierte todo a minusculas
print("The Moon And The Earth".upper())
print ("-----------------------------------------------------------------")
# El código anterior confía en que todo lo que hay después de los dos puntos (:)
# es una temperatura. La cadena se divide en :, lo que genera una lista de dos elementos. 
# El uso de [-1] en la lista devuelve el último elemento que, en este ejemplo, es la temperatura.
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
print ("-----------------------------------------------------------------")
# Si el texto es irregular, no puede usar los mismos métodos de división para obtener el valor. 
# Debe recorrer en bucle los elementos y comprobar si los valores son de un tipo determinado. 
# Python tiene métodos que ayudan a comprobar el tipo de cadena:
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
print ("-----------------------------------------------------------------")
# se usa el metodo .startswitch con el guion, para que el texto detecte el valor negativo
# ya que el guion se agrega como valor negativo
print("-60".startswith('-'))
print ("-----------------------------------------------------------------")
# como el simbolo está al final, se usa .endswitch 
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
print ("-----------------------------------------------------------------")
# se usa .replace para remplazar el primer valor dado por el segundo, haciendo modificaciones necesarias para la cadena
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
print ("-----------------------------------------------------------------")
# El método .join() necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es 
# diferente al de otros métodos de cadena: 
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
print ("-----------------------------------------------------------------")

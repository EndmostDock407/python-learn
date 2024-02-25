# El marcador de posición de la variable de la cadena es %s. Después de la cadena, use otro carácter % seguido del nombre de la variable. 
# En el ejemplo siguiente, se muestra cómo dar formato mediante el carácter %:
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
#Se hace lo mismo que lo anterior pero se usa varios elementos a sustituir
print("""\nBoth sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# se usa el metodo .format y el uso de llaves para remplazar valores
mass_percentage = "1/6"
print("\nOn the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
# En este caso, se puede ver que es menos probable que salgan errores de posicion ya que el metodo .format establece posiciones con numeros
mass_percentage = "1/6"
print("""\nYou are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
# el metodo .format tambien acepta palabras en vez de numeros para agregar claridad al texto
mass_percentage = "1/6"
print("""\nYou are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))
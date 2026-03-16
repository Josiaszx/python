# modulos -> archivo que contiene codigo reutilizable (funciones, clases, variables)
from math import pi as PI_VALUE # importar solo el valor de pi y renombrarlo como PI_VALUE
import math # importar todo el modulo math

print("Valor de pi usando math:", math.pi) # 3.141592653589793
print("Valor de pi usando PI_VALUE:", PI_VALUE) # 3.141592653589793

from clases import Persona # importar la clase Persona del modulo clases
persona = Persona("Carlos", "Gomez", 31)
print(persona.saludar()) # Hola, me llamo Carlos Gomez y tengo 31 años.
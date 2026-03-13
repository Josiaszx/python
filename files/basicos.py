# Comentario

"""
    Comentario en 
    varias lineas
"""

# Variables (snake_case)
nombre = "Juan" # String
apellido, alias = "Perez", "JP" # Multiple assignment
edad = 30 # Integer
altura = 1.75 # Float
es_estudiante = True # Boolean
none = None # NoneType (valor nulo)

# cheqear tipos de datos ... type()
print(type(nombre)) # <class 'str'>
print(type(edad)) # <class 'int'>   
print(type(altura)) # <class 'float'>
print(type(es_estudiante)) # <class 'bool'>
print(type(none)) # <class 'NoneType'>

# build-in functions (funciones predefinidas)
print(len(nombre)) # 4
print(str(edad)) # '30'
print(int(altura)) # 1
print(float(edad)) # 30.0

# tipar variables (type hints)
nombre: str = "Juan"

# operadores
suma = 5 + 3 # 8
resta = 5 - 3 # 2
multiplicacion = 5 * 3 # 15
division = 5 / 3 # 1.6666666666666667
division_entera = 5 // 3 # 1 (parte entera)
modulo = 5 % 3 # 2 (resto)
exponente = 5 ** 3 # 125 (5 elevado a la 3)

# operadores logicos
and_result = True and False # False
or_result = True or False # True
not_result = not True # False


# Métodos útiles para strings en Python

# len() - Obtiene la longitud de la cadena
cadena = "Hola Mundo"
print(f"Longitud: {len(cadena)}")  # Salida: 10

# upper() y lower() - Convierte a mayúsculas o minúsculas
print(cadena.upper())  # HOLA MUNDO
print(cadena.lower())  # hola mundo

# strip() - Elimina espacios en blanco al inicio y final
cadena_con_espacios = "  Hola  "
print(f"'{cadena_con_espacios.strip()}'")  # 'Hola'

# split() - Divide la cadena en una lista
frase = "Hola, cómo estás?"
palabras = frase.split()  # Divide por espacios
print(palabras)  # ['Hola,', 'cómo', 'estás?']

# join() - Une elementos de una lista en una cadena
lista_palabras = ["Hola", "mundo"]
cadena_unida = " ".join(lista_palabras)
print(cadena_unida)  # Hola mundo

# replace() - Reemplaza una subcadena por otra
texto = "Me gusta Python"
nuevo_texto = texto.replace("Python", "JavaScript")
print(nuevo_texto)  # Me gusta JavaScript

# find() - Encuentra la posición de una subcadena (devuelve -1 si no encuentra)
posicion = cadena.find("Mundo")
print(posicion)  # 5

# startswith() y endswith() - Verifica si comienza o termina con una subcadena
print(cadena.startswith("Hola"))  # True
print(cadena.endswith("Mundo"))   # True

# isalpha(), isdigit(), isalnum() - Verifica el tipo de caracteres
print("Hola".isalpha())  # True
print("123".isdigit())   # True
print("Hola123".isalnum())  # True

# format() - Formatea cadenas
nombre = "Ana"
edad = 25
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Hola, me llamo Ana y tengo 25 años.

# También se puede usar f-strings (más moderno)
mensaje_f = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje_f)

# Desempaqueado de caracteres
lenguage = "python"
a, b, c, d, e, f = lenguage
print(a)
print(e)

# División de cadenas (slicing)
lenguage_slice = lenguage[1:3] # Desde el índice 1 hasta el 3 (sin incluir el 3)
print(lenguage_slice)

lenguage_slice = lenguage[1:] # Desde el índice 1 hasta el final
print(lenguage_slice)

lenguage_slice = lenguage[-2] # Desde el final, el índice -1 es 'n', -2 es 'o'
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2] # Desde el índice 0 hasta el 6 (sin incluir el 6), con un paso de 2
print(lenguage_slice)

invertir_language = lenguage[::-1] # invertir la cadena
print(invertir_language)


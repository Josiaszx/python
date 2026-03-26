# manejo de ficheros

# leer, escribir y sobrescribir si ya existen archivos de texto
file = open("./files/tmp/archivo.txt", "w+") # "w+" para leer y escribir (sobrescribe si ya existe)

file.write("Hola, este es un archivo de texto.\n") # Escribir en el archivo
file.write("Esta es la segunda linea.")

# Posiciona el cursor al inicio del fichero
file.seek(0)

contenido = file.read() # Leer el contenido del archivo
print(contenido)

file.seek(0) 
caracteres = file.read(10) # Leer los primeros 10 caracteres
print(caracteres)

file.seek(0)
linea = file.readline() # Leer la primera linea del archivo
print(linea)


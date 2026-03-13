# tuplas -> listas inmutables
tupla = (1, "Hola", 3.14)
print(tupla) # (1, 'Hola', 3.14)

# desempaquetado de tuplas
num, texto, decimal = tupla
print(num) # 1
print(texto) # Hola
print(decimal) # 3.14

# las tuplas son inmutables, no se pueden modificar después de su creación
# tupla[0] = 2 # Esto generará un error

# convertir tupla a lista
lista = list(tupla) # Convertir tupla a lista
print(type(lista)) # <class 'list'>


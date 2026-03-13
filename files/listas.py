# listas
lista = []
lista2 = list()

# Agregar elementos a la lista
lista.append(1) # Agrega al final
lista.append("Hola")
lista.append(3.14)
print(lista) # [1, 'Hola', 3.14]

num, texto, decimal = lista # Desempaquetado de listas
print(num) # 1
print(texto) # Hola
print(decimal) # 3.14

# eliminar elementos de la lista
lista.remove("Hola") # Elimina el primer elemento que coincida
lista.pop() # Elimina el último elemento
lista.clear() # Elimina todos los elementos

# operaciones con listas
lista2 = [1, 2, 3]
lista2.reverse() # Invierte el orden de la lista
lista2.sort() # Ordena la lista (solo funciona con elementos comparables)

# sublistas (slicing)
sublista = lista2[1:3] # Desde el índice 1 hasta el 3 (sin incluir el 3)

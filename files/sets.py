# set -> estructura de datos que no permite elementos repetidos, no tiene orden, es mutable
conjunto = set()
conjunto.add(1) # Agrega un elemento al conjunto
conjunto.add(2)
conjunto.add(3)
print(conjunto) # {1, 2, 3}

# eliminar elementos del conjunto
conjunto.remove(2) # Elimina el elemento con indice 2 (genera error si no existe)

# operaciones con conjuntos
conjunto1 = {1, 2, 3}

# busqueda 
print(2 in conjunto1) # True
print(4 in conjunto1) # False

# operaciones de conjuntos
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2) # {1, 2, 3, 4, 5}
print(union)
interseccion = conjunto1.intersection(conjunto2) # {3}
print(interseccion)
diferencia = conjunto1.difference(conjunto2) # {1, 2} 
print(diferencia)
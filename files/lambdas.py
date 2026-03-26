# lambdas - funciones anónimas
sumar = lambda x, y: x + y # Función lambda que suma dos números
print(sumar(5, 3)) # 8

exp = lambda x, y: x ** y # Función lambda que eleva x a la potencia de y
print(exp(2, 3)) # 8

# funciones lambda con map y filter
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros)) # Aplica la función lambda a cada elemento de la lista
print(cuadrados) # [1, 4, 9, 16, 25]

pares = list(filter(lambda x: x % 2 == 0, numeros)) # Filtra los elementos de la lista que cumplen la condición
print(pares) # [2, 4]

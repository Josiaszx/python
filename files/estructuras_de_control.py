# if - elif (else if) - else
if True:
    num = 1
    # codigo ...
elif True:
    num = 2
    # codigo ...
else:
    num = 3
    # codigo ...

# for
for i in range(5): # range(inicio, fin, paso)
    print(i)

lista = [10, 20, 30] 
for numero in lista: # iterar lista (tambien funciona con tuplas, conjuntos, diccionarios, etc.)
    print(numero)

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break - salir del bucle
# continue - saltar a la siguiente iteración

# else en bucles - se ejecuta si el bucle termina normalmente (sin break)
for i in range(5):
    if i == 3:
        break
else:
    print("Bucle terminado sin break") # No se ejecutará porque el bucle se rompe en i == 3


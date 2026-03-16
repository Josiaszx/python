num = int(input("Ingrese un número: "))
try:
    # Código que puede generar una excepción
    resultado = 100 / num
except ZeroDivisionError as e:
    # en caso de que ocurra el error
    print("Error: No se puede dividir por cero.")
    print("Detalles del error:", e)
else: # opcional, se ejecuta si no ocurre ninguna excepción
    print("El resultado es:", resultado)
finally: # opcional, se ejecuta siempre, haya ocurrido o no una excepción
    print("Este bloque se ejecuta siempre.")
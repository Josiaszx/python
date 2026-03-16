# Diccionarios en Python: Explicación y métodos útiles

# Un diccionario es una estructura de datos que almacena pares clave-valor.
# Las claves deben ser inmutables (strings, números, tuplas), y los valores pueden ser cualquier tipo.

# Crear un diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print("Diccionario inicial:", persona)

# Acceder a valores
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Usar get() para acceder de forma segura (evita KeyError si la clave no existe)
print("Profesión (usando get):", persona.get("profesion", "No especificada"))

# Agregar o modificar elementos
persona["profesion"] = "Ingeniera"
print("Después de agregar profesión:", persona)

# Método keys(): devuelve una vista de las claves
print("Claves:", list(persona.keys()))

# Método values(): devuelve una vista de los valores
print("Valores:", list(persona.values()))

# Método items(): devuelve una vista de los pares clave-valor
print("Pares clave-valor:", list(persona.items()))

# Método update(): actualiza el diccionario con otro diccionario o pares clave-valor
persona.update({"edad": 26, "pais": "España"})
print("Después de update:", persona)

# Método pop(): elimina una clave y devuelve su valor
edad_eliminada = persona.pop("edad")
print("Edad eliminada:", edad_eliminada)
print("Diccionario después de pop:", persona)

# Método popitem(): elimina y devuelve el último par clave-valor (útil en pilas)
ultimo_item = persona.popitem()
print("Último item eliminado:", ultimo_item)
print("Diccionario después de popitem:", persona)

# Método clear(): vacía el diccionario
persona.clear()
print("Diccionario después de clear:", persona)

# Recrear el diccionario para más ejemplos
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Barcelona"
}

# Método copy(): crea una copia superficial
persona_copia = persona.copy()
persona_copia["edad"] = 31
print("Original:", persona)
print("Copia modificada:", persona_copia)

# Método fromkeys(): crea un diccionario con claves de un iterable y un valor opcional
claves = ["a", "b", "c"]
diccionario_nuevo = dict.fromkeys(claves, 0)
print("Diccionario creado con fromkeys:", diccionario_nuevo)

# Verificar si una clave existe
if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario")

# Iterar sobre el diccionario
print("Iterando sobre claves:")
for clave in persona:
    print(f"{clave}: {persona[clave]}")

print("Iterando sobre items:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Diccionarios anidados
empresa = {
    "departamentos": {
        "ventas": ["Ana", "Luis"],
        "marketing": ["María", "Pedro"]
    },
    "ubicacion": "Madrid"
}

print("Diccionario anidado:", empresa)
print("Empleados de ventas:", empresa["departamentos"]["ventas"])

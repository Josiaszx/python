# definir una clase
class Persona:
    def __init__(self, nombre, apellido, edad): # constructor
        self.nombre = nombre        # atributo de instancia
        self.apellido = apellido    # atributo de instancia
        self.edad = edad            # atributo de instancia

    def saludar(self): # método de instancia
        return f"Hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años."
    
    # Método estático
    @staticmethod
    def utilidad():
        return "Este es un método de utilidad"
    

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", "Perez", 30)
print(persona1.saludar()) # Hola, me llamo Juan Perez y tengo 30 años.

# llamar al metodo estatico
print(Persona.utilidad()) # Este es un método de utilidad

# acceder a los atributos
print(persona1.nombre) # Juan
print(persona1.apellido) # Perez
print(persona1.edad) # 30

# modificar atributos
persona1.nombre = "Carlos"
persona1.apellido = "Gomez"
persona1.edad = 31
print(persona1.saludar()) # Hola, me llamo Carlos Gomez y tengo 31 años.

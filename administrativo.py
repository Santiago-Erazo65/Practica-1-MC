# Administrativo.py
from Persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, edad, direccion, puesto):
        super().__init__(nombre, edad, direccion)  # Llamada al constructor de la clase base
        self.__puesto = puesto

    # Métodos getters y setters para 'puesto'
    def get_puesto(self):
        return self.__puesto

    def set_puesto(self, puesto):
        self.__puesto = puesto

    # Método __str__ para representar al administrativo como una cadena
    def __str__(self):
        return f"{super().__str__()}\nPuesto: {self.get_puesto()}"

    # Método mostrar_informacion para mostrar todos los datos del administrativo
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Muestra la información de la persona
        print(f"Puesto: {self.__puesto}")

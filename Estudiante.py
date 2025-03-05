# Estudiante.py
from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)  # Llamada al constructor de la clase base
        self.__curso = curso

    # Métodos getters y setters para 'curso'
    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    # Método __str__ para representar al estudiante como una cadena
    def __str__(self):
        return f"{super().__str__()}\nMatriculado en el curso: {self.get_curso()}"

    # Método mostrar_informacion para mostrar todos los datos del estudiante
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Muestra la información de la persona
        print(f"Curso: {self.__curso}")

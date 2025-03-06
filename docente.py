from Persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, direccion, especialidad):
        super().__init__(nombre, edad, direccion)  # Llamada al constructor de la clase base
        self.__especialidad = especialidad

    # Métodos getters y setters para 'especialidad'
    def get_especialidad(self):
        return self.__especialidad

    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    # Método __str__ para representar al docente como una cadena
    def __str__(self):
        return f"{super().__str__()}\nEspecialidad: {self.get_especialidad()}"

    # Método mostrar_informacion para mostrar todos los datos del docente
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Muestra la información de la persona
        print(f"Especialidad: {self.__especialidad}")

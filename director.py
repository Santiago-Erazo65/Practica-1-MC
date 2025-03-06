from Persona import Persona

class Director(Persona):
    def __init__(self, nombre, edad, direccion, area):
        super().__init__(nombre, edad, direccion)  # Llamar al constructor de Persona
        self.__area = area  # Área de gestión del director

    # Getter para 'area'
    def get_area(self):
        return self.__area

    # Setter para 'area'
    def set_area(self, area):
        self.__area = area

    # Método __str__ para representar al director como una cadena
    def __str__(self):
        return f"{super().__str__()}\nÁrea de gestión: {self.__area}"

    # Método para mostrar la información del director
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llama al método de Persona
        print(f"Área de gestión: {self.__area}")

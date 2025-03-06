class Persona:
    def __init__(self, nombre, edad, direccion):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion

    # Métodos getters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    # Método __str__ para representar el objeto como una cadena
    def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nDirección: {self.__direccion}"

    # Método para mostrar la información
    def mostrar_informacion(self):
        print("Nombre: ", self.__nombre," , Edad: ",self.__edad,", Direccion: ",self.__direccion)
        # print(f"Edad: {self.__edad}")
        # print(f"Dirección: {self.__direccion}")

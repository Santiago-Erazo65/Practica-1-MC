from Estudiante import Estudiante
from administrativo import Administrativo
from docente import Docente

# Listas para almacenar los objetos
list_students = []
list_admins = []
list_docents = []

# Funciones de Estudiante

def registrar_estudiante():
    print('Se va a registrar un estudiante')
    name = input('Ingresar el nombre: ')
    address = input('Ingresar la dirección: ')
    age = input('Ingresar la edad: ')
    course = input('Ingresar el curso: ')

    estudiante = Estudiante(name, age, address, course)  # Creación del objeto Estudiante
    list_students.append(estudiante)  # Agregar a la lista
    print('Estudiante guardado con éxito')

def mostrar_estudiantes():
    if len(list_students) == 0:
        print("No hay estudiantes en la lista.")
    else:
        print('Listado de estudiantes:')
        for estudiante in list_students:
            estudiante.mostrar_informacion()

def actualizar_estudiante():
    nombre = input("Ingresa el nombre del estudiante a actualizar: ")
    for estudiante in list_students:
        if estudiante.get_nombre().lower() == nombre.lower():
            nuevo_curso = input(f"Ingresa el nuevo curso para '{nombre}': ")
            estudiante.set_curso(nuevo_curso)
            print(f"Curso actualizado a '{nuevo_curso}' para '{nombre}'.")
            return
    print(f"Estudiante '{nombre}' no encontrado.")

def eliminar_estudiante():
    nombre = input("Ingresa el nombre del estudiante a eliminar: ")
    for estudiante in list_students:
        if estudiante.get_nombre().lower() == nombre.lower():
            list_students.remove(estudiante)
            print(f"Estudiante '{nombre}' eliminado con éxito.")
            return
    print(f"Estudiante '{nombre}' no encontrado.")

# Funciones de Administrativo
def registrar_administrativo():
    print('Se va a registrar un administrativo')
    name = input('Ingresar el nombre: ')
    address = input('Ingresar la dirección: ')
    age = input('Ingresar la edad: ')
    puesto = input('Ingresar el puesto: ')

    administrativo = Administrativo(name, age, address, puesto)  # Creación del objeto Administrativo
    list_admins.append(administrativo)  # Agregar a la lista
    print('Administrativo guardado con éxito')

def mostrar_administrativos():
    if len(list_admins) == 0:
        print("No hay administrativos en la lista.")
    else:
        print('Listado de administrativos:')
        for administrativo in list_admins:
            administrativo.mostrar_informacion()

def actualizar_administrativo():
    nombre = input("Ingresa el nombre del administrativo a actualizar: ")
    for administrativo in list_admins:
        if administrativo.get_nombre().lower() == nombre.lower():
            nuevo_puesto = input(f"Ingresa el nuevo puesto para '{nombre}': ")
            administrativo.set_puesto(nuevo_puesto)
            print(f"Puesto actualizado a '{nuevo_puesto}' para '{nombre}'.")
            return
    print(f"Administrativo '{nombre}' no encontrado.")

def eliminar_administrativo():
    nombre = input("Ingresa el nombre del administrativo a eliminar: ")
    for administrativo in list_admins:
        if administrativo.get_nombre().lower() == nombre.lower():
            list_admins.remove(administrativo)
            print(f"Administrativo '{nombre}' eliminado con éxito.")
            return
    print(f"Administrativo '{nombre}' no encontrado.")

# Funciones de Docente
def registrar_docente():
    print('Se va a registrar un docente')
    name = input('Ingresar el nombre: ')
    address = input('Ingresar la dirección: ')
    age = input('Ingresar la edad: ')
    especialidad = input('Ingresar la especialidad (asignatura): ')

    docente = Docente(name, age, address, especialidad)  # Creación del objeto Docente
    list_docents.append(docente)  # Agregar a la lista
    print('Docente guardado con éxito')

def mostrar_docentes():
    if len(list_docents) == 0:
        print("No hay docentes en la lista.")
    else:
        print('Listado de docentes:')
        for docente in list_docents:
            docente.mostrar_informacion()

def actualizar_docente():
    nombre = input("Ingresa el nombre del docente a actualizar: ")
    for docente in list_docents:
        if docente.get_nombre().lower() == nombre.lower():
            nueva_especialidad = input(f"Ingresa la nueva especialidad para '{nombre}': ")
            docente.set_especialidad(nueva_especialidad)
            print(f"Especialidad actualizada a '{nueva_especialidad}' para '{nombre}'.")
            return
    print(f"Docente '{nombre}' no encontrado.")

def eliminar_docente():
    nombre = input("Ingresa el nombre del docente a eliminar: ")
    for docente in list_docents:
        if docente.get_nombre().lower() == nombre.lower():
            list_docents.remove(docente)
            print(f"Docente '{nombre}' eliminado con éxito.")
            return
    print(f"Docente '{nombre}' no encontrado.")

# Menú Estudiantes
def menu_estudiante():
    while True:
        print("""
        --- MENÚ ESTUDIANTES ---
        1. Registrar estudiante
        2. Consultar listado de estudiantes
        3. Actualizar curso de estudiante
        4. Eliminar estudiante
        5. Volver al menú principal
        """)
        op = input("Selecciona una opción: ")
        if op == '1':
            registrar_estudiante()
        elif op == '2':
            mostrar_estudiantes()
        elif op == '3':
            actualizar_estudiante()
        elif op == '4':
            eliminar_estudiante()
        elif op == '5':
            break
        else:
            print("Opción inválida.")

# Menú Administrativos
def menu_administrativo():
    while True:
        print("""
        --- MENÚ ADMINISTRATIVOS ---
        1. Registrar administrativo
        2. Consultar listado de administrativos
        3. Actualizar puesto de administrativo
        4. Eliminar administrativo
        5. Volver al menú principal
        """)
        op = input("Selecciona una opción: ")
        if op == '1':
            registrar_administrativo()
        elif op == '2':
            mostrar_administrativos()
        elif op == '3':
            actualizar_administrativo()
        elif op == '4':
            eliminar_administrativo()
        elif op == '5':
            break
        else:
            print("Opción inválida.")

# Menú Docentes
def menu_docente():
    while True:
        print("""
        --- MENÚ DOCENTES ---
        1. Registrar docente
        2. Consultar listado de docentes
        3. Actualizar especialidad de docente
        4. Eliminar docente
        5. Volver al menú principal
        """)
        op = input("Selecciona una opción: ")
        if op == '1':
            registrar_docente()
        elif op == '2':
            mostrar_docentes()
        elif op == '3':
            actualizar_docente()
        elif op == '4':
            eliminar_docente()
        elif op == '5':
            break
        else:
            print("Opción inválida.")

# Menú principal
def menu_principal():
    while True:
        print("""
        --- MENÚ PRINCIPAL ---
        1. Gestionar Estudiantes
        2. Gestionar Administrativos
        3. Gestionar Docentes
        4. Salir
        """)
        op = input("Selecciona una opción: ")
        if op == '1':
            menu_estudiante()
        elif op == '2':
            menu_administrativo()
        elif op == '3':
            menu_docente()
        elif op == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

# Iniciar el menú principal
menu_principal()

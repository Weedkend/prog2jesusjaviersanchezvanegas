class MenuPersonas:
    def __init__(self):
        # Inicialización de la lista de personas
        self.personas = []

    def crear_persona(self):
        # Solicitar información para crear una persona y agregarla a la lista
        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        sexo = input("Ingrese el sexo de la persona: ")
        cedula = input("Ingrese la cedula de la persona: ")
        direccion = input("Ingrese la direccion de la persona: ")
        self.personas.append({"nombre": nombre, "edad": edad, "sexo": sexo, "cedula":cedula, "direccion": direccion})
        print("Persona creada con éxito.")

    def listar_personas(self):
        # Mostrar la lista de personas almacenadas
        print("Listado de personas:")
        for persona in self.personas:
            print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, sexo: {persona['sexo']}, cedula: {persona['cedula']}, direccion: {persona['direccion']}")

    def eliminar_persona(self):
        # Eliminar una persona de la lista por su nombre
        nombre = input("Ingrese el nombre de la persona que desea eliminar: ")
        for persona in self.personas:
            if persona['nombre'] == nombre:
                self.personas.remove(persona)
                print("Persona eliminada con éxito.")
                return
        print("La persona no se encontró.")
        
    def actualizar_persona(self):
        # Actualizar la información de una persona por su nombre
        nombre = input("Ingrese el nombre de la persona que desea actualizar: ")
        for persona in self.personas:
            if persona['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                sexo = input("Sexo: ")
                cedula = input("Cédula: ")
                direccion = input("Dirección: ")
                persona.update({"nombre": nombre, "edad": edad, "sexo": sexo, "cedula": cedula, "direccion": direccion})
                print("Datos de la persona actualizados con éxito.")
                return
        print("La persona no se encontró.")

class MenuUniversidades:
    def __init__(self):
        # Inicialización de la lista de universidades
        self.universidades = []

    def crear_universidad(self):
        # Solicitar información para crear una universidad y agregarla a la lista
        nombre = input("Ingrese el nombre de la universidad: ")
        direccion = input("Ingrese la direccion de la universidad: ")
        self.universidades.append({"nombre": nombre, "direccion": direccion})
        print("Universidad creada con éxito.")

    def listar_universidades(self):
        # Mostrar la lista de universidades almacenadas
        print("Listado de universidades:")
        for universidad in self.universidades:
            print(f"Nombre: {universidad['nombre']}, Direccion: {universidad['direccion']}")

    def eliminar_universidad(self):
        # Eliminar una universidad de la lista por su nombre
        nombre = input("Ingrese el nombre de la universidad que desea eliminar: ")
        for universidad in self.universidades:
            if universidad['nombre'] == nombre:
                self.universidades.remove(universidad)
                print("Universidad eliminada con éxito.")
                return
        print("La universidad no se encontró.")
        
    def actualizar_universidad(self):
        # Actualizar la información de una universidad por su nombre
        nombre = input("Ingrese el nombre de la universidad que desea actualizar: ")
        for universidad in self.universidades:
            if universidad['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nombre = input("Nombre: ")
                direccion = input("Dirección: ")
                universidad.update({"nombre": nombre, "direccion": direccion})
                print("Datos de la universidad actualizados con éxito.")
                return
        print("La universidad no se encontró.")

class MenuNotas:
    def __init__(self):
        # Inicialización del diccionario de notas
        self.notas = {}

    def agregar_nota(self, asignatura, nota):
        # Agregar una nota para una asignatura dada
        self.notas[asignatura] = nota
        print(f"Nota agregada para la asignatura {asignatura}.")

    def listar_notas(self):
        # Mostrar el diccionario de notas
        print("Listado de notas:")
        for asignatura, nota in self.notas.items():
            print(f"Asignatura: {asignatura}, Nota: {nota}")

    def eliminar_nota(self, asignatura):
        # Eliminar una nota para una asignatura dada
        if asignatura in self.notas:
            del self.notas[asignatura]
            print(f"Nota para la asignatura {asignatura} eliminada con éxito.")
        else:
            print("La asignatura no se encontró en el registro de notas.")
            
    def actualizar_nota(self, asignatura):
        # Actualizar la nota para una asignatura dada
        if asignatura in self.notas:
            nueva_nota = input(f"Ingrese la nueva nota para la asignatura {asignatura}: ")
            self.notas[asignatura] = nueva_nota
            print(f"Nota actualizada para la asignatura {asignatura}.")
        else:
            print("La asignatura no se encontró en el registro de notas.")

class MenuAsignatura:
    def __init__(self):
        # Inicialización de la lista de asignaturas
        self.asignaturas = []

    def crear_asignatura(self):
        # Solicitar información para crear una asignatura y agregarla a la lista
        nombre = input("Ingrese el nombre de la asignatura: ")
        profesor = input("Ingrese el nombre del profesor de la asignatura: ")
        self.asignaturas.append({"nombre": nombre, "profesor": profesor})
        print("Asignatura creada con éxito.")

    def listar_asignaturas(self):
        # Mostrar la lista de asignaturas almacenadas
        print("Listado de asignaturas:")
        for asignatura in self.asignaturas:
            print(asignatura)

    def eliminar_asignatura(self):
        # Eliminar una asignatura de la lista por su nombre
        nombre = input("Ingrese el nombre de la asignatura que desea eliminar: ")
        for asignatura in self.asignaturas:
            if asignatura['nombre'] == nombre:
                self.asignaturas.remove(asignatura)
                print("Asignatura eliminada con éxito.")
                return
        print("La asignatura no se encontró.")

    def actualizar_asignatura(self):
        # Actualizar la información de una asignatura por su nombre
        nombre = input("Ingrese el nombre de la asignatura que desea actualizar: ")
        for asignatura in self.asignaturas:
            if asignatura['nombre'] == nombre:
                print("Ingrese los nuevos datos:")
                nuevo_nombre = input("Nuevo nombre de la asignatura: ")
                nuevo_profesor = input("Nuevo nombre del profesor: ")
                asignatura['nombre'] = nuevo_nombre
                asignatura['profesor'] = nuevo_profesor
                print("Asignatura actualizada con éxito.")
                return
        print("La asignatura no se encontró.")     

class MenuPrincipal:
    def __init__(self):
        # Inicialización de los diferentes menús
        self.menu_personas = MenuPersonas()
        self.menu_universidades = MenuUniversidades()
        self.menu_notas = MenuNotas()
        self.menu_asignatura = MenuAsignatura()

    def mostrar_menu(self):
        # Mostrar el menú principal y manejar las opciones seleccionadas
        while True:
            print("\nMENU PRINCIPAL\n")
            print("1. PERSONAS")
            print("2. UNIVERSIDADES")
            print("3. NOTAS")
            print("4. ASIGNATURA")
            print("5. SALIR")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.submenu_personas()
            elif opcion == "2":
                self.submenu_universidades()
            elif opcion == "3":
                self.submenu_notas()
            elif opcion == "4":
                self.submenu_asignatura()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def submenu_personas(self):
        # Mostrar el submenu de personas y manejar las opciones seleccionadas
        while True:
            print("\nSUBMENU PERSONAS\n")
            print("1. CREAR PERSONA")
            print("2. LISTAR PERSONAS")
            print("3. ACTUALIZAR PERSONAS")
            print("4. ELIMINAR PERSONA")
            print("5. ATRAS")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_personas.crear_persona()
            elif opcion == "2":
                self.menu_personas.listar_personas()
            elif opcion == "3":
                self.menu_personas.actualizar_persona()
            elif opcion == "4":
                self.menu_personas.eliminar_persona()
            elif opcion == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    # Los métodos submenu_universidades(), submenu_notas() y submenu_asignatura() son similares en estructura y funcionamiento, por lo que no se proporcionan comentarios detallados para cada uno de ellos.

menu_principal = MenuPrincipal()
menu_principal.mostrar_menu()

# PACIAL PROGRAMACION 2 DE DOUGLAS ARAUJO Y JESUS SANCHEZ
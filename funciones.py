def agregar_estudiante():
    print       ("--- Agregar estudiante ---")
    rut         = input("Ingrese RUT: ")
    nombre      = input("Ingrese nombre: ")
    carrera     = input("Ingrrese carrera: ")
    edad        = int(input("Ingrese edad: "))
    
    estudiante = {"rut":rut, "nombre": nombre, "carrera": carrera,"edad": edad}
    print("Estudiante agregado correctamente")
    
    return estudiante
         


def listar_estudiantes(estudiantes):
    
    if len(estudiantes) == 0:
        print("la lista no tiene estudiantes registrados")
    else:
        print("\n--- Lista de estudiantes ---")
        for estudiante in estudiantes:
            print(estudiante)


def buscar_estudiante(estudiantes, rut):
    print("\n--- Buscar estudiante ---")

    encontrado = False

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            print("Estudiante encontrado")
            print(f"RUT: {estudiante['rut']}")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Carrera: {estudiante['carrera']}")
            print(f"Edad: {estudiante['edad']}")
            encontrado = True

        if encontrado == False:
            print("No se encontró el estudiante")


def actualizar_estudiante(estudiantes, rut):
    print("--- Actualizar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            nueva_edad = input("Ingrese nueva edad: ")

            estudiante["nombre"] = nuevo_nombre
            estudiante["carrera"] = nueva_carrera
            estudiante["edad"] == nueva_edad
            print("Estudiante actualizado correctamente")
            return
    print("No se encontró el estudiante")
            



def eliminar_estudiante(estudiantes, rut):
    print("--- Eliminar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente")
            return
        
    print("No se encontró el estudiante")

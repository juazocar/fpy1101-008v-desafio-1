def agregar_estudiante():
    
    print       ("--- Agregar estudiante ---")

    while True:
        rut = input("Ingrese RUT: ")
        if rut == "":
            print("El RUT no puede estar vacío")
        elif len(rut) != 9:
            print("El RUT debe tener 8 dígitos")
        else:
            break

    while True:
        nombre = input("Ingrese nombre: ")
        if nombre == "":
            print("El nombre no puede estar vacío")
        else:
            break

    while True:
        carrera = input("Ingrese carrera: ")
        if carrera == "":
            print("Tienes que ingresar una carrera")
        else:
            break

    while True:
        edad = input("Ingrese edad: ")
        if edad == "":
            print("Tienes que ingresar una edad")
        elif not edad.isdigit():
            print("La edad debe ser un número")
        else:
            edad = int(edad)
            if edad < 0:
                print("La edad no puede ser negativa")
            elif edad > 99:
                print("La edad no puede ser mayor a 99")

            else:
                break

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
    sn=input("¿Está seguro que desea eliminar el estudiante? (s/n): ")
    if sn.lower() != "s":
        print("Operación cancelada")
        return
    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente")
            return
            
    print("No se encontró el estudiante")


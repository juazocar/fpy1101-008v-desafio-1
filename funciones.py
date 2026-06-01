"""
Actividad DUOC UC - Debugging con Python
Archivo de funciones: funciones.py

Este archivo contiene las funciones del CRUD.
Tiene errores intencionales de sintaxis, lógica y uso de parámetros.
"""

def agregar_estudiante(estudiantes):
    print("\n--- Agregar estudiante ---")
    
    
    rutChk = False
    while rutChk == False:
        try:
            rut = int(input("Ingrese rut: "))
            # Verificación para no repetir RUT
            repetido = False
            for est in estudiantes:
                if est["rut"] == rut:
                    repetido = True
            
            if repetido:
                print("Error: Este RUT ya está registrado.")
            else:
                rutChk = True

        except ValueError:
            print("Tienes que ingresar un número entero")    

    # Asegurar que escriban un nombre de usuario
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese nombre: ").strip()
        if nombre == "":
            print("Error: El nombre no puede estar vacío.")

    # Asegurar que escriban algo en carrera
    carrera = ""
    while carrera == "":
        carrera = input("Ingrese carrera: ").strip()
        if carrera == "":
            print("Error: La carrera no puede estar vacía.")

    edadChk = False
    while edadChk == False:
        try:
            edad = int(input("Ingrese edad: "))
            edadChk = True
        except ValueError:
            print("Error: La edad debe ser un número entero")
    estudiante = {
        "rut": rut,
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente")


def listar_estudiantes(estudiantes):
    print("\n--- Lista de estudiantes ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        for i in range(len(estudiantes)):
            print(f"RUT: {estudiantes[i]['rut']}")
            print(f"Nombre: {estudiantes[i]['nombre']}")
            print(f"Carrera: {estudiantes[i]['carrera']}")
            print(f"Edad: {estudiantes[i]['edad']}")
            print("------------------------")


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
    print("\n--- Actualizar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            # Validación numero entero
            while True:
                try:
                    nueva_edad = int(input("Ingrese nueva edad: "))
                    break
                except ValueError:
                    print("Error: la edad debe ser un número entero.")

            estudiante["nombre"] = nuevo_nombre
            estudiante["carrera"] = nueva_carrera
            estudiante["edad"] = nueva_edad

            print("Estudiante actualizado correctamente")
            return

    print("No se encontró el estudiante")


def eliminar_estudiante(estudiantes, rut):
    print("\n--- Eliminar estudiante ---")

    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            # Confirmación para borrar
            print(f"Estudiante encontrado: {estudiante['nombre']}")
            confirmdelet = input("¿Está seguro que desea eliminar al estudiante? (S/N): ").upper()
            if confirmdelet == "S" or confirmdelet == "SI":
                estudiantes.remove(estudiante)
                print("Estudiante eliminado correctamente")
            else:
                print("Eliminación cancelada.")
            return

    print("No se encontró el estudiante")
import funciones as u

estudiantes = [

]
print("===== SISTEMA CRUD ESTUDIANTES DUOC UC =====")
print("1. Agregar estudiante")
print("2. Listar estudiantes")
print("3. Buscar estudiante")
print("4. Actualizar estudiante")
print("5. Eliminar estudiante")
print("6. Salir")

opcion = 0

while opcion != 6:

    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Error al ingresar la opción")

    if opcion == 1:
        estudiante = u.agregar_estudiante()
        estudiantes.append(estudiante)

    elif opcion == 2:
        u.listar_estudiantes(estudiantes)

    elif opcion == 3:
        rut = input("Ingrese RUT del estudiante a buscar: ")
        u.buscar_estudiante( estudiantes, rut)

    elif opcion == 4:
        rut = input("Ingrese RUT del estudiante a actualizar: ")
        u.actualizar_estudiante(estudiantes, rut)

    elif opcion == 5:
        rut = input("Ingrese RUT del estudiante a eliminar: ")
        u.eliminar_estudiante(estudiantes, rut)

    elif opcion == 6:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida")

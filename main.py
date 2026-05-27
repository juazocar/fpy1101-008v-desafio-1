"""
Actividad DUOC UC - Debugging con Python
Archivo principal: main.py

IMPORTANTE:
Este programa contiene errores intencionales.
La misión del estudiante es clonar el repositorio, crear una rama,
corregir los errores y dejar funcionando el CRUD.
"""

from funciones import (
    agregar_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante
)

estudiantes = []

def mostrar_menu():
    print("\n===== SISTEMA CRUD ESTUDIANTES DUOC UC =====")
    print("1. Agregar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")

opcion = 0

while opcion != 6:
    print(opcion)
    mostrar_menu()

    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Error al ingresar la opción")

    if opcion == 1:
        agregar_estudiante(estudiantes)

    elif opcion == 2:
        listar_estudiantes(estudiantes)

    elif opcion == 3:
        rut = input("Ingrese RUT del estudiante a buscar: ").upper().strip()
        buscar_estudiante(estudiantes, rut)

    elif opcion == 4:
        rut = input("Ingrese RUT del estudiante a actualizar: ").upper().strip()
        actualizar_estudiante(estudiantes, rut)

    elif opcion == 5:
        rut = input("Ingrese RUT del estudiante a eliminar: ").upper().strip()
        eliminar_estudiante(estudiantes, rut)

    elif opcion == 6:
        print("Saliendo del sistema...")

    
    else:
        print("Opción inválida")    

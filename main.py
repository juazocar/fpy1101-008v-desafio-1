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

# Corrección 1: Se agregan los dos puntos (:) obligatorios
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
    mostrar_menu()

    try:
        # Corrección 2: Convertimos el input a int para poder comparar números en el menú
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        opcion = 0 # Reiniciamos para evitar que mantenga un valor anterior
        continue # Saltamos el resto del ciclo para volver a pedir la opción

    if opcion == 1:
        agregar_estudiante(estudiantes)

    elif opcion == 2: # Ahora que es entero, quitamos las comillas "2"
        # Corrección 3: Se pasa el parámetro 'estudiantes' que faltaba
        listar_estudiantes(estudiantes)

    elif opcion == 3:
        rut = input("Ingrese RUT del estudiante a buscar: ")
        # Corrección 4: Se cambia 'nombre' por la variable correcta 'rut'
        buscar_estudiante(estudiantes, rut)

    elif opcion == 4:
        rut = input("Ingrese RUT del estudiante a actualizar: ")
        # Corrección 5: Se añade el parámetro 'rut' que faltaba
        actualizar_estudiante(estudiantes, rut)

    elif opcion == 5:
        rut = input("Ingrese RUT del estudiante a eliminar: ")
        # Corrección 6: Se corrige el orden de los parámetros (primero lista, luego rut)
        eliminar_estudiante(estudiantes, rut)

    elif opcion == 6:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida")
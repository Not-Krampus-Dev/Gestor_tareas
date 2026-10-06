import json


print("== GESTOR DE TAREAS ==")


# Carga las tareas guardadas en el archivo JSON.
def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)

    except FileNotFoundError:
        tareas = []

    except json.JSONDecodeError:
        tareas = []

    return tareas


# Guarda las tareas actuales en el archivo JSON.
def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

    print("Tareas guardadas correctamente.")


# Muestra el menú principal y permite seleccionar una acción.
def opcion_menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese el número de la opción: "))
        except ValueError:
            print("Opción inválida. Por favor, intente nuevamente.")
            continue

        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            ver_tareas()
        elif opcion == 3:
            completar_tarea()
        elif opcion == 4:
            eliminar_tarea()
        elif opcion == 5:
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


# Solicita una descripción y agrega una nueva tarea.
def agregar_tarea():
    tarea = input("Ingrese la descripción de la tarea: ").strip()

    if not tarea:
        print("La tarea no puede estar vacía.")
        return

    nueva_tarea = {
        "descripcion": tarea,
        "completada": False
    }

    tareas.append(nueva_tarea)

    print("Tarea agregada correctamente.")

    guardar_tareas()


# Muestra todas las tareas junto con su estado.
def ver_tareas():
    print("== TAREAS ==")

    for numero, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{numero}. [{estado}] {tarea['descripcion']}")


# Marca una tarea seleccionada como completada.
def completar_tarea():
    try:
        numero = int(input("Ingrese el número de la tarea: "))
    except ValueError:
        print("Número inválido.")
        return

    if numero < 1 or numero > len(tareas):
        print("Número fuera de rango.")
        return

    indice = numero - 1
    tarea = tareas[indice]

    tarea["completada"] = True

    print("Tarea completada correctamente.")

    guardar_tareas()


# Elimina una tarea seleccionada de la lista.
def eliminar_tarea():
    try:
        numero = int(input("Ingrese el número de la tarea que desea eliminar: "))
    except ValueError:
        print("Número inválido.")
        return

    if numero < 1 or numero > len(tareas):
        print("Número fuera de rango.")
        return

    indice = numero - 1
    tareas.pop(indice)

    print("Tarea eliminada correctamente.")

    guardar_tareas()


tareas = cargar_tareas()

opcion_menu()

estudiantes = []

def agregar():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    promedio = input("Promedio: ")

    if not edad.isdigit() or not promedio.replace(".", "", 1).isdigit():
        print("Edad o promedio inválido.\n")
        return

    edad = int(edad)
    promedio = float(promedio)

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado.\n")


def mostrar():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    for e in estudiantes:
        print(f"Nombre: {e['nombre']}, Edad: {e['edad']}, Promedio: {e['promedio']}")
    print()


def mejor_promedio():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    mejor = estudiantes[0]
    for e in estudiantes:
        if e["promedio"] > mejor["promedio"]:
            mejor = e

    print("Estudiante con mejor promedio:")
    print(f"Nombre: {mejor['nombre']}, Edad: {mejor['edad']}, Promedio: {mejor['promedio']}\n")


def buscar():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    nombre = input("Nombre a buscar: ")
    encontrado = False

    for e in estudiantes:
        if e["nombre"].lower() == nombre.lower():
            print(f"Nombre: {e['nombre']}, Edad: {e['edad']}, Promedio: {e['promedio']}")
            encontrado = True

    if not encontrado:
        print("No encontrado.\n")
    else:
        print()


def eliminar():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    nombre = input("Nombre a eliminar: ")
    eliminado = False

    for e in estudiantes:
        if e["nombre"].lower() == nombre.lower():
            estudiantes.remove(e)
            eliminado = True
            break

    if eliminado:
        print("Estudiante eliminado.\n")
    else:
        print("No encontrado.\n")

# --------------------------
# Menú principal iterativo
# --------------------------

while True:
    print("=== MENÚ ===")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")

    op = input("Opción: ")

    if op == "1":
        agregar()
    elif op == "2":
        mostrar()
    elif op == "3":
        mejor_promedio()
    elif op == "4":
        buscar()
    elif op == "5":
        eliminar()
    elif op == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.\n")
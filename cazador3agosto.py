
from datetime import datetime, date

# Lista donde guardamos las tareas
tareas = []

# Función para agregar una tarea
def agregar_tarea(titulo, fecha_str):
    try:
        deadline = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        tarea = {"titulo": titulo, "deadline": deadline, "hecha": False}
        tareas.append(tarea)
        print(" Tarea agregada.")
    except ValueError:
        print(" Fecha inválida. Usa el formato AAAA-MM-DD.")

# Función para calcular días restantes
def dias_restantes(fecha):
    return (fecha - date.today()).days

# Función para mostrar tareas ordenadas por deadline
def mostrar_tareas():
    for t in sorted(tareas, key=lambda x: x["deadline"]):
        estado = "" if t["hecha"] else ""
        print(f"{t['titulo']} - vence {t['deadline']} ({dias_restantes(t['deadline'])} días) {estado}")

# Función para marcar una tarea como hecha
def marcar_hecha(titulo):
    for t in tareas:
        if t["titulo"].lower() == titulo.lower():
            t["hecha"] = True
            print(" Tarea completada.")
            return
    print(" Tarea no encontrada.")

# ---------------- MENÚ ----------------
while True:
    print("\n--- Cazador de Tareas ---")
    print("1) Agregar tarea")
    print("2) Ver tareas")
    print("3) Marcar tarea como hecha")
    print("4) Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        titulo = input("Título: ")
        fecha = input("Deadline (AAAA-MM-DD): ")
        agregar_tarea(titulo, fecha)

    elif opcion == "2":
        mostrar_tareas()

    elif opcion == "3":
        titulo = input("Título de la tarea: ")
        marcar_hecha(titulo)

    elif opcion == "4":
        print(" Adiós")
        break

    else:
        print("Opción inválida")
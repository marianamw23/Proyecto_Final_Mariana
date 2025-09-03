#juego banco monedas de color rojo o azul
import json
from datetime import datetime

# Tesoro inicial
tesoro = {"rojo": 120, "azul": 85}
eventos = []  # lista de movimientos

# Guardar en JSON
def guardar():
    with open("tesoro.json", "w") as f:
        json.dump({"tesoro": tesoro, "eventos": eventos}, f, indent=4)
    print(" Tesoro guardado.")

# Cargar desde JSON
def cargar():
    global tesoro, eventos
    try:
        with open("tesoro.json", "r") as f:
            data = json.load(f)
            tesoro = data["tesoro"]
            eventos = data["eventos"]
        print(" Tesoro cargado.")
    except FileNotFoundError:
        print(" No hay archivo guardado todavía.")

# Depositar
def depositar(color, monto):
    if monto > 0:
        tesoro[color] = tesoro.get(color, 0) + monto
        registrar_evento("depositar", color, monto)
        print(f"Depositaste {monto} en {color}.")
    else:
        print(" El monto debe ser positivo.")

# Retirar
def retirar(color, monto):
    if monto > 0 and tesoro.get(color, 0) >= monto:
        tesoro[color] -= monto
        registrar_evento("retirar", color, monto)
        print(f" Retiraste {monto} de {color}.")
    else:
        print(" No puedes retirar ese monto.")

# Registrar evento
def registrar_evento(accion, color, monto):
    eventos.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "accion": accion,
        "color": color,
        "monto": monto,
        "total": tesoro.get(color, 0)
    })

# Mostrar total general
def total_general():
    return sum(tesoro.values())

# Menú principal
while True:
    print("\n--- TESORO ---")
    print("1) Depositar")
    print("2) Retirar")
    print("3) Ver total")
    print("4) Guardar / Cargar")
    print("5) Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        color = input("Color: ").lower()
        try:
            monto = int(input("Monto a depositar: "))
            depositar(color, monto)
        except ValueError:
            print(" Ingresa un número válido.")

    elif opcion == "2":
        color = input("Color: ").lower()
        try:
            monto = int(input("Monto a retirar: "))
            retirar(color, monto)
        except ValueError:
            print(" Ingresa un número válido.")

    elif opcion == "3":
        print("Tesoro actual:", tesoro)
        print(" Total general:", total_general())

    elif opcion == "4":
        sub = input("¿Quieres (g)uardar o (c)argar? ").lower()
        if sub == "g":
            guardar()
        elif sub == "c":
            cargar()

    elif opcion == "5":
        print(" Saliendo...")
        break

    else:
        print(" Opción no válida.")
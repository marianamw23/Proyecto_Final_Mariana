#1)ruleta de frutas
import random

# Lista de frutas
frutas = ["manzana", "piña", "banano", "arandano", "fresa", "mango"]

secreta = random.choice(frutas)

# Número máximo de intentos
max_intentos = 5
intentos = 0

print(" Juego: Adivina la fruta secreta ")


while intentos < max_intentos:
    intento = input("Escribe el nombre de una fruta: ").lower()

    intentos += 1

    if intento == secreta:
        print(" Ganaste, la fruta secreta era:", secreta)
        break
    else:
        print(" No es esa fruta. tienes:", max_intentos - intentos, "intentos.")

if intento != secreta:
    print(" Perdiste. La fruta secreta era:", secreta)
    
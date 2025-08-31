# mariana_macias.py

print("hola,este es mi primer commit")

import pandas as pd

# Leer archivo CSV
ingredientes_df = pd.read_csv("ingredientess.csv")

# Normalizar texto
ingredientes_df["ingrediente"] = ingredientes_df["ingrediente"].str.lower().str.strip()

def analizar_producto(ingredientes):
    puntaje = 0
    riesgos, beneficios, neutros, no_clasificados = [], [], [], []

    for ing in ingredientes:
        ing_norm = ing.lower().strip()
        fila = ingredientes_df[ingredientes_df["ingrediente"] == ing_norm]

        if not fila.empty:
            tipo = fila.iloc[0]["tipo"]
            valor = int(fila.iloc[0]["puntaje"])
            puntaje += valor

            if tipo == "riesgoso":
                riesgos.append(ing)
            elif tipo == "beneficioso":
                beneficios.append(ing)
            elif tipo == "neutro":
                neutros.append(ing)
        else:
            no_clasificados.append(ing)

    # Resultados
    print("\n🔍 RESULTADOS DEL ANÁLISIS")
    print("-------------------------")
    print("❌ Riesgosos:", riesgos)
    print("✅ Beneficiosos:", beneficios)
    print("⚪ Neutros:", neutros)
    print("❓ No clasificados:", no_clasificados)
    print(f"\nPuntaje final: {puntaje}")

    if puntaje > 2:
        print("🌿 Producto recomendado")
    elif -2 <= puntaje <= 2:
        print("⚠️ Producto aceptable, pero con precaución")
    else:
        print("🚫 Producto no recomendado")

# -----------------------------
# EJEMPLO DE PRUEBA
ingredientes_prueba = [
    "Agua", 
    "Alcohol", 
    "Aloe Vera", 
    "Fragancia", 
    "Glicerina", 
    "Aceite de jojoba", 
    "Karité fermentado"
]

analizar_producto(ingredientes_prueba)
# mariana_macias.py

def presentar():
    print("hola,este es mi primer commit")

# Lista de ingredientes riesgosos con sus puntajes negativos 

ingredientes_riesgosos= {
    "paraben ":-2,
    "phenoxyethanol":-1,
    "triclosan":-3,
    "formaldedehyde":-5,
    "dmdm hydantoin": -4,
    "imidazolidinyl urea": -4,
    "sodium laurylsulfate": -3, 
    "sls": -3, 
    "sles": -3, 
    "alcohol denat": -2, 
    "ethanol": -2,
    "isopropyl alcohol": -2, 
    "dimethicone": -1,
    "cyclopentasiloxane": -1, 
    "petrolatum": -2, 
    "mineral oil": -2,
    "fragrance": -2,
    "parfum": -2,
    "colorant": -1,
    "fd&c": -1
}
# Lista de ingredientes seguros/beneficios con puntajes positivos
ingredientes_buenos ={"aloe vera":+3,"aloe vera": +3,
    "glycerin": +2,
    "hyaluronic acid": +3,
    "panthenol": +2,
    "urea": +1,
    "vitamin c": +3,
    "ascorbic acid": +3,
    "vitamin e": +2,
    "tocopherol": +2,
    "niacinamide": +3,
    "retinol": +2,
    "coenzyme q10": +2,
    "ferulic acid": +2,
    "jojoba oil": +2,
    "argan oil": +2,
    "coconut oil": +1,
    "almond oil": +2,
    "olive oil": +2,
    "shea butter": +2,
    "cocoa butter": +2,
    "allantoin": +2,
    "chamomile extract": +2,
    "centella asiatica": +3,
    "green tea extract": +2,
    "calendula extract": +2,
    "bisabolol": +2,
    "ceramides": +3,
    "peptides": +3,
    "zinc oxide": +3,
    "titanium dioxide": +3}

def analizar_cosmetico(lista_ingredientes):
    puntaje = 0
    riesgos = []
    beneficios = []
    for ing in lista_ingredientes:
        ing_lower = ing.lower()
        encontrado = False

        # Buscar si es riesgoso
        for riesgo in ingredientes_riesgosos:
            if riesgo in ing_lower:
                puntaje += ingredientes_riesgosos[riesgo]
                riesgos.append(ing)
                encontrado = True

 
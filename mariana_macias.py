#proyecto final clasificador de cosmeticos este codigo le pide al usuario que ingrese
#los ingredientes de su cosmetico y el programa clasificara cada ingrediente como beneficioso riesgoso o neutro

#  Analizador de ingredientes cosméticos

# Lista de ingredientes riesgosos con sus puntajes negativos
ingredientes_riesgosos = {
    "paraben": -2,
    "phenoxyethanol": -1,
    "triclosan": -3,
    "formaldehyde": -5,
    "dmdm hydantoin": -4,
    "imidazolidinyl urea": -4,
    "sodium lauryl sulfate": -3,
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
    "fd&c": -1,
    "oxybenzone" : -3,
    "toluene":-5,
    "oxybenzone": -3
}

# Lista de ingredientes seguros/beneficiosos con puntajes positivos
ingredientes_buenos = {
    "aloe vera": +3,
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
    "titanium dioxide": +3,
    "betaglucan": +2,
    "lactic acid": +1,
    "ceramide np" : +3,
    "ceramide ap": +3,
    "ceramide eop":+3,
    "phytic acid": +1,
    "citric acid":+1}
# Lista de ingredientes seguros/beneficiosos con puntajes positivos
ingredientes_neutros = {"agua":0,
    "glicerina":0,
    "carbomer":0,
    "cera de abejas":0,
    "cera candelilla":0,
    "cera carnauba":0,
    "estearato de glicerilo":0,
    "caprylic/capric triglyceride":0,
    "propylene glycol":0,
    "cetyl alcohol":0,
    "stearyl alcohol":0,
    "polysorbate 20":0,
    "polysorbate 60":0,
    "polysorbate 80":0,
    "dimethicone":0,
    "talco":0,
    "kaolin":0,
    "magnesio estearato":0,
    "peg-100 stearate":0,
    "disodium edta":0,
    "triethanolamine":0,
    "pvp":0,
    "xanthan gum":0,
    "hydroxyethylcellulose":0

    }


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

        # Buscar si es bueno
        for bueno in ingredientes_buenos:
            if bueno in ing_lower:
                puntaje += ingredientes_buenos[bueno]
                beneficios.append(ing)
                encontrado = True

        if not encontrado:
            print(f" {ing}: ingrediente no clasificado")

    # Evaluar puntaje
    if puntaje <= -3:
        estado = " Riesgoso para la piel"
    elif -2 <= puntaje <= 1:
        estado = " Neutro / uso moderado"
    else:
        estado = " Seguro y beneficioso"

    # Mostrar resultados
    print("\n Resultados del análisis:")
    print(f" Puntaje total: {puntaje}")
    print(f" Clasificación: {estado}")
    print(f" Riesgos detectados: {', '.join(riesgos) if riesgos else 'Ninguno'}")
    print(f" Ingredientes buenos: {', '.join(beneficios) if beneficios else 'Ninguno'}")



entrada= input("Ingrese la lista de ingredientes separados por comas :")
ingredientes_usuario=entrada.split(",")

analizar_cosmetico(ingredientes_usuario)
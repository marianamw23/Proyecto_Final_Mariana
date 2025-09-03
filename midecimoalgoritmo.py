#reforzar lista  diccionario
estudiante = {
    "Hernan Dario" : "Toolkit",
    "edad" : 17,
    "carrrera": "Ingenier"

}
print ("Nombre",estudiante ["Hernan Dario"])

#agregar elemeto al diccionario
estudiante ["nota"]=90

for clave , valor in estudiante.items():
    print(clave,":" , valor)
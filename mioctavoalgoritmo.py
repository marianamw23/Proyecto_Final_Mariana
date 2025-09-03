#colocar numeros aleatorios
import random
dado=random.randint(1,6)#rango
print("el dado muestra el numero :",dado)
#genere el numero decimal entre cero y uno
decimal= random.random() 
print("numero decimal aleatorio",decimal)
#escoger un elemento aleatorio
frutas= ["manzana" ,"pera" ," uva" ,"mango"]
eleccion = random.choice (frutas)

print ("La fruta elegida es :",eleccion)

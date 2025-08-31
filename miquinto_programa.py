# Este es un programa para entrenarme 
Frutas = ["manzana", "pera","banana","fresa","uva","naranja"]
# El error en la lista era una coma extra después de "banana" y comillas faltantes.
# También corregí el espacio después de "uva".

print(Frutas) 
# Esto imprime la lista completa.
# Para imprimir solo el primer elemento (índice 0), usarías: print(Frutas[0])

Frutas.insert(2,"kiwi")
# El método .insert() necesita un índice y un valor.
# Aquí insertamos "kiwi" en el índice 2, moviendo "banana" y los siguientes elementos.
# El índice 10 estaba fuera de rango para una lista con 6 elementos.

Frutas.pop(0)
# El método .pop() elimina un elemento. Sin un índice, elimina el último. 
# Si especificas un índice, como .pop(0), elimina el elemento en esa posición (en este caso, "manzana").
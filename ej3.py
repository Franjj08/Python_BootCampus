#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.

peso= float(input("Ingrese tu peso en kg: "))
print(peso,"kg")

estatura= float(input("Ingrese tu estatura en m: "))
print(estatura,"m")

indiceDeMasaCorporal = peso / estatura**estatura
print("Tu indice de masa corporal es:",round(indiceDeMasaCorporal,2))
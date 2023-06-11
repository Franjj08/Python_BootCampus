# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open('archivo.txt','w')
f.write("datos\n")
f.write("datos2\n")
f.close()

f = open('archivo.txt', 'r')
contenido = f.read()
f.close()
print(contenido)
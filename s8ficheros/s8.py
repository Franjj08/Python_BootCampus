import pickle
class Juguete:
    nombre =""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def getNombre(self):
        return self.nombre

# j1 = Juguete("Potato", 10.5)
# f = open('datos.bin','wb')#serilizar datos writ + binario cargar datos en disco
# pickle.dump(j1,f)
# f.close

f = open('datos.bin','rb')
potato = pickle.load(f)
f.close
print(type(potato))
print(potato.getNombre())
# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle
class Vehiculo:
    nombre =""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def getNombre(self):
        return self.nombre
j1 = Vehiculo("v1", 10.5)
f = open('datos1.bin','wb')#serilizar datos writ + binario cargar datos en disco
pickle.dump(j1,f)
f.close

f = open('datos1.bin','rb')
vehiculo = pickle.load(f)
f.close
print(type(vehiculo))
print(vehiculo.getNombre())
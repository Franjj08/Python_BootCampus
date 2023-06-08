from abc import ABC, abstractmethod

class Juguete:#clase dinamica
    
    def __init__(self):
        print("Estoy en la clase jueguete")
    _encendido = True#_noSePuedeTocarDesdeAfuera

    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido

d = Juguete()
#d.encendido = True#Python todo es publico no exite privado
d.apaga()
print(d.isEncendido())

class Estatica:# las clases estaticas comparten misma zona de memoria
    numero = 1

    def incrementa():
        Estatica.numero +=1

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

class Potato(Juguete):#clase dinamica
    
    def __init__(self):
        print("Estoy en la clase Potato")

    def quitarOreja(self):
        pass
    
    def ponerOreja(self):
        pass

class Dino(Potato):#herencia multiple menor a mayo
    nombre = None
    def __init__(self, nombre):#constructor
       #Juguete.__init__(self)
       super().__init__()
       print("Estoy en la clase de Dino")
      # self.nombre = nombre
        
    def haceRuido(self):
        return"Ahhhh"

p = Dino("midinosaurito")


class Animal(ABC):#class abastracta sirve para definir un conjuntos de funciones a otras clases
    @abstractmethod
    def sonido(self):
        pass
    
class Perro(Animal):
    def sonido(self):
        print("Guau")

p = Perro()
p.sonido()

class Coche:#composicion de class
    motor = Motor()
    ventana = Ventanas()
    

class Motor:
    pass

class Ventanas:
    pass

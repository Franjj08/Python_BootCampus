numero = 511
texto = "quijote"
otromas = 1.2

#print("El numero es %d y el texto es %s y tiene %f" %(numero, texto, otromas))

# print("El numero es {num} y el texto es {text} y tiene {flt}".format(num =numero, text=texto, flt=otromas))

print(f'El numero es{numero} y el texto es {texto.upper()} y tiene {otromas}')

class Juguete:
    nombre = ""
    precio= 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):#Para codigo de produccion
        return f"Mi nombre es {self.nombre} y mi precio {self.precio}"
    def __repr__(self):#Para codig depuracion o en desarrollo tecnico
        return f"Potato({self.nombre},{self.precio})"
    
# j1 = Juguete("Potato", 10.5)
# print(str(j1))
# print(repr(j1))

import pprint
pprint.pprint(dir(''))
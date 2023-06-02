tupla = ("x", 2)
print(tupla)

lsita = ["x", 2]
print(lsita)

diccionario= {
    "clave":2
}
print(diccionario)

conjunto = {1,2,3,1,2,3} #un conjunto no hay elemento repetido
print(conjunto)
a = {1,2,3,1,2,3,4} 
b = {4,5,6,4,5,6}
print(a | b)# union
print(a & b)#interseccion
print(a -b)#lo que no esta en b
print(a ^b)#lo que no se repite entre los dos conjuntos

a = 5
a +=6
b = 2
print(a**b)

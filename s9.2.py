from functools import reduce
# import logging

# logging.basicConfig(level=logging.INFO)
# logging.debug("Prueba de debug")
# logging.info("Arrancando programa")
# logging.warning("hace calor")
# logging.error("test")
# logging.critical("adios")

numeros = [1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x% 2 == 0:
        return True
resultado=filter(mifuncion, numeros)#queda lo que return True, es un iterador interno

print(list(resultado))


def cuadrado(x):
    return x *x

resultado = map( cuadrado, [1,2,3,4,])#lambda x: x*x
print(list(resultado))

def suma(a,b):
    return a +b
res = reduce( suma, [1,2,3,4,5])#se ejecuta recursivamente hasta que se queda con unico elemeento de la lista

print(res)

cursos  = ['Java','Python']
asistentes = [15,6]
demo = zip(cursos, asistentes)
print(list(demo))
# all() , any(), round(), min(), pow(2,4), sorted()

a = int(input("tu edad?"))
print(f'hola,{a}')
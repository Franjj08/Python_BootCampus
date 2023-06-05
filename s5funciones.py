hoyHace = 12.8

def mifuncion(hoyhace=13):#parametro opcional a partir un parametro opcional ,los que estan atras tmb tiene que ser opcional
    global hoyHace #cambia valor de variable global
    hoyHace = 6.0

mifuncion(hoyHace)

print(hoyHace)

def suma(*args):#*args como array
    resultado = 0

    for arg in args:
        resultado += arg
    return resultado

print(suma(1,9))

def mostrar(**kwargas):#**kwargas como diccionario
    if kwargas['coche'] == 'bonito':
        print("hola")
    for key, value in kwargas.items():
        print(key,"=",value)

mostrar(vivienda="piso", coche="rojo")

#funcion anonima no tiene retrun 
anonima = lambda nombre, nombre2:print("hola", nombre, "adios",nombre2)
anonima('pepe',"pepe2")
    
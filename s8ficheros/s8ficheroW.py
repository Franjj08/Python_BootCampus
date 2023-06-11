# f = open('mifichero.txt', 'w')
# # f.write("datos\n")
# # f.write("datos2\n")
# lista =[
#     'Una linea\n',
#     'Dos lineas\n',
#     'Tres lineas\n'
# ]
# f.writelines(lista)

# f.close

def escribe(fichero, datos):
    f = open(fichero, 'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea +'\n'
        
        f.write(linea)
    f.close()

lista =[
    'Una linea',
    'Dos lineas',
    'Tres lineas'
]

escribe('mifichero.txt',lista)
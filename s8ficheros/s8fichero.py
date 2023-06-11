# r: lectura
# a: append
# w:escritura
# x:create
# t:texto
# b:binary

def main():
    usuarios = listarUsuarios()
    for usuario in usuarios:
        print(f'Usuarios: {usuario}')

def listarUsuarios():
    f = open('file.txt', 'r')
    datos = f.readlines()
    f.close()
    resultado = []
    for line in datos:
        if line[0] =='3':
            continue
        
        partes = line.split('1')
        
        resultado.append(partes[0])
    return resultado
if __name__ == '__main__':
    main()

# f = open('mifichero.txt', 'w')
# f.write("datos\n")
# f.write("datos2")
# f.close
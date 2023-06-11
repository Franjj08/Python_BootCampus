#modulo: es un fichero con extension .py
import s7operaciones as o 
import sys
import pprint


def main():
#     res = o.suma(2,2)
#     print("Hola en main()", res)
    op =  o.Operador()
#   print(op.multiplicacion(4,2))
    print(o.PI)
    pprint.pprint(sys.path)

if __name__ == '__main__':
    main()
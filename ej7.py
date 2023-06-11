# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

import ej7Operaciones as op

def main():
    print(op.suma(1,2))
    print(op.restar(1,2))
    print(op.multiplicar(1,2))
    print(op.dividir(1,2))

if __name__ == '__main__':
    main()
# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

def pedir_paises(paises):
    pais= input("Ingrese paises, salir con q :")
    while pais != 'q':
        paises.append(pais)
        pais= input("Ingrese paises, salir con q :")
    paises.sort()
       


def main():
    paises= []
    pedir_paises(paises)
    print(list(paises))
 
if __name__ == '__main__':
    main()
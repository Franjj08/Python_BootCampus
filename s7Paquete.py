import operaciones.suma
import math

def main():
  #print(operaciones.suma.suma(2,2))
   mp = operaciones.suma.Mutiplicador()

   print(mp.multiplica(5,5))
   help(mp.multiplica)
if __name__ == '__main__':
    main()
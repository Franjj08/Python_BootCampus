#built-in: las funciones que traen el propio lenguaje, implementada a nivek de interprete ej:abs()

import _thread
import time

def horaActual(nombbre_thread, tiempo_de_espera):
    count = 0

    while count < 5:
        time.sleep(tiempo_de_espera)
        count +=1
        print(f'hilo:{nombbre_thread} - {time.ctime(time.time())}')
#Tiene desbloquear mi programa para que se ejecute
_thread.start_new_thread(horaActual,("thread_uno",1))
_thread.start_new_thread(horaActual,("thread_dos",2))

print("He disparado ya los hilos")

while True:
    pass

import time



hora_actual = time.localtime().tm_hour

if  hora_actual >= 7:
    print('Es hora de ir a la casa')
else:
    hora_faltada = abs(hora_actual -7)
    print('Falta:'+ str(hora_faltada))